// Dark mode toggle functionality
document.addEventListener('DOMContentLoaded', function() {
    const darkModeToggle = document.getElementById('darkModeToggle');
    const body = document.body;
    
    // Check for saved dark mode preference, default to light mode
    const darkModeEnabled = localStorage.getItem('darkMode') === 'enabled';
    
    // Apply saved preference on load
    if (darkModeEnabled) {
        body.classList.add('dark-mode');
    }
    
    // Toggle dark mode on button click
    darkModeToggle.addEventListener('click', function() {
        body.classList.toggle('dark-mode');
        
        // Save preference to localStorage
        if (body.classList.contains('dark-mode')) {
            localStorage.setItem('darkMode', 'enabled');
        } else {
            localStorage.setItem('darkMode', 'disabled');
        }
    });
});
