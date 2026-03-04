
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const targetId = this.getAttribute('href');
        if (targetId === '#') return;
        e.preventDefault();
        const targetElement = document.querySelector(targetId);
        if (targetElement) {
            targetElement.scrollIntoView({ behavior: 'smooth' });
        }
    });
});

let lastScrollY = window.scrollY;
let ticking = false;

window.addEventListener('scroll', () => {
    lastScrollY = window.scrollY;
    if (!ticking) {
        window.requestAnimationFrame(() => {
            updateHeader(lastScrollY);
            ticking = false;
        });
        ticking = true;
    }
}, { passive: true });

function updateHeader(scrollPos) {
    const header = document.querySelector('header');
    if (scrollPos > 50) {
        header.style.background = 'rgba(10, 10, 12, 0.9)';
        header.style.boxShadow = '0 10px 30px rgba(0, 0, 0, 0.5)';
    } else {
        header.style.background = 'rgba(10, 10, 12, 0.8)';
        header.style.boxShadow = 'none';
    }
}

const cards = document.querySelectorAll('.glass');
const isTouchDevice = 'ontouchstart' in window || navigator.maxTouchPoints > 0;

if (!isTouchDevice) {
    cards.forEach(card => {
        let tiltTicking = false;

        card.addEventListener('mousemove', (e) => {
            if (!tiltTicking) {
                window.requestAnimationFrame(() => {
                    applyTilt(e, card);
                    tiltTicking = false;
                });
                tiltTicking = true;
            }
        });

        card.addEventListener('mouseleave', () => {
            card.style.transform = `perspective(1000px) rotateX(0deg) rotateY(0deg) translateY(0)`;
        });
    });
}

function applyTilt(e, card) {
    const rect = card.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    const centerX = rect.width / 2;
    const centerY = rect.height / 2;
    const rotateX = (y - centerY) / 12; 
    const rotateY = (centerX - x) / 12;
    card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-10px)`;
}

const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px'
};

const visibilityObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {

        if (entry.isIntersecting) {
            entry.target.classList.add('visible');

            const video = entry.target.querySelector('video');
            if (video) video.play();
        } else {
            const video = entry.target.querySelector('video');
            if (video) video.pause();
        }
    });
}, observerOptions);

document.querySelectorAll('.tech-card, .social-card').forEach(card => {
    visibilityObserver.observe(card);
});

document.querySelectorAll('section').forEach(section => {
    visibilityObserver.observe(section);
});

