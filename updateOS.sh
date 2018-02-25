#!/bin/bash

#   FREEproject OS Git Helper
#   The Git push/pull helper for FREEproject OS.
#
#   Contributors are shown at https://freeproject-oss.github.io/contributors.html
#
#   (C) FREEproject Open Source Systems and contributors 2018.

echo "NOTICE: THIS WILL DESTROY ALL UNPUSHED FILES!"
echo "Press Enter to continue."
read enter

git fetch
git checkout master
git pull
git reset --hard

echo "Branch master pulled. Installing dependencies."

sudo bash installDeps.sh

echo "Dependencies installed. Updating local files."

sudo cp -rfT apps/ /home/pi/.apps/
sudo cp -rfT system/ /home/pi/.system/

echo "FREEproject OS is updated to newest development build."
