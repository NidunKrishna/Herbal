from components.ui import e

def badges(labels: tuple[str, ...]) -> str:
    return ''.join(f'<span class="badge">{e(label)}</span>' for label in labels[:2])
