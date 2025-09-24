# Photography Portfolio Single Page App

A Python-powered single page application that showcases a photographer's story, body of work,
and contact information. The design is built with modern gradients, responsive layouts, and
smooth in-page navigation so visitors can explore the four core sections: Home, About,
Portfolio, and Contact.

## Project Structure

```
photography-website/
├── requirements.txt   # Python dependencies for the web server
└── src/
    └── app.py         # Flask app returning the single-page HTML experience
```

## Getting Started

1. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the development server**
   ```bash
   python src/app.py
   ```
4. **View the site**
   Open your browser to [http://localhost:5000](http://localhost:5000) to explore the single-page
   portfolio.

## Customization Tips

- Replace the Unsplash image URLs in `PAGE_HTML` with links to your own work.
- Adjust the color palette by editing the CSS custom properties located at the top of the
  `<style>` block.
- Update the hero headline, about copy, and portfolio descriptions so they reflect your voice
  and services.
- Hook the contact form up to a backend or service such as Formspree if you want to capture
  submissions.

## License

This project is provided as-is for personal or commercial portfolio use. Modify it freely to
match your needs.
