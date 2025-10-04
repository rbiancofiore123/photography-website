# Captured Moments Photography Portfolio

A single-page photography portfolio website built with semantic HTML, modern CSS, and a sprinkle of
progressive enhancement for smooth navigation and accessibility. The layout features anchored
sections for Home, About, Portfolio, and Contact, making it easy to showcase work, tell a story, and
invite visitors to inquire.

## Getting Started

1. Clone or download this repository.
2. Open `index.html` in your favorite browser.
3. Customize the copy, images, and colors to reflect your brand.

### Optional local development

Run a quick development server to benefit from live reload and correct relative asset paths:

```bash
python -m http.server --directory .
```

Then open `http://localhost:8000` in your browser.

## Customization Tips

- Replace the Unsplash image URLs with links to your own photography. Remember to keep descriptive
  `alt` text for accessibility.
- Adjust the color palette by editing the CSS custom properties at the top of `public/css/style.css`.
- Update the hero headline, about copy, and portfolio descriptions to match your services.
- Hook the contact form up to your preferred form service by swapping the placeholder `action`
  attribute on the `<form>` element.

## License

This project is provided as-is for personal or commercial portfolio use. Modify it freely to match
your needs.
