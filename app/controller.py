import urllib.parse

from flask import Blueprint, render_template, request

from app import service

app = Blueprint("main", __name__)


@app.route("/", methods=["GET"])
def index():
    emulators = service.get_emulators()
    return render_template("index.html", context={"emulators": emulators})


@app.route("/game", methods=["POST", "GET"])
def game():
    payload = dict(request.form)
    context = {}
    context["emulator"] = (emu_system := payload["emulator"].split("|"))[0]
    context["console"] = emu_system[1]
    context["rom_url"] = urllib.parse.unquote(payload.pop("rom", None))
    context["rom_b64"] = service.get_b64_rom(context["rom_url"])
    context["rom_name"] = (context["rom_url"].split("/")[-1]).split(".")[0]
    context["bios"] = ""
    return render_template("game.html", context=context)
