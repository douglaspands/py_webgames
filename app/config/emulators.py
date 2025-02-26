from app.resource import Emulator

EMULATORS: list[Emulator] = [
    {
        "name": "nes",
        "description": "Nintendo - Nintendo Entertainment System",
        "root": "Nintendo - Nintendo Entertainment System (Headered)",
    },
    {
        "name": "snes",
        "description": "Nintendo - Super Nintendo Entertainment System",
        "root": "Nintendo - Super Nintendo Entertainment System",
    },
    {
        "name": "gba",
        "description": "Nintendo - Game Boy",
        "root": "Nintendo - Game Boy",
    },
    {
        "name": "gba",
        "description": "Nintendo - Game Boy Color",
        "root": "Nintendo - Game Boy Color",
    },
    {
        "name": "gba",
        "description": "Nintendo - Game Boy Advance",
        "root": "Nintendo - Game Boy Advance",
    },
    {
        "name": "sega32x",
        "description": "Sega - Master System - Mark III",
        "root": "Sega - Master System - Mark III",
    },
    {
        "name": "sega32x",
        "description": "Sega - Mega Drive - Genesis",
        "root": "Sega - Mega Drive - Genesis",
    },
    {"name": "sega32x", "description": "Sega - 32X", "root": "Sega - 32X"},
    {
        "name": "mednafen_pce",
        "description": "NEC - PC Engine - TurboGrafx-16",
        "root": "NEC - PC Engine - TurboGrafx-16",
    },
    {"name": "atari2600", "description": "Atari - 2600", "root": "Atari - 2600"},
    {
        "name": "n64",
        "description": "Nintendo - Nintendo 64",
        "root": "Nintendo - Nintendo 64 (ByteSwapped)",
    },
    # {
    #     "name": "psx",
    #     "description": "Sony - PlayStation",
    #     "root": "Sony - PlayStation (PS one Classics) (PSN)",
    #     "bios_url": "https://myrient.erista.me/files/Redump/Sony%20-%20PlayStation%20-%20BIOS%20Images/ps-41a.zip",
    # },
]
