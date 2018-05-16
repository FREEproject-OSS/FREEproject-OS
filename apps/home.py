"""
    FREEproject OS Home
    The post-login home screen for FREEproject OS.

    Contributors are shown at https://freeproject-oss.github.io/contributors.html

    (C) FREEproject Open Source Systems and contributors 2018.
"""

import term
import ui

# TODO: Create a Home screen.
ui.screen("Home", closeButton = False)
ui.message("The Home screen is still in development.")

term.pyexec("~/.apps/login.py")
