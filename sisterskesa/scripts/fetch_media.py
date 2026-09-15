"""Download configured photos once, resize, and store WebP. Never runs at app startup."""
import io
import json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import requests
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]

def fetch(entry):
    target = ROOT / entry["local_path"]
    if target.exists():
        return f"exists {entry['id']}"
    response = requests.get(entry["fallback_url"], timeout=45)
    response.raise_for_status()
    with Image.open(io.BytesIO(response.content)) as raw:
        picture = ImageOps.exif_transpose(raw).convert("RGB")
        picture.thumbnail((1800, 1800) if entry["category"] == "hero" else (1200, 1400))
        target.parent.mkdir(parents=True, exist_ok=True)
        picture.save(target, "WEBP", quality=84, method=6)
    return f"saved {entry['id']} ({target.stat().st_size//1024} KB)"

if __name__ == "__main__":
    manifest = json.loads((ROOT/"data/media.json").read_text(encoding="utf-8"))
    with ThreadPoolExecutor(max_workers=6) as pool:
        for result in pool.map(fetch, manifest.values()):
            print(result, flush=True)
