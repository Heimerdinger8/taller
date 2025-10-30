document.addEventListener('DOMContentLoaded', () => {
    const toggleButton = document.getElementById('darkModeToggle');
    const darkModeIcon = document.getElementById('darkModeIcon');
    const body = document.body;

    // Check for user's preferred mode in localStorage or system preference
    const savedTheme = localStorage.getItem('theme');
    const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;

    if (savedTheme === 'dark' || (savedTheme === null && prefersDark)) {
        body.classList.add('dark-mode');
        darkModeIcon.src = '/static/img/luna.png'; // Assuming Django static URL
        darkModeIcon.alt = 'Modo Claro';
        console.log('Dark mode applied on load.');
    } else {
        body.classList.remove('dark-mode');
        darkModeIcon.src = '/static/img/sol.png'; // Assuming Django static URL
        darkModeIcon.alt = 'Modo Oscuro';
        console.log('Light mode applied on load.');
    }

    toggleButton.addEventListener('click', () => {
        body.classList.toggle('dark-mode');
        if (body.classList.contains('dark-mode')) {
            darkModeIcon.src = '/static/img/luna.png'; // Assuming Django static URL
            darkModeIcon.alt = 'Modo Claro';
            localStorage.setItem('theme', 'dark');
            console.log('Dark mode activated by toggle.');
        } else {
            darkModeIcon.src = '/static/img/sol.png'; // Assuming Django static URL
            darkModeIcon.alt = 'Modo Oscuro';
            localStorage.setItem('theme', 'light');
            console.log('Light mode activated by toggle.');
        }
    });
});