"""
    FREEproject OS Login
    The login program for FREEproject OS.

    Contributors are shown at https://freeproject-oss.github.io/contributors.html

    (C) FREEproject Open Source Systems and contributors 2018.
"""

import term
import ui
import time

button = -1
action = 0

def loginBack():
	term.clear(bg = ui.prolibg, fg = ui.prolifg)
	
	term.goto(0, 0)
	term.echo(time.strftime("%H:%M ", time.gmtime()) + term.colour(time.strftime("%A %d %B %Y", time.gmtime()), bg = ui.prolibg, fg = "lgrey"))
	
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

while action == 0:
	while button == -1:
		loginBack()
		
		ui.button("Login", x = 36, y = 15, big = True)
		ui.button("Power ^", x = 68, y = 28, big = False, bg = ui.proscxb, fg = ui.proscfg)
		button = ui.sense(screen = False)
		
	if button == 0:
		loginBack()
		
		ui.text("Enter password:", x = 31, y = 15, bg = ui.prolibg, fg = ui.prolifg)
		ui.textbox(x = 28, y = 17, width = 20, big = True)
		passInput = ui.tbinput(x = 28, y = 17, big = True)
		
		loginBack()
		
		ui.text("Enter password:", x = 31, y = 15, bg = ui.prolibg, fg = ui.prolifg)
		ui.textbox(x = 28, y = 17, width = 20, text = "*" * len(passInput), big = True)
		
		if True:	# TODO: Create a password saving file, then add condition
			time.sleep(1)
			ui.message("Incorrect password. Please try again.", title = "Cannot Login", light = True)
		else:
			action = 1
		
		button = -1
	elif button == 1:
		ui.button("Shutdown", x = 67, y = 26, big = False, bg = ui.prodmbg, fg = ui.prodmfg)
		ui.button("Restart ", x = 67, y = 27, big = False, bg = ui.prodmbg, fg = ui.prodmfg)
		
		dmaction = ui.sense(screen = False)
		
		if dmaction == 0:
			term.shexec("sudo shutdown -h now")
		elif dmaction == 1:
			term.shexec("sudo reboot")
		
		button = -1
