"""
    FREEproject OS API
    The API for FREEproject OS.

    Contributors are shown at https://freeproject-oss.github.io/contributors.html

    (C) FREEproject Open Source Systems and contributors 2018.
"""

import os

colours = {
    "background": {
        "black": "\e[40m",
        "white": "\e[107m",
        "red": "\e[41m",
        "green": "\e[42m",
        "yellow": "\e[43m",
        "blue": "\e[44m",
        "magenta": "\e[45m",
        "cyan": "\e[46m",
        "lgrey": "\e[47m",
        "dgrey": "\e[100m",
        "lred": "\e[101m",
        "lgreen": "\e[102m",
        "lyellow": "\e[103m",
        "lblue": "\e[104m",
        "lmagenta": "\e[105m",
        "lcyan": "\e[106m"
    },
    "foreground": {
        "black": "\e[30m",
        "white": "\e[97m",
        "red": "\e[31m",
        "green": "\e[32m",
        "yellow": "\e[33m",
        "blue": "\e[34m",
        "magenta": "\e[35m",
        "cyan": "\e[36m",
        "lgrey": "\e[37m",
        "dgrey": "\e[90m",
        "lred": "\e[91m",
        "lgreen": "\e[92m",
        "lyellow": "\e[93m",
        "lblue": "\e[94m",
        "lmagenta": "\e[95m",
        "lcyan": "\e[96m"
    }
}

bgcolour = "black"
fgcolour = "white"

def shexec(command):
    os.system(command)
    
def pyexec(pyfile, sudo = False, python3 = True):
	if python3:
		if sudo: os.system("sudo python3 " + pyfile)
		else: os.system("python3 " + pyfile)
	else:
		if sudo: os.system("sudo python " + pyfile)
		else: os.system("python " + pyfile)

def echo(text):
    shexec("bash -c 'echo -e \"" + colours["background"][bgcolour] + colours["foreground"][fgcolour] + text.replace("'", "\\x27").replace('"', '\\"') + '"\'')

def prompt(text = ""):
	return input(text)

def clear(bg = bgcolour, fg = fgcolour):
	global bgcolour, fgcolour
	bgcolour = bg
	fgcolour = fg
	
	echo(colour("", bg = bgcolour, fg = fgcolour, revert = False))
	shexec("clear")

def goto(x, y):
	# Size of terminal screen (1-indexed) is x: 80 y: 31 (suggested 30 for no newline).
	shexec("tput cup " + str(y) + " " + str(x))
	
def mouse():
	shexec("sudo sh ~/.apps/api/getmouse.sh")
	output = open("/home/pi/.temp/getmouse", "r")
	outputRead = output.read()
	return [int(int(outputRead.split()[0]) / 7.94), int(int(outputRead.split()[1]) / 15)]
	
def key():
	shexec("sudo bash ~/.apps/api/getkey.sh")
	output = open("/home/pi/.temp/getkey", "r")
	outputRead = output.read()
	
	if outputRead.split() == []:
		return " "
	else:
		return outputRead.split()[0]
		
def keytimeout(time = 3, default = " "):
	if time <= 0: raise ValueError("Length of timeout cannot be less than 1")
	
	while time != 0:
		shexec("sudo bash ~/.apps/api/getkeytimeout.sh")
		output = open("/home/pi/.temp/getkeytimeout", "r")
		outputRead = output.read()
		
		if outputRead.split() != []:
			time = 0
		else:
			time -= 1
	
	if outputRead.split() == []:
		return default
	else:
		return outputRead.split()[0]

def colour(text, bg = bgcolour, fg = fgcolour, revert = True):
	if revert:
		return colours["background"][bg] + colours["foreground"][fg] + text + colours["background"][bgcolour] + colours["foreground"][fgcolour]
	else:
		return colours["background"][bg] + colours["foreground"][fg] + text

def init():
	pass

