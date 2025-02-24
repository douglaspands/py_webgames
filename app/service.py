import base64
import io

import requests


def _download_rom(url: str) -> io.BytesIO:
    file = io.BytesIO()
    with requests.get(url, stream=True) as res:
        res.raise_for_status()
        for chunk in res.iter_content(chunk_size=8192):
            file.write(chunk)
    file.seek(0)
    return file


def get_b64_rom(url: str) -> str:
    file = _download_rom(url=url)
    return base64.b64encode(file.read()).decode()


def get_emulators() -> list[tuple[str, str]]:
    return [
        ("nes", "Nintendo / Famicom"),
        ("snes", "Super Nintendo / Super Famicom"),
        ("gba", "GameBoy"),
        ("gba", "GameBoy Color"),
        ("gba", "GameBoy Advance"),
        ("sega32x", "Master System / Sega Mark III"),
        ("sega32x", "Mega Drive / Genesis"),
        ("sega32x", "Sega 32X"),
    ]
