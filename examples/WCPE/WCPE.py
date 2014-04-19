#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.2.2a
# In conjunction with Tcl version 8.6
#    Mar. 30, 2014 08:57:04 PM
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

import WCPE_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    root.title('WCPE__Now_Playing')
    root.geometry('811x632+996+108')
    WCPE_support.set_Tk_var()
    w = WCPE__Now_Playing (root)
    WCPE_support.init(root, w)
    root.mainloop()

w = None
def create_WCPE__Now_Playing (root, param=None):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    w.title('WCPE__Now_Playing')
    w.geometry('811x632+996+108')
    WCPE_support.set_Tk_var()
    w_win = WCPE__Now_Playing (w)
    WCPE_support.init(w, w_win, param)
    return w_win

def destroy_WCPE__Now_Playing ():
    global w
    w.destroy()
    w = None


class WCPE__Now_Playing:
    def __init__(self, master=None):
        _bgcolor = 'wheat'  # X11 color: #f5deb3
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#b2c9f4' # Closest X11 color: 'SlateGray2'
        _ana1color = '#eaf4b2' # Closest X11 color: '{pale goldenrod}' 
        _ana2color = '#f4bcb2' # Closest X11 color: 'RosyBrown2' 
        font10 = "-family {DejaVu Sans} -size 16 -weight normal -slant " + \
            " roman -underline 0 -overstrike 0"
        font11 = "-family {DejaVu Sans Mono} -size 14 -weight normal  " + \
            "-slant roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font=font10)
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])
        master.configure(background=_bgcolor)
        master.configure(highlightbackground="wheat")
        master.configure(highlightcolor="black")


        self.Scrolledtext1 = ScrolledText (master)
        self.Scrolledtext1.place(relx=0.01,rely=0.28,relheight=0.6
                ,relwidth=0.97)
        self.Scrolledtext1.configure(background="white")
        self.Scrolledtext1.configure(font=font11)
        self.Scrolledtext1.configure(highlightbackground="wheat")
        self.Scrolledtext1.configure(insertborderwidth="3")
        self.Scrolledtext1.configure(selectbackground="#ddc8a1")
        self.Scrolledtext1.configure(width=10)
        self.Scrolledtext1.configure(wrap=NONE)

        self.TSizegrip1 = ttk.Sizegrip(master)
        self.TSizegrip1.place(anchor=SE,relx=1.0,rely=1.0)

        self.Button1 = Button (master)
        self.Button1.place(relx=0.44,rely=0.92,height=33,width=63)
        self.Button1.configure(activebackground="#f4bcb2")
        self.Button1.configure(background=_bgcolor)
        self.Button1.configure(command=WCPE_support.quit)
        self.Button1.configure(disabledforeground="#b8a786")
        self.Button1.configure(font=font10)
        self.Button1.configure(highlightbackground="wheat")
        self.Button1.configure(text='''Quit''')

        self.Label1 = Label (master)
        self.Label1.place(relx=0.05,rely=0.02,height=27,width=185)
        self.Label1.configure(activebackground="#ffffcd")
        self.Label1.configure(background=_bgcolor)
        self.Label1.configure(disabledforeground="#b8a786")
        self.Label1.configure(font=font10)
        self.Label1.configure(highlightbackground="wheat")
        self.Label1.configure(text='''Current Local Time:''')

        self.Label2 = Label (master)
        self.Label2.place(relx=0.05,rely=0.06,height=27,width=104)
        self.Label2.configure(activebackground="#ffffcd")
        self.Label2.configure(background=_bgcolor)
        self.Label2.configure(disabledforeground="#b8a786")
        self.Label2.configure(font=font10)
        self.Label2.configure(highlightbackground="wheat")
        self.Label2.configure(text='''Composer:''')

        self.Label3 = Label (master)
        self.Label3.place(relx=0.05,rely=0.16,height=27,width=113)
        self.Label3.configure(activebackground="#ffffcd")
        self.Label3.configure(background=_bgcolor)
        self.Label3.configure(disabledforeground="#b8a786")
        self.Label3.configure(font=font10)
        self.Label3.configure(highlightbackground="wheat")
        self.Label3.configure(text='''Performers:''')

        self.Label4 = Label (master)
        self.Label4.place(relx=0.05,rely=0.11,height=27,width=49)
        self.Label4.configure(activebackground="#ffffcd")
        self.Label4.configure(background=_bgcolor)
        self.Label4.configure(disabledforeground="#b8a786")
        self.Label4.configure(font=font10)
        self.Label4.configure(highlightbackground="wheat")
        self.Label4.configure(text='''Title:''')

        self.Label5 = Label (master)
        self.Label5.place(relx=0.05,rely=0.21,height=27,width=106)
        self.Label5.configure(activebackground="#ffffcd")
        self.Label5.configure(background=_bgcolor)
        self.Label5.configure(disabledforeground="#b8a786")
        self.Label5.configure(font=font10)
        self.Label5.configure(highlightbackground="wheat")
        self.Label5.configure(text='''Start Time:''')

        self.Label6 = Label (master)
        self.Label6.place(relx=0.32,rely=0.02,height=27,width=223)
        self.Label6.configure(activebackground="#ffffcd")
        self.Label6.configure(anchor=W)
        self.Label6.configure(background=_bgcolor)
        self.Label6.configure(disabledforeground="#b8a786")
        self.Label6.configure(font=font10)
        self.Label6.configure(highlightbackground="wheat")
        self.Label6.configure(justify=LEFT)
        self.Label6.configure(text='''Label''')
        self.Label6.configure(textvariable=WCPE_support.time_current)

        self.Label7 = Label (master)
        self.Label7.place(relx=0.32,rely=0.06,height=27,width=233)
        self.Label7.configure(activebackground="#ffffcd")
        self.Label7.configure(anchor=W)
        self.Label7.configure(background=_bgcolor)
        self.Label7.configure(disabledforeground="#b8a786")
        self.Label7.configure(font=font10)
        self.Label7.configure(highlightbackground="wheat")
        self.Label7.configure(justify=LEFT)
        self.Label7.configure(text='''Label''')
        self.Label7.configure(textvariable=WCPE_support.composer)

        self.Label8 = Label (master)
        self.Label8.place(relx=0.32,rely=0.11,height=27,width=483)
        self.Label8.configure(activebackground="#ffffcd")
        self.Label8.configure(anchor=W)
        self.Label8.configure(background=_bgcolor)
        self.Label8.configure(disabledforeground="#b8a786")
        self.Label8.configure(font=font10)
        self.Label8.configure(highlightbackground="wheat")
        self.Label8.configure(justify=LEFT)
        self.Label8.configure(text='''Label''')
        self.Label8.configure(textvariable=WCPE_support.title)

        self.Label9 = Label (master)
        self.Label9.place(relx=0.32,rely=0.16,height=27,width=483)
        self.Label9.configure(activebackground="#ffffcd")
        self.Label9.configure(anchor=W)
        self.Label9.configure(background=_bgcolor)
        self.Label9.configure(disabledforeground="#b8a786")
        self.Label9.configure(font=font10)
        self.Label9.configure(highlightbackground="wheat")
        self.Label9.configure(justify=LEFT)
        self.Label9.configure(text='''Label''')
        self.Label9.configure(textvariable=WCPE_support.performers)

        self.Label10 = Label (master)
        self.Label10.place(relx=0.32,rely=0.21,height=27,width=483)
        self.Label10.configure(activebackground="#ffffcd")
        self.Label10.configure(anchor=W)
        self.Label10.configure(background=_bgcolor)
        self.Label10.configure(disabledforeground="#b8a786")
        self.Label10.configure(font=font10)
        self.Label10.configure(highlightbackground="wheat")
        self.Label10.configure(justify=LEFT)
        self.Label10.configure(text='''Label''')
        self.Label10.configure(textvariable=WCPE_support.start_time)




# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        self.configure(yscrollcommand=self._autoscroll(vsb),
            xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        vsb.grid(column=1, row=0, sticky='ns')
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (took from ScrolledText.py)
        if py3:
            methods = Pack.__dict__.keys() | Grid.__dict__.keys() \
                  | Place.__dict__.keys()
        else:
            methods = Pack.__dict__.keys() + Grid.__dict__.keys() \
                  + Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        return func(cls, container, **kw)
    return wrapped

class ScrolledText(AutoScroll, Text):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        Text.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

if __name__ == '__main__':
    vp_start_gui()



