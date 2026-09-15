"""All external URLs and credits live here. Local assets take precedence."""
import json
from pathlib import Path

MANIFEST_PATH = Path(__file__).with_name("media.json")
MEDIA = json.loads(MANIFEST_PATH.read_text(encoding="utf-8")) if MANIFEST_PATH.exists() else {}
