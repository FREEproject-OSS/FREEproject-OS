#!/bin/bash

echo "Enter what you've changed (commit message):"
read commit

echo "Enter what branch you want to push to:"
read branch

sudo cp -rf /home/pi/.apps apps
sudo cp -rf /home/pi/.system system

git add -all
git commit -m "$commit"

echo "About to push, please login:"
git push origin $branch

echo "Git push completed."
echo "Don't forget to create a pull request if on another branch!"
