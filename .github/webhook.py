import os
import sys
import json


def main():
    release = json.load(sys.stdin)

    repo = os.environ.get("REPO", "")
    tag = os.environ.get("TAG", release.get("tag_name", ""))
    title = f"{repo} {tag}"

    color = 0x9BB6A7

    asset_url = ""
    for a in release.get("assets", []):
        if a.get("name") == "release.zip":
            asset_url = a.get("browser_download_url") or ""
            break

    release_url = release.get("html_url", "")
    if not asset_url:
        asset_url = release_url

    embed = {"title": title, "color": color}

    components = [
        {
            "type": 1,
            "components": [
                {"type": 2, "style": 5, "label": "download", "url": asset_url},
                {"type": 2, "style": 5, "label": "view release", "url": release_url},
            ],
        }
    ]

    payload = {
        "username": "Yuri inspector",
        "avatar_url": "https://cdn.discordapp.com/avatars/1427680032305971300/1fe529c06f7534ce9a30ceacd5c63c08.png?size=1024",
        "embeds": [embed],
        "components": components,
    }
    json.dump(payload, sys.stdout)


if __name__ == "__main__":
    main()
