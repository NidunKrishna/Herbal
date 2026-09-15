# Media guide

All image IDs, paths, source URLs, fallback URLs, alt text and credits live in `data/media.json`. Python views call `get_media("home_hero")` and `media_alt()` through reusable components. Do not scatter image URLs into page code.

## Directory map

| Directory | Content | Recommended preparation |
| --- | --- | --- |
| images/hero | Full-width home hero | 2200×1400+ WebP, considered mobile focal point |
| images/products | Isolated or studio product photographs | 1200×1500 WebP or transparent PNG; consistent crop |
| images/categories | Category reveal photography | 1400×900 WebP; readable when cropped wide |
| images/editorial | Lifestyle features and texture studies | 1800×1200+ WebP |
| images/founders | Approved portraits or illustrative herbal preparation for the founder story | 1400×1800 portrait or suitable landscape |
| images/journal | Article and journal card photography | 1600×1100 WebP |
| images/ingredients | Botanical and ingredient macros | 1200×1200 WebP |
| images/backgrounds | Optional atmospheric backgrounds | Optimize carefully; no assets required yet |
| video/hero | Short muted looping hero video | MP4/WebM; provide still poster; respect reduced motion |
| video/products | Optional product demonstrations | MP4/WebM, subtitles for spoken content |
| video/editorial | Optional editorial films | MP4/WebM with poster and accessible text alternative |
| icons | SVG UI icons and favicon | Simple shapes, currentColor where useful |
| logos | Approved marks and alternate lockups | SVG with accessible naming |
| fonts | Locally licensed font files | WOFF2 plus license documents |
| placeholders | Missing-media fallback | Bundled, local and deliberately neutral |

Video directories are ready for future media. No video players or remote video dependencies are used in this version.

## Replace one image

1. Export your approved photograph as WebP (roughly 80–85 quality).
2. Place it at the matching `local_path`, such as `assets/images/hero/home_hero.webp`, or update that path in the manifest.
3. Update its alt text to describe the actual image. Update photographer, source and rights metadata. Remove or replace the old fallback URL so a missing brand photograph cannot silently display unrelated stock imagery.
4. Save and rerun the app. A changed file modification time invalidates the cached data URL. Restart if the manifest module is still cached.
5. Inspect desktop and phone crops. Adjust `object-position` in the relevant CSS; the home hero uses `.hero-photo`.

A local WebP sibling takes precedence over a configured PNG/JPEG. Remove or update that sibling when replacing formats, otherwise you will continue seeing the older WebP.

## Current stock photography

17 local images are bundled, using credited Pexels photographs. Some IDs reuse the same photograph for separate future replacement. All original source pages, credits and license links appear in `CREDITS.md` and the manifest. Herbal preparation photographs are illustrative and must not be presented as the actual founders, their facilities or production. Product imagery is representative and not proof of actual packaging.

`python scripts/fetch_media.py` is a one-time restoration tool that downloads HTTPS sources, applies EXIF orientation, resizes and writes WebP. It skips files already present. It never runs when the app starts or reruns. The UI uses lazy loading for most non-hero imagery and reserves dimensions to reduce layout movement.

## Fallback behavior

1. Optimized local WebP.
2. Configured local image.
3. Configured HTTPS remote fallback.
4. Local neutral placeholder when no configured local or remote image exists.

The helper does not make a blocking network request to validate a remote URL during rendering. If an external host fails, restore or replace the local file. The delivered app has all configured images locally, so normal operation does not need image-host network access.
