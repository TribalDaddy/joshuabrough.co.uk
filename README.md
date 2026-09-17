# Joshua Brough portfolio

Static portfolio website. Deployable files are in `dist/`; the supplied Word CV is preserved in the repository and is not published as a website asset.

## Preview

Run `python -m http.server 4173 --directory dist` and open http://localhost:4173.

## CV

`build_cv.py` creates the two-page downloadable PDF with ReportLab. After content changes, regenerate it and render both pages for visual review.

## Contact form

The form posts to FormSubmit for delivery to Joshuabrough1@outlook.com. CAPTCHA is enabled. The recipient must complete FormSubmit's email activation before delivery can be relied on. Client-side tests intercept the request and do not establish inbox delivery. A production submission and recipient confirmation remain necessary to verify end-to-end delivery.

## Hosting

Sites configuration is in `.openai/hosting.json`. The public asset directory is `dist`. New Sites deployments are owner-private by default; sharing must be changed before the site can be viewed by recruiters or other visitors.

## Validation

Desktop (1440px) and mobile (390px, 320px) layouts were inspected; no horizontal overflow or JavaScript errors. Required fields, invalid email rejection, intercepted form payload, confirmation page, keyboard skip link and PDF response were checked. Both PDF pages were rendered and inspected. Website and PDF text were scanned for prohibited specialist terminology.
