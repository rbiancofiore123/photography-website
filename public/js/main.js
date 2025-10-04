'use strict';

const links = document.querySelectorAll('.nav-link');
const sections = document.querySelectorAll('main section[id]');

function updateActiveLink(activeId) {
    links.forEach((link) => {
        const href = link.getAttribute('href');
        const isActive = href === `#${activeId}`;
        link.classList.toggle('active', isActive);
        if (isActive) {
            link.setAttribute('aria-current', 'page');
        } else {
            link.removeAttribute('aria-current');
        }
    });
}

if ('IntersectionObserver' in window && sections.length > 0) {
    const observer = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    updateActiveLink(entry.target.id);
                }
            });
        },
        {
            rootMargin: '-40% 0px -50% 0px',
            threshold: 0.1,
        },
    );

    sections.forEach((section) => observer.observe(section));
} else {
    const setActiveLink = () => {
        const fromTop = window.scrollY + 120;
        sections.forEach((section) => {
            const top = section.offsetTop;
            const bottom = top + section.offsetHeight;
            if (fromTop >= top && fromTop < bottom) {
                updateActiveLink(section.id);
            }
        });
    };

    setActiveLink();
    window.addEventListener('scroll', setActiveLink, { passive: true });
}

links.forEach((link) => {
    link.addEventListener('click', (event) => {
        const href = link.getAttribute('href');
        if (!href || !href.startsWith('#')) {
            return;
        }

        const target = document.querySelector(href);
        if (!target) {
            return;
        }

        event.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
});

const year = new Date().getFullYear();
const yearSpan = document.getElementById('current-year');
if (yearSpan) {
    yearSpan.textContent = year;
}
