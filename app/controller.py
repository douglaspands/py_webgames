import base64
import urllib.parse

import requests
from flask import Blueprint, Response, render_template, request

from app import service

app = Blueprint("main", __name__)


@app.route("/", methods=["GET"])
def index():
    emulators = service.get_emulators()
    return render_template("index.html", context={"emulators": emulators})


@app.route("/gameplay", methods=["POST"])
def gameplay():
    payload = dict(request.form)
    context = {}
    context["emulator"] = (emu_system := payload["emulator"].split("|"))[0]
    context["console"] = emu_system[1]
    rom_url = urllib.parse.unquote(payload["rom"])
    rom_url_b64 = base64.b64encode(
        (urllib.parse.unquote(rom_url)).encode("utf-8")
    ).decode("utf-8")
    context["rom_url"] = f"/rom/{rom_url_b64}"
    context["rom_name"] = rom_url.split("/")[-1]
    context["bios"] = ""
    return render_template("gameplay.html", context=context)


@app.route("/rom/<path>", methods=["GET", "HEAD"])
def rom_path(path: str):
    if request.method == "HEAD":
        return Response(status=200)
    else:
        res = requests.get(base64.b64decode(path).decode("utf-8"))
        headers = dict(
            [
                (key, value)
                for key, value in res.raw.headers.items()
                if key.lower()
                not in (
                    "content-encoding",
                    "content-length",
                    "transfer-encoding",
                    "connection",
                )
            ]
        )
        return Response(res.content, res.status_code, headers)
