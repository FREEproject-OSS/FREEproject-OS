#   FREEproject OS API Component
#   The API component for FREEproject OS.
#
#   Contributors are shown at https://freeproject-oss.github.io/contributors.html
#
#   (C) FREEproject Open Source Systems and contributors 2018.

( xinput test-xi2 --root & ) | grep -q "RawButtonPress"
xdotool getmouselocation 2>&1 | sed -rn '${s/x:([0-9]+) y:([0-9]+) .*/\1 \2/p}' > /home/pi/.temp/getmouse
sudo killall xinput
