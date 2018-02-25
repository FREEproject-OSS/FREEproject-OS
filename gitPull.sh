#!/bin/bash

#   FREEproject OS Git Helper
#   The Git push/pull helper for FREEproject OS.
#
#   Contributors are shown at https://freeproject-oss.github.io/contributors.html
#
#   (C) FREEproject Open Source Systems and contributors 2018.

echo "NOTICE: THIS WILL DESTROY ALL UNPUSHED FILES!"
echo "Enter the branch you want to pull from."
read branch

git fetch
git checkout $branch
git reset --hard

echo "Branch pulled."
