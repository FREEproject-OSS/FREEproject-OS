#!/bin/bash

#   FREEproject OS Git Helper
#   The Git push/pull helper for FREEproject OS.
#
#   Contributors are shown at https://freeproject-oss.github.io/contributors.html
#
#   (C) FREEproject Open Source Systems and contributors 2018.

echo "Enter what you've changed (commit message):"
read commit

echo "Enter what branch you want to push to:"
read branch

sudo cp -rfT /home/pi/.apps apps/
sudo cp -rfT /home/pi/.system system/

git add --all
git commit -m "$commit"

git stash
git pull
git stash pop

echo "About to push, please login:"
git push origin $branch

echo "Git push completed."
echo "Don't forget to create a pull request if on another branch!"
