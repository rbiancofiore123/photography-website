const links = document.querySelectorAll('.nav-link');

function setActiveLink() {
    const fromTop = window.scrollY + 120;
    links.forEach((link) => {
        const section = document.querySelector(link.getAttribute('href'));
        if (!section) return;
        const top = section.offsetTop;
        const bottom = top + section.offsetHeight;
        link.classList.toggle('active', fromTop >= top && fromTop < bottom);
    });
}

links.forEach((link) => {
    link.addEventListener('click', (event) => {
        event.preventDefault();
        const target = document.querySelector(link.getAttribute('href'));
        if (target) {
            window.scrollTo({ top: target.offsetTop - 80, behavior: 'smooth' });
        }
    });
});

setActiveLink();
window.addEventListener('scroll', setActiveLink);

const year = new Date().getFullYear();
const yearSpan = document.getElementById('current-year');
if (yearSpan) {
    yearSpan.textContent = year;
}
