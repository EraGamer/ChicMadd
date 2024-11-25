import checkwhitelist
from flask import Flask, request, jsonify
import getsettings
import json
# import discordlog

app = Flask(__name__)

hwid_list = [
    "Syn-Fingerprint",
    "Exploit-Guid",
    "Proto-User-Identifier",
    "Sentinel-Fingerprint",
    "Krnl-Hwid",
    "Sw-Fingerprint",
    "Flux-Fingerprint",
]


@app.route('/')
def hello_world():
    # instantiate an empty dict
    UserData = {}

    return 'Hello, World!'


@app.route('/api/get', methods=["GET"]
           )  # GET is not secure, you should use POST in production.
def get_data():
    content = request.args

    if content.get('placeId') and content.get('gameId') and content.get('userId'):
        print(content)

        userHwid = False

        for hwid in hwid_list:
            if request.headers.get(hwid):
                userHwid = request.headers.get(hwid)

        if userHwid == False:
            return jsonify({"whitelisted": False})
        else:
            whitelisted = checkwhitelist.get_hwid(userHwid)
            if whitelisted:
                file = open("obfuscated.lua", "rt").read()
                return jsonify({
                    "whitelisted": True,
                    "contents": file,
                    "settings": getsettings.get_settings(userHwid),
                })
                # return jsonify({"whitelisted": True})
            else:
                return jsonify({"whitelisted": False})

    else:
        return jsonify({"whitelisted": False})


@app.route('/api/savesettings', methods=["POST"])
def post_data():
    userHwid = False

    for hwid in hwid_list:
        if request.headers.get(hwid):
            userHwid = request.headers.get(hwid)

    if userHwid == False:
        return jsonify({"success": False})
    else:
        content = request.json
        print(content['settings'])
        getsettings.write_settings({
            userHwid: content["settings"]
        })

        return jsonify({"success": True})


app.run(host='0.0.0.0', port=8080)
