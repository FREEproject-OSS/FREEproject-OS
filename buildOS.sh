#!/bin/bash

#   FREEproject OS Builder
#   The OS tidy-upper and builder for FREEproject OS.
#
#   Contributors are shown at https://freeproject-oss.github.io/contributors.html
#
#   (C) FREEproject Open Source Systems and contributors 2018.

echo "NOTICE: THIS WILL CLEAR ANY PREFERENCES!"
echo "Press Enter to continue."
read enter

echo "Resetting git credentials..."

sudo git config user.email ""
sudo git config user.name ""

echo "Clearing bash command history..."

cat /dev/null > /root/.bash_history
cat /dev/null > /home/pi/.bash_history

echo "FREEprojectOS is ready for stable release."
