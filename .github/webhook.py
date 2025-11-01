import os
import sys
import json

def main():
    release = json.load(sys.stdin)

    repo_env = os.environ.get("REPO", "")
    if "/" in repo_env:
        repo_name = repo_env.split("/")[-1]
    elif repo_env:
        repo_name = repo_env
    else:
        repo_name = release.get("repository", {}).get("name", "")

    tag = os.environ.get("TAG", release.get("tag_name", ""))
    title = f"{repo_name} {tag}".strip()

    color = 0x9BB6A7

    asset_url = ""
    for a in release.get("assets", []):
        if a.get("name") == "release.zip":
            asset_url = a.get("browser_download_url") or ""
            break

    release_url = release.get("html_url", "")
    if not asset_url:
        asset_url = release_url

    embed = {
        "title": title,
        "color": color,
        "description": f"[Download](<{asset_url}>)\n[View Release](<{release_url}>)"
    }

    embed = {
        "username": "Yuri Inspector",
        "avatar_url": "https://cdn.discordapp.com/avatars/1427680032305971300/1fe529c06f7534ce9a30ceacd5c63c08.png?size=1024",
        "embeds": [embed]
    }

    json.dump(embed, sys.stdout)


if __name__ == "__main__":
    main()
