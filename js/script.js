// Ждем полной загрузки DOM
document.addEventListener('DOMContentLoaded', () => {
    // --- Мобильное меню ---
    const burger = document.querySelector('.burger');
    const navLinks = document.querySelector('.nav-links');
    
    if (burger) {
        burger.addEventListener('click', () => {
            navLinks.classList.toggle('active');
        });
    }

    // Закрыть меню при клике на ссылку
    const links = document.querySelectorAll('.nav-links a');
    links.forEach(link => {
        link.addEventListener('click', () => {
            navLinks.classList.remove('active');
        });
    });

    // Подсветка активной ссылки в навигации
    const currentPath = window.location.pathname.split('/').pop() || 'index.html';
    links.forEach(link => {
        const href = link.getAttribute('href');
        if (href === currentPath || (currentPath === 'index.html' && href === 'index.html')) {
            link.classList.add('active');
        } else if (currentPath === '' && href === 'index.html') {
            link.classList.add('active');
        }
    });

    // --- Обработка отправки контактной формы ---
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Имитация отправки данных (можно заменить на реальный запрос к бэкенду)
            const formData = new FormData(contactForm);
            const data = Object.fromEntries(formData.entries());
            console.log('Form submitted:', data);
            
            // Показываем пользователю сообщение об успехе
            alert('Thank you! Your message has been sent. We will contact you shortly.');
            contactForm.reset();
        });
    }
});
