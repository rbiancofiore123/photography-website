"""Flask application serving a single-page photography portfolio site."""
from __future__ import annotations

from flask import Flask, Response

app = Flask(__name__)


PAGE_HTML = """<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\" />
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />
    <title>Captured Moments &mdash; Photography Portfolio</title>
    <style>
        :root {
            color-scheme: light dark;
            --accent: #ff7a59;
            --accent-dark: #d95c3d;
            --bg: #0f172a;
            --bg-light: #f8fafc;
            --text-dark: #0f172a;
            --text-light: #f8fafc;
            --muted: #64748b;
            --shadow: 0 18px 45px rgba(15, 23, 42, 0.15);
            font-family: "Inter", "Segoe UI", system-ui, -apple-system, sans-serif;
        }

        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            background: linear-gradient(180deg, rgba(15, 23, 42, 0.98), rgba(15, 23, 42, 0.92) 45%, rgba(15, 23, 42, 0.85));
            color: var(--text-light);
        }

        header {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 1rem clamp(2rem, 6vw, 6rem);
            background: rgba(15, 23, 42, 0.85);
            backdrop-filter: blur(12px);
            z-index: 1000;
            box-shadow: 0 2px 24px rgba(15, 23, 42, 0.2);
        }

        .logo {
            font-weight: 700;
            letter-spacing: 0.08em;
            text-transform: uppercase;
        }

        nav ul {
            list-style: none;
            display: flex;
            gap: 1.5rem;
            margin: 0;
            padding: 0;
        }

        nav a {
            color: inherit;
            text-decoration: none;
            font-weight: 500;
            position: relative;
            padding-bottom: 0.25rem;
        }

        nav a::after {
            content: "";
            position: absolute;
            left: 0;
            bottom: 0;
            width: 100%;
            height: 2px;
            background: var(--accent);
            transform: scaleX(0);
            transform-origin: right;
            transition: transform 0.25s ease;
        }

        nav a:hover::after,
        nav a.active::after {
            transform: scaleX(1);
            transform-origin: left;
        }

        main {
            padding-top: 5rem;
        }

        section {
            min-height: 100vh;
            display: grid;
            align-items: center;
            padding: clamp(4rem, 12vw, 8rem) clamp(2rem, 8vw, 8rem);
            gap: 3rem;
        }

        .hero {
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            column-gap: clamp(2rem, 6vw, 5rem);
        }

        .hero h1 {
            font-size: clamp(2.8rem, 6vw, 4.5rem);
            margin-bottom: 1.5rem;
        }

        .hero p {
            line-height: 1.7;
            color: var(--muted);
            margin-bottom: 2rem;
        }

        .cta-group {
            display: flex;
            flex-wrap: wrap;
            gap: 1rem;
        }

        .btn {
            padding: 0.85rem 1.8rem;
            border-radius: 999px;
            font-weight: 600;
            border: none;
            cursor: pointer;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }

        .btn-primary {
            background: linear-gradient(135deg, var(--accent), var(--accent-dark));
            color: white;
            box-shadow: var(--shadow);
        }

        .btn-secondary {
            background: transparent;
            color: var(--text-light);
            border: 1px solid rgba(248, 250, 252, 0.3);
        }

        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 12px 30px rgba(255, 122, 89, 0.35);
        }

        .hero-image {
            position: relative;
            min-height: 320px;
            border-radius: 32px;
            overflow: hidden;
            box-shadow: var(--shadow);
            background: url('https://images.unsplash.com/photo-1524504388940-b1c1722653e1?auto=format&fit=crop&w=1600&q=80') center/cover;
        }

        .about {
            background: var(--bg-light);
            color: var(--text-dark);
            border-radius: clamp(2rem, 6vw, 3rem) clamp(2rem, 6vw, 3rem) 0 0;
        }

        .about h2 {
            font-size: clamp(2.2rem, 5vw, 3.2rem);
            margin: 0 0 1.5rem;
        }

        .about p {
            margin: 0 0 1rem;
            color: #475569;
            line-height: 1.8;
        }

        .highlights {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 1.5rem;
            margin-top: 2.5rem;
        }

        .highlight-card {
            background: white;
            border-radius: 20px;
            padding: 1.8rem;
            box-shadow: 0 16px 35px rgba(15, 23, 42, 0.08);
        }

        .highlight-card h3 {
            margin-top: 0;
            margin-bottom: 0.75rem;
            font-size: 1.15rem;
        }

        .portfolio {
            position: relative;
        }

        .portfolio-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
            gap: 1.5rem;
        }

        .portfolio-card {
            background: rgba(15, 23, 42, 0.75);
            border-radius: 18px;
            overflow: hidden;
            box-shadow: var(--shadow);
            transition: transform 0.25s ease, box-shadow 0.25s ease;
        }

        .portfolio-card:hover {
            transform: translateY(-6px);
            box-shadow: 0 25px 45px rgba(15, 23, 42, 0.3);
        }

        .portfolio-card img {
            width: 100%;
            height: 240px;
            object-fit: cover;
        }

        .portfolio-card div {
            padding: 1.5rem;
        }

        .portfolio-card h3 {
            margin: 0 0 0.5rem;
            font-size: 1.1rem;
        }

        .portfolio-card p {
            margin: 0;
            color: var(--muted);
            line-height: 1.6;
        }

        .contact {
            background: rgba(15, 23, 42, 0.88);
            border-radius: 0 0 clamp(2rem, 6vw, 3rem) clamp(2rem, 6vw, 3rem);
        }

        .contact-wrapper {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 3rem;
        }

        form {
            display: grid;
            gap: 1rem;
        }

        label {
            font-weight: 600;
            letter-spacing: 0.02em;
        }

        input,
        textarea {
            padding: 0.9rem 1.1rem;
            border-radius: 14px;
            border: 1px solid rgba(248, 250, 252, 0.25);
            background: rgba(15, 23, 42, 0.4);
            color: inherit;
        }

        textarea {
            resize: vertical;
            min-height: 140px;
        }

        footer {
            text-align: center;
            padding: 2rem;
            color: rgba(248, 250, 252, 0.6);
            font-size: 0.9rem;
        }

        @media (max-width: 768px) {
            header {
                flex-direction: column;
                gap: 1rem;
            }

            nav ul {
                flex-wrap: wrap;
                justify-content: center;
            }

            section {
                min-height: unset;
            }
        }
    </style>
</head>
<body>
<header>
    <span class=\"logo\">Captured Moments</span>
    <nav>
        <ul>
            <li><a class=\"nav-link\" href=\"#home\">Home</a></li>
            <li><a class=\"nav-link\" href=\"#about\">About</a></li>
            <li><a class=\"nav-link\" href=\"#portfolio\">Portfolio</a></li>
            <li><a class=\"nav-link\" href=\"#contact\">Contact</a></li>
        </ul>
    </nav>
</header>
<main>
    <section id=\"home\" class=\"hero\">
        <div>
            <h1>Photography that celebrates every fleeting moment</h1>
            <p>
                I’m Lena Moore, a traveling photographer dedicated to crafting cinematic imagery that feels
                honest, intimate, and alive. From weddings to editorial portraits, I partner closely with my
                clients to ensure their story is told with empathy and artistry.
            </p>
            <div class=\"cta-group\">
                <a class=\"btn btn-primary\" href=\"#portfolio\">View Portfolio</a>
                <a class=\"btn btn-secondary\" href=\"#contact\">Book a Session</a>
            </div>
        </div>
        <div class=\"hero-image\" role=\"presentation\"></div>
    </section>

    <section id=\"about\" class=\"about\">
        <div>
            <h2>About Me</h2>
            <p>
                Over the past decade I have photographed hundreds of couples, creators, and adventurers across the globe.
                My signature style blends natural light with documentary storytelling, producing imagery that feels
                timeless and full of heart.
            </p>
            <p>
                When I’m not behind the lens, you can find me scouting new locations, planning creative concepts,
                and mentoring emerging photographers who want to refine their craft.
            </p>
            <div class=\"highlights\">
                <article class=\"highlight-card\">
                    <h3>Worldwide Experience</h3>
                    <p>Assignments completed across 17 countries with multi-lingual crews and vendors.</p>
                </article>
                <article class=\"highlight-card\">
                    <h3>Award Winning</h3>
                    <p>Recipient of the 2023 LensCulture Portrait Award and featured in Vogue Italia.</p>
                </article>
                <article class=\"highlight-card\">
                    <h3>Story First</h3>
                    <p>Every session begins with interviews and mood boards to ensure your vision leads the shoot.</p>
                </article>
            </div>
        </div>
    </section>

    <section id=\"portfolio\" class=\"portfolio\">
        <div>
            <h2>Portfolio</h2>
            <p style=\"max-width: 640px; color: var(--muted);\">
                A curated look at client stories&mdash;from luminous destination weddings to editorial portraiture and
                lifestyle campaigns. Each gallery is shot on full-frame digital and 35mm film for layered texture.
            </p>
        </div>
        <div class=\"portfolio-grid\">
            <article class=\"portfolio-card\">
                <img src=\"https://images.unsplash.com/photo-1524504388940-b1c1722653e1?auto=format&fit=crop&w=600&q=80\" alt=\"Couple embracing during golden hour\" />
                <div>
                    <h3>Golden Hour Vows</h3>
                    <p>Destination elopement in the Dolomites, capturing soft, sun-kissed romance.</p>
                </div>
            </article>
            <article class=\"portfolio-card\">
                <img src=\"https://images.unsplash.com/photo-1487412947147-5cebf100ffc2?auto=format&fit=crop&w=600&q=80\" alt=\"Editorial portrait of a model with colorful styling\" />
                <div>
                    <h3>Chromatic Muse</h3>
                    <p>Editorial series for Bloom Magazine exploring bold color stories in fashion.</p>
                </div>
            </article>
            <article class=\"portfolio-card\">
                <img src=\"https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?auto=format&fit=crop&w=600&q=80\" alt=\"Landscape of mountains during sunrise\" />
                <div>
                    <h3>Echoes of Earth</h3>
                    <p>Fine art landscape collection focused on the quiet poetry of remote terrain.</p>
                </div>
            </article>
            <article class=\"portfolio-card\">
                <img src=\"https://images.unsplash.com/photo-1534447677768-be436bb09401?auto=format&fit=crop&w=600&q=80\" alt=\"Family smiling together outdoors\" />
                <div>
                    <h3>Kinship Sessions</h3>
                    <p>Documentary-style family sessions celebrating connection in everyday moments.</p>
                </div>
            </article>
        </div>
    </section>

    <section id=\"contact\" class=\"contact\">
        <div class=\"contact-wrapper\">
            <div>
                <h2>Contact Me</h2>
                <p style=\"color: var(--muted); line-height: 1.8;\">
                    Ready to create something beautiful together? Share your vision, and I’ll be in touch within two
                    business days with availability, location ideas, and tailored packages.
                </p>
                <div style=\"display: grid; gap: 1rem; margin-top: 2rem;\">
                    <span>Email: <a style=\"color: inherit; text-decoration: underline;\" href=\"mailto:hello@capturedmoments.co\">hello@capturedmoments.co</a></span>
                    <span>Phone: <a style=\"color: inherit; text-decoration: none;\" href=\"tel:+13125551234\">+1 (312) 555-1234</a></span>
                    <span>Studio: 902 Aurora Ave, Suite 210, Chicago, IL</span>
                </div>
            </div>
            <form>
                <label for=\"name\">Name</label>
                <input id=\"name\" name=\"name\" type=\"text\" placeholder=\"Your full name\" required />

                <label for=\"email\">Email</label>
                <input id=\"email\" name=\"email\" type=\"email\" placeholder=\"you@example.com\" required />

                <label for=\"message\">How can I help?</label>
                <textarea id=\"message\" name=\"message\" placeholder=\"Share details about your event, project, or desired session.\" required></textarea>

                <button class=\"btn btn-primary\" type=\"submit\">Send Message</button>
            </form>
        </div>
    </section>
</main>
<footer>
    &copy; {year} Captured Moments Photography. All rights reserved.
</footer>
<script>
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
</script>
</body>
</html>
"""


@app.get("/")
def index() -> Response:
    """Return the single-page application markup."""
    return Response(PAGE_HTML.format(year=2024), mimetype="text/html")


if __name__ == "__main__":
    app.run(debug=True)
