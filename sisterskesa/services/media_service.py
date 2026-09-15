from base64 import b64encode
from pathlib import Path
import mimetypes
import streamlit as st
from data.media_manifest import MEDIA

ROOT = Path(__file__).resolve().parents[1]

@st.cache_data
def _data_url(path: str, modified: float) -> str:
    file = Path(path)
    mime = mimetypes.guess_type(file.name)[0] or "image/webp"
    return f"data:{mime};base64,{b64encode(file.read_bytes()).decode()}"

def get_media(asset_id: str) -> str:
    asset = MEDIA.get(asset_id, {})
    local = ROOT / asset.get("local_path", "assets/placeholders/image.svg")
    for file in (local.with_suffix(".webp"), local):
        if file.is_file() and file.resolve().is_relative_to(ROOT):
            return _data_url(str(file), file.stat().st_mtime)
    if asset.get("fallback_url", "").startswith("https://"):
        return asset["fallback_url"]
    placeholder = ROOT / "assets/placeholders/image.svg"
    return _data_url(str(placeholder), placeholder.stat().st_mtime)

def media_alt(asset_id: str) -> str:
    return MEDIA.get(asset_id, {}).get("alt", "sisterskesa — image unavailable")
