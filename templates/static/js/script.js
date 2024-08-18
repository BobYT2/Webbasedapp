// JavaScript for adding more language options
document.getElementById('add-more').addEventListener('click', function() {
    var container = document.getElementById('language-container');
    var newCheckbox = document.createElement('input');
    newCheckbox.type = 'checkbox';
    newCheckbox.name = 'languages';
    newCheckbox.value = 'new-lang';
    newCheckbox.id = 'new-lang';
    var newLabel = document.createElement('label');
    newLabel.htmlFor = 'new-lang';
    newLabel.textContent = 'New Language';
    
    container.appendChild(newCheckbox);
    container.appendChild(newLabel);
    container.appendChild(document.createElement('br'));
});

// JavaScript to handle network errors
document.getElementById('appForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    // Check for network availability
    if (!navigator.onLine) {
        document.getElementById('error-message').style.display = 'block';
    } else {
        document.getElementById('error-message').style.display = 'none';
        this.submit();
    }
});
