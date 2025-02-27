import base64

import requests
from flask import (
    Blueprint,
    Response,
    jsonify,
    redirect,
    render_template,
    request,
    stream_with_context,
)

from app import service

app = Blueprint("main", __name__)


@app.route("/", methods=["GET"])
def index():
    emulators = service.get_emulators()
    return render_template("index.html", context={"emulators": emulators})


@app.route("/gameplay", methods=["POST"])
def gameplay_redirect():
    payload = dict(request.form)
    return redirect(f"/gameplay/{payload['emulator']}/{payload['rom']}")


@app.route("/gameplay/<console>/<game>", methods=["GET"])
def gameplay(console: str, game: str):
    context = service.gameplay_detail(
        console=console,
        game=game,
    )
    return render_template("gameplay.html", context=context)


@app.route("/roms", methods=["GET"])
def rom_list():
    console = request.args.get("console")
    roms = service.get_roms(console=console)
    return jsonify(roms)


@app.route("/roms/download/<path>", methods=["HEAD", "GET"])
def rom_download(path: str):
    def generate():
        url = base64.b64decode(path).decode("utf-8")
        with requests.Session() as session:
            with session.get(url, stream=True) as res:
                res.raise_for_status()
                for chunk in res.raw.stream():
                    yield chunk

    if request.method == "HEAD":
        return Response(status=200)
    else:
        return stream_with_context(generate())


@app.route("/bios/download/<path>", methods=["HEAD", "GET"])
def bios_download(path: str):
    def generate():
        url = base64.b64decode(path).decode("utf-8")
        with requests.Session() as session:
            with session.get(url, stream=True) as res:
                res.raise_for_status()
                for chunk in res.raw.stream():
                    yield chunk

    if request.method == "HEAD":
        return Response(status=200)
    else:
        return stream_with_context(generate())
