import os

def fix_css_final():
    filepath = r'f:\Portfolio Website\style.css'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'overflow-x: hidden;' not in content[:500]:
        content = content.replace('body {', 'html, body {\n    overflow-x: hidden;\n    max-width: 100%;\n}\n\nbody {', 1)

    premium_responsiveness = """/* BEGIN PREMIUM RESPONSIVENESS */

/* Tablet & Smaller Desktop (1024px) */
@media (max-width: 1024px) {
    .container { padding: 0 1.5rem; }
    .about-grid, .racing-grid { gap: 2rem; }
    .tech-grid { gap: 2rem; max-width: 900px; }
}

/* TABLET_FIX */
@media (max-width: 768px) {
    header { padding: 0.8rem 0; }
    nav { flex-direction: row; justify-content: space-between; }
    .nav-links { gap: 1rem; }
    .nav-links a { font-size: 0.75rem; letter-spacing: 0.5px; }
    .nav-logo { height: 45px; width: 45px; }
    section { padding: 60px 0; overflow-x: hidden; }
    .hero-title { font-size: 3.2rem; }
    .hero-subtitle { font-size: 1rem; }
    .about-grid, .racing-grid { grid-template-columns: 1fr; text-align: center; }
    .about-image, .racing-image { max-width: 500px; margin: 0 auto; }
    .about-text, .racing-content { padding: 2.5rem 0; }
    .tech-grid { grid-template-columns: 1fr; max-width: 500px; margin: 0 auto; }
    .tech-card { height: auto; min-height: 400px; }
    .links-grid { grid-template-columns: repeat(3, 1fr); gap: 1rem; }
}

/* MOBILE_FIX */
@media (max-width: 480px) {
    header { padding: 0.5rem 0; }
    .container { padding: 0 1rem; }
    .nav-logo { height: 35px; width: 35px; }
    .nav-links { gap: 0.6rem; }
    .nav-links a { font-size: 0.6rem; font-weight: 700; }
    .hero-title { font-size: 2.0rem; letter-spacing: -1px; line-height: 1.2; text-align: center; width: 100%; }
    .hero-subtitle { font-size: 0.8rem; margin: 1rem auto 2rem auto; text-align: center; max-width: 280px; }
    .btn { padding: 0.7rem 1.1rem; font-size: 0.75rem; width: auto !important; display: inline-block; }
    .btn-secondary { margin-left: 0.2rem; }
    .section-title { font-size: 1.6rem; margin-bottom: 2rem; text-align: center; }
    .skill-pill { padding: 0.4rem 0.8rem; font-size: 0.7rem; margin: 0.2rem; }
    .glass { padding: 1rem !important; margin: 0 auto; width: 100%; max-width: 320px; }
    .glass h2, .glass h3 { font-size: 1.1rem; text-align: center; }
    .tech-grid { padding: 1rem 0; gap: 1.5rem; justify-items: center; }
    .tech-link { width: 100%; display: flex; justify-content: center; text-decoration: none; }
    .tech-card { width: 100%; max-width: 320px; margin: 0 auto; }
    .contact-item { font-size: 0.8rem; gap: 0.4rem; justify-content: center; }
    .contact-item i { font-size: 1.0rem; }
    .links-grid { grid-template-columns: 1fr 1fr; width: 100%; max-width: 320px; margin: 0 auto; }
    video { pointer-events: none; }
    
    /* Hard Center Reset for Animations */
    .tech-card, .social-card { 
        transform: translateX(0) !important; 
        opacity: 1 !important; 
        transition: none !important;
        animation: none !important;
    }
}

/* Tiny Mobile (340px) */
@media (max-width: 340px) {
    .nav-links { gap: 0.3rem; }
    .nav-links a { font-size: 0.5rem; }
    .hero-title { font-size: 1.6rem; }
    .btn { padding: 0.6rem 0.9rem; font-size: 0.7rem; }
}"""

    head = content.split('/* BEGIN PREMIUM RESPONSIVENESS */')[0]
    new_content = head + premium_responsiveness
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

if __name__ == "__main__":
    fix_css_final()
