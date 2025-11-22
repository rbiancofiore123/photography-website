# Captured Moments Photography Portfolio

A single-page photography portfolio website built with semantic HTML, modern CSS, and a sprinkle of
progressive enhancement for smooth navigation and accessibility. The layout features anchored
sections for Home, About, Portfolio, and Contact, making it easy to showcase work, tell a story, and
invite visitors to inquire.

## Project Structure

```
photography-website/
├── index.html              # Main HTML file
├── css/
│   └── style.css          # All styles and design tokens
├── js/
│   └── main.js            # Navigation and interactive features
├── images/
│   ├── hero/              # Hero section images
│   ├── portfolio/         # Portfolio gallery images
│   ├── about/             # About section images
│   └── README.md          # Image guidelines and optimization tips
├── AGENTS.md              # Guidelines for AI agents
├── README.md              # This file
└── .gitignore             # Git ignore rules
```

## Getting Started

1. Clone or download this repository.
2. Open `index.html` in your favorite browser.
3. Add your images to the `images/` directory (see `images/README.md` for guidelines).
4. Customize the copy, images, and colors to reflect your brand.

### Local Development

Run a local development server to benefit from live reload and correct relative asset paths:

```bash
python -m http.server
```

Then open `http://localhost:8000` in your browser.

## Customization Tips

- **Images**: Add your photography to the `images/` folder. See `images/README.md` for optimization
  guidelines and naming conventions.
- **Colors**: Adjust the color palette by editing CSS custom properties at the top of `css/style.css`.
- **Content**: Update the hero headline, about copy, and portfolio descriptions in `index.html` to
  match your brand and services.
- **Contact Form**: Hook up the form to your preferred service (Formspree, Netlify Forms, etc.) by
  updating the `action` attribute on the `<form>` element.
- **Navigation**: The site uses smooth scrolling and automatic active link highlighting via
  `js/main.js`.

## License

This project is provided as-is for personal or commercial portfolio use. Modify it freely to match
your needs.
