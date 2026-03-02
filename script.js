// Performance Optimized Interactions
// --------------------------------

// 1. Optimized Smooth Scrolling
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

// 2. Throttled Header & Parallax Updates
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

// 3. 3D Tilt with requestAnimationFrame
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
    const rotateX = (y - centerY) / 12; // Softer tilt
    const rotateY = (centerX - x) / 12;
    card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-10px)`;
}

// 4. Smart Visibility Management (Pause inactive videos)
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px'
};

const visibilityObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        // Handle Entrance Animations
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');

            // Play video if it's a section with a video
            const video = entry.target.querySelector('video');
            if (video) video.play();
        } else {
            // Pause video if not in view to save CPU/GPU
            const video = entry.target.querySelector('video');
            if (video) video.pause();
        }
    });
}, observerOptions);

// Observe tech cards & social cards for entrance
document.querySelectorAll('.tech-card, .social-card').forEach(card => {
    visibilityObserver.observe(card);
});

// Observe sections for both fade-in and VIDEO control
document.querySelectorAll('section').forEach(section => {
    visibilityObserver.observe(section);
});

