from typing import Any, TypedDict


class Emulator(TypedDict, total=False):
    name: str
    description: str
    root: str
    bios_url: str
    threads: bool


class Rom(TypedDict):
    name: str
    url: str


class Gameplay(TypedDict, total=False):
    emulator: str
    console: str
    rom_name: str
    rom_url: str
    bios_url: str
    threads: bool
    options: dict[str, Any]
