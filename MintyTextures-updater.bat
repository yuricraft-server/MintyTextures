@echo off
SETLOCAL ENABLEDELAYEDEXPANSION

SET location=%~dp0

for %%F in ("%location%\MintyTextures*.zip") do (
    DEL "%%F"
)

FOR /f "tokens=1,* delims=:" %%A IN ('curl -ks https://api.github.com/repos/yuricraft-server/MintyTextures/releases/latest ^| findstr "browser_download_url"') DO (
    SET url=%%B
    IF NOT "!url:MintyTextures.zip=!"=="!url!" (
        curl -kOL !url!
    )
)

SET "index=0"
FOR /f "delims=" %%A IN ('curl -ks https://api.github.com/repos/yuricraft-server/MintyTextures/releases/latest ^| findstr "tag_name"') DO (
    IF !index! EQU 0 (
        SET "release_name=%%A"
        SET "release_name=!release_name:*: =!"
        SET "release_name=!release_name: =!"
        SET "release_name=!release_name:~1,-2!"
        set name=!release_name!
    )
    SET /A index+=1
)
:EndLoop

REN "MintyTextures.zip" "MintyTextures-%name%.zip"
echo Finished updating resources
SET /p exit=""