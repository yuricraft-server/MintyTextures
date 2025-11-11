@echo off

SET location=C:\Users\%USERNAME%\AppData\Roaming\.minecraft\resourcepacks
echo The default resource folder was found at "%location%"

SET /P default="Use default resource folder? (y/n)    "

IF "%default%"=="n" (
    SET /p location="Enter resource folder location        "
)

IF NOT EXIST "%location%" (
    echo Location does not exist
    SET /p exit=""
    EXIT
)

MOVE "%~dp0\MintyTextures.zip" "%location%"
MOVE "%~dp0\MintyTextures-updater.bat" "%location%"
echo Finished installing resources
SET /p exit=""