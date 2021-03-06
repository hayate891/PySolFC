#!/usr/bin/env python
# -*- mode: python; coding: utf-8; -*-
# ---------------------------------------------------------------------------##
#
# Copyright (C) 1998-2003 Markus Franz Xaver Johannes Oberhumer
# Copyright (C) 2003 Mt. Hood Playing Card Co.
# Copyright (C) 2005-2009 Skomoroh
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# ---------------------------------------------------------------------------##
"""
A number of function that enhance PySol on MacOSX when it used as a normal
GUI application (as opposed to an X11 application).
"""
import sys
from six.moves.tkinter import TclError


def runningAsOSXApp():
    """ Returns True if-and-only-if running from the
    PySol.app bundle on OSX """
    return (sys.platform == 'darwin' and 'PySol.app' in sys.argv[0])


def hideTkConsole(root):
    try:
        root.tk.call('console', 'hide')
    except TclError:
        pass


def setupApp(app):
    """
    Perform setup for the OSX application bundle.
    """
    if not runningAsOSXApp():
        return
    hideTkConsole(app.top)
