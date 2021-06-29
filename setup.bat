@echo off

title Setup (0/2 packages installed)

echo Installing packages...

python -m pip install --upgrade pip

title Setup (1/2 packages installed)

pip install discord_webhook

title Setup (2/2 packages installed)

echo Installed all packages!

@pause
