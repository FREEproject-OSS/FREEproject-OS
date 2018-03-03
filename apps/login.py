"""
    FREEproject OS Login
    The login program for FREEproject OS.

    Contributors are shown at https://freeproject-oss.github.io/contributors.html

    (C) FREEproject Open Source Systems and contributors 2018.
"""

import term
import ui

button = -1
action = 0

while action == 0:
	while button == -1:
		term.clear(bg = ui.prolibg, fg = ui.prolifg)
		
		term.goto(5, 5); term.echo( "   " + term.colour("          ", bg = "lblue").replace("*", term.colour(" ", bg = "black") + term.colour("", bg = "lblue", revert = False)))
		term.goto(5, 6); term.echo( " " + term.colour("   ***        ", bg = "lblue").replace("*", term.colour(" ", bg = "black") + term.colour("", bg = "lblue", revert = False)))
		term.goto(5, 7); term.echo( " " + term.colour("   ***  ***   ", bg = "lblue").replace("*", term.colour(" ", bg = "black") + term.colour("", bg = "lblue", revert = False)))
		term.goto(5, 8); term.echo(      term.colour("    *    *  *   ", bg = "lblue").replace("*", term.colour(" ", bg = "black") + term.colour("", bg = "lblue", revert = False)))
		term.goto(5, 9); term.echo(      term.colour("    ***  *  *   ", bg = "lblue").replace("*", term.colour(" ", bg = "black") + term.colour("", bg = "lblue", revert = False)))
		term.goto(5, 10); term.echo(     term.colour("    ***  ***    ", bg = "lblue").replace("*", term.colour(" ", bg = "black") + term.colour("", bg = "lblue", revert = False)))
		term.goto(5, 11); term.echo(" " + term.colour("   *    *     ", bg = "lblue").replace("*", term.colour(" ", bg = "black") + term.colour("", bg = "lblue", revert = False)))
		term.goto(5, 12); term.echo(" " + term.colour("        *     ", bg = "lblue").replace("*", term.colour(" ", bg = "black") + term.colour("", bg = "lblue", revert = False)))
		term.goto(5, 13); term.echo("   " + term.colour("          ", bg = "lblue").replace("*", term.colour(" ", bg = "black") + term.colour("", bg = "lblue", revert = False)))
		
		term.goto(23, 6); term.echo( "*** **  *** *** **   **  *   *  *   ** *     *   **".replace("*", term.colour(" ", bg = "white")))
		term.goto(23, 7); term.echo( "*** *** *** *** * * *   * *    * * *   *    * * *".replace("*", term.colour(" ", bg = "white")))
		term.goto(23, 8); term.echo( "*   * * *   *   * * *   * *  * * * *   **   * *  *".replace("*", term.colour(" ", bg = "white")))
		term.goto(23, 9); term.echo( "*** **  *** *** **  *   * *  * **  *   *    * *   *".replace("*", term.colour(" ", bg = "white")))
		term.goto(23, 10); term.echo("*** **  *   *   *   *   * *  * *   *   *    * *   *".replace("*", term.colour(" ", bg = "white")))
		term.goto(23, 11); term.echo("*   * * *** *** *   *    *  *   **  **  *    *  **".replace("*", term.colour(" ", bg = "white")))
		
		ui.button("Login", x = 36, y = 15, big = True)
		ui.button("Power ^", x = 68, y = 28, big = False, bg = ui.proscxb, fg = ui.proscfg)
		button = ui.sense(screen = False)
		
	if button == 0:
		action = 1
	elif button == 1:
		ui.button("Shutdown", x = 67, y = 26, big = False, bg = ui.prodmbg, fg = ui.prodmfg)
		ui.button("Restart ", x = 67, y = 27, big = False, bg = ui.prodmbg, fg = ui.prodmfg)
		
		dmaction = ui.sense(screen = False)
		button = -1
