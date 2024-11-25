import json


def get_default():
    return {
        "MagnetRangeSlider": 0.5,
        "MagnetKeybind": "N",
        "JamRangeSlider": 1,
        "TabOutToggle": True,
        "MocrewsAnimsKeybind": "M",
        "JamTackleKeybind": "V",
        "SelfDestructKeybind": "L",
        "StaminaRegenSpeed": 10
    }


def write_settings(data):
    with open('UserData.json', 'w') as f:
        json.dump(data, f)


def get_settings(key):
    f = open('UserData.json')
    data = json.load(f)
    settings = get_default()
    if key in data:
        settings = data[key]

    f.close()
    return settings
