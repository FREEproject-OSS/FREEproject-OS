#!/bin/bash

#   FREEproject OS Git Helper
#   The Git push/pull helper for FREEproject OS.
#
#   Contributors are shown at https://freeproject-oss.github.io/contributors.html
#
#   (C) FREEproject Open Source Systems and contributors 2018.

echo "Enter your GitHub e-mail."
read email
echo "Enter your GitHub username."
read name

sudo git config user.email $email
sudo git config user.name $name

echo "You are now ready to commit and push. You will be prompted to login on push."
