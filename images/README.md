# Images Directory

This directory contains all image assets for the photography portfolio website.

## Structure

- **`hero/`** - Hero section images (main landing page visuals)
- **`portfolio/`** - Portfolio gallery images organized by project
- **`about/`** - About section images (photographer portrait, studio shots, etc.)

## Image Guidelines

### File Formats
- Use **WebP** format for modern browsers with JPEG/PNG fallbacks
- Use **JPEG** for photographs (quality 85-90%)
- Use **PNG** for images requiring transparency
- Use **SVG** for icons and logos

### Image Optimization
- Hero images: max 1920px width, optimized for web
- Portfolio thumbnails: 600x450px (4:3 ratio)
- Portfolio full-size: max 2400px width
- About section: max 1200px width

### Naming Conventions
- Use descriptive, lowercase names with hyphens
- Examples: `hero-golden-hour.jpg`, `portfolio-wedding-dolomites.jpg`
- Include dimensions if multiple versions exist: `hero-main-1920w.jpg`, `hero-main-768w.jpg`

## Placeholder Images

Currently using empty `src=""` attributes. Replace with actual image paths:

```html
<!-- Example -->
<img src="images/hero/golden-hour-couple.jpg" alt="Description" />
<img src="images/portfolio/wedding-dolomites.jpg" alt="Description" />
```

## Responsive Images

Consider using `<picture>` elements or `srcset` for responsive images:

```html
<img 
  src="images/hero/main.jpg"
  srcset="images/hero/main-768w.jpg 768w,
          images/hero/main-1200w.jpg 1200w,
          images/hero/main-1920w.jpg 1920w"
  sizes="100vw"
  alt="Description" />
```
