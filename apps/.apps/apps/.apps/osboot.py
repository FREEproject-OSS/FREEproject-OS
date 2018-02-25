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

echo("           " + colour("            ", bg = "lblue").replace("*", colour(" ", bg = "black") + colour("", bg = "lblue", revert = False)))
echo("       " + colour("                    ", bg = "lblue").replace("*", colour(" ", bg = "black") + colour("", bg = "lblue", revert = False)))
echo("     " + colour("                        ", bg = "lblue").replace("*", colour(" ", bg = "black") + colour("", bg = "lblue", revert = False)))
echo("    " + colour("     *******              ", bg = "lblue").replace("*", colour(" ", bg = "black") + colour("", bg = "lblue", revert = False)))
echo("   " + colour("      *******  * *****      ", bg = "lblue").replace("*", colour(" ", bg = "black") + colour("", bg = "lblue", revert = False)))
echo("   " + colour("      **       **     *     ", bg = "lblue").replace("*", colour(" ", bg = "black") + colour("", bg = "lblue", revert = False)))
echo("  " + colour("       **       *      *      ", bg = "lblue").replace("*", colour(" ", bg = "black") + colour("", bg = "lblue", revert = False)))
echo("  " + colour("       *****    *      *      ", bg = "lblue").replace("*", colour(" ", bg = "black") + colour("", bg = "lblue", revert = False)))
echo("  " + colour("       *****    *******       ", bg = "lblue").replace("*", colour(" ", bg = "black") + colour("", bg = "lblue", revert = False)))
echo("  " + colour("       **       *             ", bg = "lblue").replace("*", colour(" ", bg = "black") + colour("", bg = "lblue", revert = False)))
echo("   " + colour("      **       *            ", bg = "lblue").replace("*", colour(" ", bg = "black") + colour("", bg = "lblue", revert = False)))
echo("   " + colour("               *            ", bg = "lblue").replace("*", colour(" ", bg = "black") + colour("", bg = "lblue", revert = False)))
echo("    " + colour("              *           ", bg = "lblue").replace("*", colour(" ", bg = "black") + colour("", bg = "lblue", revert = False)))
echo("     " + colour("                        ", bg = "lblue").replace("*", colour(" ", bg = "black") + colour("", bg = "lblue", revert = False)))
echo("       " + colour("                    ", bg = "lblue").replace("*", colour(" ", bg = "black") + colour("", bg = "lblue", revert = False)))
echo("           " + colour("            ", bg = "lblue").replace("*", colour(" ", bg = "black") + colour("", bg = "lblue", revert = False)))

echo("")
echo(" Booted FREEproject OS.")

echo("")
echo(" " + colour(" Bash ", bg = "blue") + " " + colour(" Exit ", bg = "red"))

while True:
	mpos = mouse()
	if mpos[0] >= 1 and mpos[0] <= 6 and mpos[1] == 20:
		shexec("lxterminal")
	elif mpos[0] >= 8 and mpos[0] <= 13 and mpos[1] == 20:
		shexec("sudo shutdown -h now")
