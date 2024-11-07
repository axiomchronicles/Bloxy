document.getElementById('newsletter-form').addEventListener('submit', async function(event) {
    event.preventDefault(); // Prevent the default form submission
    const email = document.getElementById('enteredEmail').value;
    const spinner = document.getElementById('spinner');
    const alert = document.getElementById('alert');
    const newsletterCard = document.getElementById('newsletter-card');

    // Email validation
    if (!validateEmail(email)) {
        showAlert('Invalid email address. Please enter a valid email.', 'danger');
        return;
    }

    // Show spinner
    spinner.style.display = 'block';

    // Hide previous alerts
    alert.style.display = 'none';
    alert.className = '';

    // Prepare the data to be sent
    const data = JSON.stringify({ email: email });

    try {
        const scheme = window.location.protocol; // e.g., 'http:' or 'https:'
        const host = window.location.host;
        const response = await fetch(`/bloxy/api/newsletter`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: data
        });

        spinner.style.display = 'none';
        if (response.ok) {
            // Show success alert
            showAlert('Successfully subscribed to the newsletter!', 'success');

            // Hide the newsletter form
            newsletterCard.style.display = 'none';
        } else {
            const errorData = await response.json();
            throw new Error(errorData.message);
        }
    } catch (error) {
        // Show error alert
        spinner.style.display = 'none';
        showAlert(`Error: ${error.message}`, 'danger');
    }
});

function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(String(email).toLowerCase());
}

function showAlert(message, type) {
    const alert = document.getElementById('alert');
    alert.className = `alert alert-${type}`;
    alert.textContent = message;
    alert.style.display = 'block';
}

function closeNewsletter() {
    document.getElementById('newsletter-card').style.display = 'none';
}
