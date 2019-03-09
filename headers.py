import json


def fake_user():
    with open("settings.json") as file:
        path = json.loads(file.read())
        for bypass in path['headers']:
            return bypass
