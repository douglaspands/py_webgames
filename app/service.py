import base64
import json
from functools import cache
from pathlib import Path

import requests
from parsel import Selector

from app.resource import Emulator, Gameplay, Rom

URL_BASE = "https://myrient.erista.me/files/No-Intro"


@cache
def get_emulators() -> list[Emulator]:
    with open("app/config/emulators.json") as f:
        content = json.load(f)
    return sorted(
        content,
        key=lambda x: x["description"],
    )


@cache
def get_emulator(console: str) -> Emulator:
    return [
        emulator for emulator in get_emulators() if emulator["description"] == console
    ][0]


@cache
def get_roms(console: str) -> list[Rom]:
    root = get_emulator(console=console)["root"]
    result: list[Rom] = []
    url_console_base = f"{URL_BASE}/{root}/"
    res = requests.get(url_console_base)
    selector = Selector(text=res.text)
    for idx, rom in enumerate(
        selector.xpath('//*[@id="list"]/tbody/tr/td[1]/a//text()')
    ):
        if idx == 0:
            continue
        file = Path(rom.get())
        if any(
            [
                ignore_word in file.name
                for ignore_word in ["DLC", "Update", "Demo", "Theme"]
            ]
        ):
            continue
        result.append(
            {
                "name": file.name.replace(file.suffix, ""),
                "url": url_console_base + file.name,
            }
        )
    return result


@cache
def get_rom(console: str, game: str) -> Rom:
    emulator = get_emulator(console=console)
    roms = get_roms(console=emulator["description"])
    return [rom for rom in roms if game == rom["name"]][0]


def gameplay_detail(console: str, game: str) -> Gameplay:
    context: Gameplay = {}
    emulator = get_emulator(console=console)
    context["emulator"] = emulator["name"]
    context["console"] = console
    rom = get_rom(console=console, game=game)
    rom_url_b64 = base64.b64encode(rom["url"].encode("utf-8")).decode("utf-8")
    context["rom_url"] = f"/roms/{rom_url_b64}"
    context["rom_name"] = rom["name"]
    context["bios_url"] = ""
    context["threads"] = emulator["threads"]
    return context
