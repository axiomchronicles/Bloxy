document.addEventListener("DOMContentLoaded", function () {
  const searchInput = document.getElementById("searchInput");
  const resultsList = document.getElementById("resultsList");
  const loadingSpinner = document.getElementById("loadingSpinner");
  const clearButton = document.getElementById("clearButton");
  let debounceTimer;
  let cache = new Map();
  let allResults = [];
  let currentPage = 1;
  const resultsPerPage = 5;
  let totalResults = 0;
  let highlightedIndex = -1;
  let searchHistory = JSON.parse(localStorage.getItem("searchHistory")) || [];

  searchInput.addEventListener("input", function () {
    clearTimeout(debounceTimer);
    const query = searchInput.value.trim().toLowerCase();

    if (query.length > 0) {
      clearButton.style.display = "block";
      debounceTimer = setTimeout(() => {
        if (cache.has(query)) {
          allResults = cache.get(query);
          totalResults = allResults.length;
          displayResults(allResults.slice(0, resultsPerPage), query);
          if (totalResults > resultsPerPage) {
            const showAll = document.createElement("li");
            showAll.className = "list-group-item show-all";
            showAll.textContent = `Show all ${totalResults} results`;
            showAll.onclick = () => displayResults(allResults, query);
            resultsList.appendChild(showAll);
          }
        } else {
          currentPage = 1;
          fetchResults(query);
        }
      }, 500);
    } else {
      clearSearch();
    }
  });

  clearButton.addEventListener("click", clearSearch);

  searchInput.addEventListener("keydown", function (event) {
    const items = resultsList.querySelectorAll(".list-group-item");
    if (event.key === "ArrowDown") {
      highlightedIndex = (highlightedIndex + 1) % items.length;
      updateHighlight(items);
    } else if (event.key === "ArrowUp") {
      highlightedIndex = (highlightedIndex - 1 + items.length) % items.length;
      updateHighlight(items);
    } else if (event.key === "Enter" && highlightedIndex !== -1) {
      items[highlightedIndex].click();
    }
  });

  function fetchResults(query) {
    loadingSpinner.style.display = "block";
    const scheme = window.location.protocol; // e.g., 'http:' or 'https:'
    const host = window.location.host;
    fetch(`/bloxy/api/search?query=${query}`)
      .then((response) => response.json())
      .then((data) => {
        resultsList.innerHTML = "";
        loadingSpinner.style.display = "none";
        allResults = data.results || [];
        totalResults = allResults.length;
        cache.set(query, allResults);
        displayResults(allResults.slice(0, resultsPerPage), query);
        if (totalResults > resultsPerPage) {
          const showAll = document.createElement("li");
          showAll.className = "list-group-item show-all";
          showAll.textContent = `Show all ${totalResults} results`;
          showAll.onclick = () => displayResults(allResults, query);
          resultsList.appendChild(showAll);
        }
        resultsList.style.display = "block";
      })
      .catch((error) => {
        console.error("Error fetching search results:", error);
        loadingSpinner.style.display = "none";
        const errorMessage = document.createElement("li");
        errorMessage.className = "list-group-item error-message";
        errorMessage.textContent =
          "Error fetching search results. Please try again later.";
        resultsList.appendChild(errorMessage);
      });
  }

  function displayResults(results, query) {
    resultsList.innerHTML = "";
    if (results.length === 0) {
      const noResults = document.createElement("li");
      noResults.className = "list-group-item no-results";
      noResults.textContent = "No results found";
      resultsList.appendChild(noResults);
      return;
    }
    appendResults(results);
    const resultCount = document.createElement("li");
    resultCount.className = "list-group-item no-results";
    resultCount.textContent = `Found ${totalResults} results`;
    resultsList.appendChild(resultCount);
    if (totalResults > resultsPerPage) {
      const loadMore = document.createElement("li");
      loadMore.className = "list-group-item load-more";
      loadMore.textContent = "Load more results";
      loadMore.onclick = () => {
        currentPage++;
        appendResults(
          allResults.slice(
            (currentPage - 1) * resultsPerPage,
            currentPage * resultsPerPage
          )
        );
        if (currentPage * resultsPerPage >= totalResults) {
          loadMore.style.display = "none";
        }
      };
      resultsList.appendChild(loadMore);
    }
  }

  function appendResults(results) {
    results.forEach((result) => {
      const li = document.createElement("li");
      li.className = "list-group-item";
      li.onclick = () => (window.location.href = result.url);

      const img = document.createElement("img");
      img.src = result.urlToImage;
      img.alt = result.title;

      const content = document.createElement("div");
      const title = document.createElement("span");
      title.innerHTML = highlightTerm(result.title, searchInput.value);

      content.appendChild(title);
      li.appendChild(img);
      li.appendChild(content);
      resultsList.appendChild(li);
    });
  }

  function highlightTerm(text, term) {
    const regex = new RegExp(`(${term})`, "gi");
    return text.replace(regex, '<span class="highlight">$1</span>');
  }

  function clearSearch() {
    searchInput.value = "";
    resultsList.innerHTML = "";
    resultsList.style.display = "none";
    clearButton.style.display = "none";
    highlightedIndex = -1;
  }

  function updateHighlight(items) {
    items.forEach((item, index) => {
      item.classList.toggle("active", index === highlightedIndex);
    });
  }
});
