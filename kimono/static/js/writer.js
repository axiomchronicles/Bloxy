document.addEventListener('DOMContentLoaded', function() {
    const tagInput = document.getElementById('tagInput');
    const tagInputContainer = document.getElementById('tagInputContainer');
    const tagsCount = document.getElementById('tags-count');
    const suggestions = document.getElementById('suggestions');

    const predefinedTags = ['JavaScript', 'HTML', 'CSS', 'React', 'Node.js']; // Example suggestions

    tagInput.addEventListener('keyup', function(event) {
        const tagValue = tagInput.value.trim();
        if (event.key === ' ' || event.key === 'Enter') {
            event.preventDefault();
            if (tagValue && !isTagDuplicate(tagValue)) {
                addTag(tagValue);
                tagInput.value = ''; // Clear input
                updateCharacterCount();
                hideSuggestions();
            }
        } else if (event.key !== 'ArrowUp' && event.key !== 'ArrowDown' && event.key !== 'Enter') {
            showSuggestions(tagValue);
        }
    });

    function addTag(value) {
        const newTag = document.createElement('span');
        newTag.className = 'tag-box';
        newTag.textContent = value;

        const closeButton = document.createElement('span');
        closeButton.className = 'close-btn';
        closeButton.textContent = 'x';
        closeButton.onclick = function() {
            newTag.remove();
            updateCharacterCount();
        };
        newTag.appendChild(closeButton);

        tagInputContainer.insertBefore(newTag, tagInput);
    }

    function isTagDuplicate(value) {
        const existingTags = document.querySelectorAll('#tagInputContainer .tag-box');
        return Array.from(existingTags).some(tag => tag.textContent.replace('x', '').trim() === value);
    }

    function updateCharacterCount() {
        const tags = document.querySelectorAll('#tagInputContainer .tag-box');
        const count = tags.length;
        tagsCount.textContent = `${count}/100`;
    }

    function showSuggestions(value) {
        hideSuggestions();
        if (value) {
            const filteredTags = predefinedTags.filter(tag => tag.toLowerCase().includes(value.toLowerCase()));
            filteredTags.forEach(tag => {
                const suggestionItem = document.createElement('div');
                suggestionItem.className = 'suggestion-item';
                suggestionItem.textContent = tag;
                suggestionItem.onclick = function() {
                    if (!isTagDuplicate(tag)) {
                        addTag(tag);
                        tagInput.value = '';
                        updateCharacterCount();
                        hideSuggestions();
                    }
                };
                suggestions.appendChild(suggestionItem);
            });
            suggestions.style.display = 'block';
        }
    }

    function hideSuggestions() {
        suggestions.innerHTML = '';
        suggestions.style.display = 'none';
    }
});
