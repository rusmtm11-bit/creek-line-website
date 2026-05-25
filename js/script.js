// Мобильное меню
document.addEventListener('DOMContentLoaded', () => {
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

    // Активная ссылка в навигации
    const currentPath = window.location.pathname.split('/').pop() || 'index.html';
    links.forEach(link => {
        const href = link.getAttribute('href');
        if (href === currentPath || (currentPath === 'index.html' && href === 'index.html')) {
            link.classList.add('active');
        } else if (currentPath === '' && href === 'index.html') {
            link.classList.add('active');
        }
    });

    // Обработка отправки контактной формы
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Собираем данные
            const formData = new FormData(contactForm);
            const data = Object.fromEntries(formData.entries());
            
            // Здесь можно добавить отправку данных на ваш email или в CRM
            console.log('Form submitted:', data);
            
            // Показываем уведомление
            alert('Thank you for your message! We will get back to you soon.');
            contactForm.reset();
        });
    }
});
