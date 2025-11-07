document.addEventListener('DOMContentLoaded', () => {
    const darkModeToggle = document.getElementById('darkModeToggle');
    const body = document.body;

    // Check for user's preferred mode in localStorage or system preference
    const savedTheme = localStorage.getItem('theme');
    const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;

    if (savedTheme === 'dark' || (savedTheme === null && prefersDark)) {
        body.classList.add('dark-mode');
        darkModeToggle.checked = true; // Set the switch to checked if dark mode is active
        console.log('Dark mode applied on load.');
    } else {
        body.classList.remove('dark-mode');
        darkModeToggle.checked = false; // Set the switch to unchecked if light mode is active
        console.log('Light mode applied on load.');
    }

    darkModeToggle.addEventListener('change', () => {
        if (darkModeToggle.checked) {
            body.classList.add('dark-mode');
            localStorage.setItem('theme', 'dark');
            console.log('Dark mode activated by toggle.');
        } else {
            body.classList.remove('dark-mode');
            localStorage.setItem('theme', 'light');
            console.log('Light mode activated by toggle.');
        }
    });
});