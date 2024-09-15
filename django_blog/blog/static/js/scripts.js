// static/js/main.js

// Basic example script to demonstrate dynamic behavior
document.addEventListener('DOMContentLoaded', function() {
    console.log('Blog page loaded');
});

document.addEventListener('DOMContentLoaded', () => {
    // Code for interactive navigation menu
    const menuButton = document.querySelector('.menu-button');
    const navMenu = document.querySelector('.nav-menu');
    
    menuButton.addEventListener('click', () => {
        navMenu.classList.toggle('active');
    });
    
    // Code for form validation
    const form = document.querySelector('form');
    
    form.addEventListener('submit', (event) => {
        const inputs = form.querySelectorAll('input[required]');
        let valid = true;
        
        inputs.forEach(input => {
            if (!input.value) {
                valid = false;
                input.classList.add('error');
            } else {
                input.classList.remove('error');
            }
        });
        
        if (!valid) {
            event.preventDefault();
            alert('Please fill out all required fields.');
        }
    });
    
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
});
