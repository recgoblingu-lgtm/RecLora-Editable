# RecLora Editable Website

A clean, static, GitHub Pages-ready website starter for **RecLora**. It includes a homepage plus 23 major pages, all using the supplied RecLora logo.

## Edit the site without hunting through HTML

Most changes happen in [`content/site.json`](content/site.json):

- Change the RecLora name, tagline, logo path, and colors under `brand`.
- Change the announcement bar under `announcement`.
- Change navigation labels and links under `navigation`.
- Change homepage feature cards under `featured`.
- Change homepage and News content under `announcements`.
- Change page titles and introductions under `pages`.

The shared layout and styling live in [`assets/app.js`](assets/app.js) and [`assets/site.css`](assets/site.css). Replace the three sample SVG artworks in `assets/` whenever you want different feature images. The supplied logo is [`assets/reclora-logo.png`](assets/reclora-logo.png).

## Pages included

The starter includes Home, Explore, Rooms, Events, Creators, News, About, Contact, Help, Community Guidelines, Safety and Privacy, Downloads, Membership, Creator Studio, Creator Resources, Showcase, Collections, Search, Service Status, Changelog, Press Kit, Partners, Terms of Use, and Accessibility.

## Local preview

From the repository root:

```bash
python3 -m http.server 4173
```

Then open `http://localhost:4173/`. Because the site loads `content/site.json`, use a local server instead of opening the HTML file directly.

## GitHub Pages

This is a static site. Enable **Settings → Pages → Deploy from branch → main → /(root)**. The `.nojekyll` file is included so all assets are served as-is.

## Adding a new page

1. Add a new key under `pages` in `content/site.json`.
2. Add a corresponding HTML file under `pages/` using the same small shell as the existing pages.
3. Add the page to `navigation` if it should appear in the header.

The content is intentionally centralized so announcements, images, colors, and links can be changed without rewriting every page.
