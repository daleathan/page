#! /usr/bin/env python
#
# Support module generated by PAGE version 4.2
# In conjunction with Tcl version 8.6
#    Feb. 12, 2014 08:48:59 PM


import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

def set_Tk_var():
    # These are Tk variables used passed to Tkinter and must be
    # defined before the widgets using them are created.
    global IRS
    IRS = StringVar()

    global Charity
    Charity = StringVar()

    global Check_1
    Check_1 = StringVar()

    global Check_2
    Check_2 = StringVar()


def check1():
        print ('menu_support.check1')
        sys.stdout.flush()

def check2():
        print ('menu_support.check2')
        sys.stdout.flush()

def copy():
        print ('menu_support.copy')
        sys.stdout.flush()

def cut():
        print ('menu_support.cut')
        sys.stdout.flush()

def paste():
        print ('menu_support.paste')
        sys.stdout.flush()

def quit():
        print ('menu_support.quit')
        sys.stdout.flush()
        sys.exit()

def radio_a():
        print ('menu_support.radio_a')
        sys.stdout.flush()

def radio_b():
        print ('menu_support.radio_b')
        sys.stdout.flush()

def save():
        print ('menu_support.save')
        sys.stdout.flush()

def init(top, gui, arg=None):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window ():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None


