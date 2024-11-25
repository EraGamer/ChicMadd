import requests
import robloxapi

url = 'https://discordapp.com/api/webhooks/1020875548773326848/y-Q2VRwosW8Tw8kK4nR9qgem7B0tRlMJiN4Xm8CEU3TEEA-nPM7y-UrQmDLapfBAmF79'


def log(HWID, IP, success, content):
    username = "Unknown"
    placeid = "Unknown"
    gameid = "Unknown"
    profile = "Unknown"

    if content.get("userId"):
        username = robloxapi.get_name(content.get("userId"))
        profile = f'https://www.roblox.com/users/{content["userId"]}/profile'

    if content.get("placeId"):
        placeid = content.get("placeId")
    if content.get("gameId"):
        placeid = content.get("gameid")

    object = {
        'content': f'**User**: {username}\n**Profile**: {profile}\n**Place ID**: {placeid}\n**Game ID**: {gameid}\n**Success**: {success}\n**HWID**: {HWID}\n||**IP**: {IP}||\n',
        'username': username,
        'avatar_url': f'https://www.roblox.com/headshot-thumbnail/image?user?Id={content["userId"]}&width=420&height=420&format=png',
    }

    requests.post(url, data=object)
