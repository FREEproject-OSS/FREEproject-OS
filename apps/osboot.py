"""
    FREEproject OS Boot Sequence
    The boot sequence for FREEproject OS.

    Contributors are shown at https://freeproject-oss.github.io/contributors.html

    (C) FREEproject Open Source Systems and contributors 2018.
"""

from term import *
import ui

clear(bg = "white", fg = "black")

echo("")
echo("")
echo("")
echo("")

echo("                                 " + colour("            ", bg = "lblue").replace("*", colour(" ", bg = "black") + colour("", bg = "lblue", revert = False)))
echo("                             " + colour("                    ", bg = "lblue").replace("*", colour(" ", bg = "black") + colour("", bg = "lblue", revert = False)))
echo("                           " + colour("                        ", bg = "lblue").replace("*", colour(" ", bg = "black") + colour("", bg = "lblue", revert = False)))
echo("                          " + colour("     *******              ", bg = "lblue").replace("*", colour(" ", bg = "black") + colour("", bg = "lblue", revert = False)))
echo("                         " + colour("      *******  * *****      ", bg = "lblue").replace("*", colour(" ", bg = "black") + colour("", bg = "lblue", revert = False)))
echo("                         " + colour("      **       **     *     ", bg = "lblue").replace("*", colour(" ", bg = "black") + colour("", bg = "lblue", revert = False)))
echo("                        " + colour("       **       *      *      ", bg = "lblue").replace("*", colour(" ", bg = "black") + colour("", bg = "lblue", revert = False)))
echo("                        " + colour("       *****    *      *      ", bg = "lblue").replace("*", colour(" ", bg = "black") + colour("", bg = "lblue", revert = False)))
echo("                        " + colour("       *****    *******       ", bg = "lblue").replace("*", colour(" ", bg = "black") + colour("", bg = "lblue", revert = False)))
echo("                        " + colour("       **       *             ", bg = "lblue").replace("*", colour(" ", bg = "black") + colour("", bg = "lblue", revert = False)))
echo("                         " + colour("      **       *            ", bg = "lblue").replace("*", colour(" ", bg = "black") + colour("", bg = "lblue", revert = False)))
echo("                         " + colour("               *            ", bg = "lblue").replace("*", colour(" ", bg = "black") + colour("", bg = "lblue", revert = False)))
echo("                          " + colour("              *           ", bg = "lblue").replace("*", colour(" ", bg = "black") + colour("", bg = "lblue", revert = False)))
echo("                           " + colour("                        ", bg = "lblue").replace("*", colour(" ", bg = "black") + colour("", bg = "lblue", revert = False)))
echo("                             " + colour("                    ", bg = "lblue").replace("*", colour(" ", bg = "black") + colour("", bg = "lblue", revert = False)))
echo("                                 " + colour("            ", bg = "lblue").replace("*", colour(" ", bg = "black") + colour("", bg = "lblue", revert = False)))

echo("")
echo(" Booted FREEproject OS.")

echo(" Build: Development.")
echo(" Would you like to open Bash or go to Login? " + colour("[b/L] after 3 seconds", bg = "white", fg = "dgrey"))

login = keytimeout(time = 3, default = "l")

if login == "l" or login == "L":
	pyexec("/home/pi/.apps/login.py")
else:
	shexec("lxterminal")
