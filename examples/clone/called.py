#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.2g
# In conjunction with Tcl version 8.6
#    Feb. 11, 2014 04:14:41 PM
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

import called_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    root.title('Called')
    root.geometry('600x450+650+150')
    w = Called (root)
    called_support.init(root, w)
    root.mainloop()

w = None
def create_Called (root, param=None):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    w.title('Called')
    w.geometry('600x450+650+150')
    w_win = Called (w)
    called_support.init(w, w_win, param)
    return w_win

def destroy_Called ():
    global w
    w.destroy()
    w = None


class Called:
    def __init__(self, master=None):
        _bgcolor = 'wheat'  # X11 color: #f5deb3
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#b2c9f4' # Closest X11 color: 'SlateGray2'
        _ana1color = '#eaf4b2' # Closest X11 color: '{pale goldenrod}'
        _ana2color = '#f4bcb2' # Closest X11 color: 'RosyBrown2'
        font10 = "-family {DejaVu Sans} -size 16 -weight normal -slant " + \
            " roman -underline 0 -overstrike 0"
        master.configure(background=_bgcolor)
        master.configure(highlightbackground="wheat")
        master.configure(highlightcolor="black")


        self.Button1 = Button (master)
        self.Button1.place(relx=0.35,rely=0.24,height=33,width=148)
        self.Button1.configure(activebackground="#f4bcb2")
        self.Button1.configure(background=_bgcolor)
        self.Button1.configure(command=lambda:called_support.create_called(rt))
        self.Button1.configure(disabledforeground="#b8a786")
        self.Button1.configure(font=font10)
        self.Button1.configure(highlightbackground="wheat")
        self.Button1.configure(text='''Create Clone''')

        self.Button2 = Button (master)
        self.Button2.place(relx=0.42,rely=0.78,height=33,width=74)
        self.Button2.configure(activebackground="#f4bcb2")
        self.Button2.configure(background=_bgcolor)
        self.Button2.configure(command=lambda:master.destroy())
        self.Button2.configure(disabledforeground="#b8a786")
        self.Button2.configure(font=font10)
        self.Button2.configure(highlightbackground="wheat")
        self.Button2.configure(text='''Close''')

        self.Label1 = Label (master)
        self.Label1.place(relx=0.35,rely=0.49,height=27,width=273)
        self.Label1.configure(activebackground="#ffffcd")
        self.Label1.configure(anchor=W)
        self.Label1.configure(background=_bgcolor)
        self.Label1.configure(disabledforeground="#b8a786")
        self.Label1.configure(font=font10)
        self.Label1.configure(highlightbackground="wheat")
        self.Label1.configure(text='''Label''')
        self.instance = StringVar()
        self.Label1.configure(textvariable=self.instance)





if __name__ == '__main__':
    vp_start_gui()



