"""
    FREEproject OS API
    The API for FREEproject OS.

    Contributors are shown at https://freeproject-oss.github.io/contributors.html

    (C) FREEproject Open Source Systems and contributors 2018.
"""

import term
import time
import textwrap

colours = term.colours
sensory = []

# Profile Elements	# BG = Background
					# FG = Foreground
					# CB = Control Bar
					# XB = Close Button
probgbg = "white"	# Profile Background BG
probgfg = "black"	# Profile Background FG
prolibg = "blue"	# Profile Login BG
prolifg = "white"	# Profile Login FG
profgbg = "lblue"	# Profile UI Element BG
profgfg = "white"	# Profile UI Element FG
profibg = "lgrey"	# Profile Field Element BG
profifg = "black"	# Profile Field Element FG
prodmbg = "lgrey"	# Profile Dropdown Menu BG
prodmfg = "black"	# Profile Dropdown Menu FG
proscbg = "blue"	# Profile Top Of Screen BG
prosccb = "lblue"	# Profile Top Of Screen CB
proscxb = "lred"	# Profile Top Of Screen XB
proscfg = "white"	# Profile Top Of Screen FG
promgbg = "lgrey"	# Profile Message BG
promgfg = "black"	# Profile Message FG

def screen(title, closeButton = True, clear = True):
	if clear: term.clear(bg = probgbg, fg = probgfg)
	
	term.goto(0, 0)
	term.echo(term.colour(" " * 79, bg = proscbg, fg = proscfg))
	term.goto(0, 0)
	term.echo(term.colour(" " * 5, bg = prosccb, fg = proscfg))
	term.goto(0, 0)
	term.echo(term.colour(time.strftime("%H:%M", time.gmtime()), bg = prosccb, fg = proscfg))
	term.goto(6, 0)
	term.echo(term.colour(title, bg = proscbg, fg = proscfg))
	
	if closeButton:
		term.goto(80, 0)
		term.echo(term.colour("X", bg = proscxb, fg = proscfg))
	
def message(text, title = "Information", mode = "OK", light = False):
	text = text[:580]
	
	wrapper = textwrap.TextWrapper(break_long_words = True, break_on_hyphens = True)
	wrapper.width = 56
	strings = wrapper.wrap(text)
	messageWidth = 0
	
	title = title[:60]
	
	for line in range(0, len(strings)):
		if len(strings[line]) > messageWidth: messageWidth = len(strings[line]) + 2
	
	if len(title) > messageWidth: messageWidth = len(title)
		
	if mode == "OK":
		if messageWidth < 6: messageWidth = 6
	elif mode == "OK+Cancel":
		if messageWidth < 15: messageWidth = 15
	elif mode == "Yes+No" or mode == "No+Yes":
		if messageWidth < 12: messageWidth = 12
	elif mode == "Yes+No+Cancel":
		if messageWidth < 21: messageWidth = 21
	
	term.goto(5, 5)
	if light: term.echo(term.colour(" " * messageWidth, bg = prosccb, fg = proscfg))
	else: term.echo(term.colour(" " * messageWidth, bg = proscbg, fg = proscfg))
	term.goto(5, 5)
	if light: term.echo(term.colour(title, bg = prosccb, fg = proscfg))
	else: term.echo(term.colour(title, bg = proscbg, fg = proscfg))
	term.goto(5, 6)
	term.echo(term.colour(" " * messageWidth, bg = promgbg, fg = promgfg))
	
	for line in range(0, len(strings)):
		term.goto(5, 7 + line)
		term.echo(term.colour(" " * messageWidth, bg = promgbg, fg = promgfg))
		term.goto(6, 7 + line)
		term.echo(term.colour(strings[line], bg = promgbg, fg = promgfg))
		
	term.goto(5, 7 + len(strings))
	term.echo(term.colour(" " * messageWidth, bg = promgbg, fg = promgfg))
	term.goto(5, 8 + len(strings))
	term.echo(term.colour(" " * messageWidth, bg = promgbg, fg = promgfg))
	term.goto(5, 9 + len(strings))
	term.echo(term.colour(" " * messageWidth, bg = promgbg, fg = promgfg))
	term.goto(5, 10 + len(strings))
	term.echo(term.colour(" " * messageWidth, bg = promgbg, fg = promgfg))
	term.goto(5, 11 + len(strings))
	term.echo(term.colour(" " * messageWidth, bg = promgbg, fg = promgfg))
	
	if mode == "OK":
		button("OK", messageWidth, 8 + len(strings), big = True)
	elif mode == "OK+Cancel":
		button("OK", messageWidth, 8 + len(strings), big = True)
		button("Cancel", messageWidth - 9, 8 + len(strings), big = True, bg = proscxb)
	elif mode == "Yes+No":
		button("Yes", messageWidth - 1, 8 + len(strings), big = True)
		button("No", messageWidth - 6, 8 + len(strings), big = True, bg = proscxb)
	elif mode == "No+Yes":
		button("No", messageWidth, 8 + len(strings), big = True)
		button("Yes", messageWidth - 6, 8 + len(strings), big = True, bg = proscxb)
	elif mode == "Yes+No+Cancel":
		button("Yes", messageWidth - 1, 8 + len(strings), big = True)
		button("No", messageWidth - 6, 8 + len(strings), big = True)
		button("Cancel", messageWidth - 15, 8 + len(strings), big = True, bg = proscxb)
		
	senseBtn = -1
	while senseBtn == -1 or senseBtn == -2:
		senseBtn = sense(clear = False)
	
	clearSense()
	return senseBtn
	
def button(text, x, y, big = False, bg = profgbg, fg = profgfg):
	global sensory
	
	if big:
		term.goto(x, y)
		term.echo(term.colour(" " * (len(text) + 2), bg = bg, fg = fg))
		term.goto(x, y + 1)
		term.echo(term.colour(" " + text + " ", bg = bg, fg = fg))
		term.goto(x, y + 2)
		term.echo(term.colour(" " * (len(text) + 2), bg = bg, fg = fg))
		sensory.append([x, y, x + len(text) + 2, y + 2])
	else:
		term.goto(x, y)
		term.echo(term.colour(text, bg = bg, fg = fg))
		sensory.append([x, y, x + len(text), y])
		
def text(text, x, y, bg = probgbg, fg = probgfg):
	term.goto(x, y)
	term.echo(term.colour(text, bg = bg, fg = fg))
	
def textbox(x, y, width = 20, text = "", big = False, bg = profibg, fg = profifg):
	text = text[:width]
	spcwidth = width - len(text)
	text = text + (" " * spcwidth)
	
	button(text, x, y, big = big, bg = bg, fg = fg)

def tbinput(x, y, big = False, bg = profibg, fg = profifg):
	if big: x +=1; y += 1
	
	term.echo(term.colour("", bg = bg, fg = fg, revert = False))
	term.goto(x, y)
	
	return term.prompt()

def sense(clear = True, screen = True):
	global sensory
	mousepos = term.mouse()
	senseitem = -1
	
	for item in range(0, len(sensory)):
		if mousepos[0] >= sensory[item][0] and mousepos[0] <= sensory[item][2] and mousepos[1] >= sensory[item][1] and mousepos[1] <= sensory[item][3]: senseitem = item;
	
	if screen:
		if mousepos[0] == 79 and mousepos[1] == 0:
			senseitem = -2
	
	if clear: sensory = []
	return senseitem
	
def clearSense(): global sensory; sensory = []

term.init()
