import os

def fix_css():
    filepath = r'f:\Portfolio Website\style.css'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    tablet_section = """/* TABLET_FIX */
@media (max-width: 768px) {
    header { padding: 0.8rem 0; }
    nav { flex-direction: row; justify-content: space-between; }
    .nav-links { gap: 1rem; }
    .nav-links a { font-size: 0.75rem; letter-spacing: 0.5px; }
    .nav-logo { height: 45px; width: 45px; }
    section { padding: 60px 0; }
    .hero-title { font-size: 3.2rem; }
    .hero-subtitle { font-size: 1rem; }
    .about-grid, .racing-grid { grid-template-columns: 1fr; text-align: center; }
    .about-image, .racing-image { max-width: 500px; margin: 0 auto; }
    .about-text, .racing-content { padding: 2.5rem 0; }
    .tech-grid { grid-template-columns: 1fr; max-width: 500px; }
    .tech-card { height: auto; min-height: 400px; }
    .links-grid { grid-template-columns: repeat(3, 1fr); gap: 1rem; }
    .tech-card.from-left, .social-card.from-left { transform: translateX(-20px); }
    .tech-card.from-right, .social-card.from-right { transform: translateX(20px); }
}
"""

    mobile_section = """/* MOBILE_FIX */
@media (max-width: 480px) {
    header { padding: 0.5rem 0; }
    .nav-logo { height: 35px; width: 35px; }
    .nav-links { gap: 0.6rem; }
    .nav-links a { font-size: 0.6rem; font-weight: 700; }
    .hero-title { font-size: 2.1rem; letter-spacing: -1px; line-height: 1.2; }
    .hero-subtitle { font-size: 0.85rem; margin-bottom: 2rem; }
    .btn { padding: 0.7rem 1.2rem; font-size: 0.8rem; width: auto !important; }
    .btn-secondary { margin-left: 0.3rem; }
    .section-title { font-size: 1.7rem; margin-bottom: 2rem; }
    .skill-pill { padding: 0.4rem 1rem; font-size: 0.75rem; }
    .glass { padding: 1.2rem !important; }
    .glass h2, .glass h3 { font-size: 1.15rem; }
    .contact-item { font-size: 0.85rem; gap: 0.4rem; }
    .contact-item i { font-size: 1.1rem; }
    .links-grid { grid-template-columns: 1fr 1fr; }
    video { pointer-events: none; }
    .tech-card.from-left, .social-card.from-left { transform: translateX(-15px); }
    .tech-card.from-right, .social-card.from-right { transform: translateX(15px); }
}

/* Tiny Mobile (340px) */
@media (max-width: 340px) {
    .nav-links { gap: 0.4rem; }
    .nav-links a { font-size: 0.55rem; }
    .hero-title { font-size: 1.6rem; }
}
"""
    
    # Simple split and rebuild
    head = content.split('/* TABLET_FIX */')[0]
    
    new_content = head + tablet_section + mobile_section
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

if __name__ == "__main__":
    fix_css()
