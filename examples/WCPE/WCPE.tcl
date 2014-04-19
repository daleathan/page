#############################################################################
# Generated by PAGE version 4.2.2a
# in conjunction with Tcl version 8.6
#    Mar. 30, 2014 08:57:04 PM


vTcl:font:add_GUI_font font10 \
"-family {DejaVu Sans} -size 16 -weight normal -slant roman -underline 0 -overstrike 0"
vTcl:font:add_GUI_font font11 \
"-family {DejaVu Sans Mono} -size 14 -weight normal -slant roman -underline 0 -overstrike 0"
set vTcl(actual_gui_bg) wheat
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #b2c9f4
set vTcl(analog_color_p) #eaf4b2
set vTcl(analog_color_m) #f4bcb2
set vTcl(active_fg) #111111
#############################################################################
#################################
#LIBRARY PROCEDURES
#


if {[info exists vTcl(sourcing)]} {

proc vTcl:project:info {} {
    set base .top34
    namespace eval ::widgets::$base {
        set set,origin 1
        set set,size 1
        set runvisible 1
    }
    set site_3_0 $base.scr35
    namespace eval ::widgets_bindings {
        set tagslist _TopLevel
    }
    namespace eval ::vTcl::modules::main {
        set procs {
        }
        set compounds {
        }
        set projectType single
    }
}
}

#################################
# USER DEFINED PROCEDURES
#

#################################
# GENERATED GUI PROCEDURES
#

proc vTclWindow. {base} {
    if {$base == ""} {
        set base .
    }
    ###################
    # CREATING WIDGETS
    ###################
    wm focusmodel $top passive
    wm geometry $top 1x1+0+0; update
    wm maxsize $top 1905 1170
    wm minsize $top 1 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm withdraw $top
    wm title $top "page.tcl"
    bindtags $top "$top Page.tcl all"
    ###################
    # SETTING GEOMETRY
    ###################

    vTcl:FireEvent $base <<Ready>>
}

proc vTclWindow.top34 {base} {
    if {$base == ""} {
        set base .top34
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl:toplevel $top -class Toplevel \
        -background wheat -highlightbackground wheat -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 811x632+584+166; update
    wm maxsize $top 1905 1170
    wm minsize $top 1 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "WCPE  Now Playing"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    bindtags $top "$top Toplevel all _TopLevel"
    vTcl::widgets::ttk::scrolledtext::CreateCmd $top.scr35 \
        -background wheat -height 75 -highlightbackground wheat \
        -highlightcolor black -width 125 
    vTcl:DefineAlias "$top.scr35" "Scrolledtext1" vTcl:WidgetProc "Toplevel1" 1

    .top34.scr35.01 configure -background white \
        -font font11 \
        -foreground black \
        -height 3 \
        -highlightbackground wheat \
        -highlightcolor black \
        -insertbackground black \
        -insertborderwidth 3 \
        -selectbackground #ddc8a1 \
        -selectforeground black \
        -width 10 \
        -wrap none
    ttk::style configure TSizegrip -background wheat
    vTcl::widgets::ttk::sizegrip::CreateCmd $top.tSi36 \
        -cursor bottom_right_corner 
    vTcl:DefineAlias "$top.tSi36" "TSizegrip1" vTcl:WidgetProc "Toplevel1" 1
    button $top.but34 \
        -activebackground {#f4bcb2} -activeforeground black -background wheat \
        -command WCPE_support.quit -disabledforeground {#b8a786} -font font10 \
        -foreground {#000000} -highlightbackground wheat \
        -highlightcolor black -text Quit 
    vTcl:DefineAlias "$top.but34" "Button1" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab35 \
        -activebackground {#ffffcd} -activeforeground black -background wheat \
        -disabledforeground {#b8a786} -font font10 -foreground {#000000} \
        -highlightbackground wheat -highlightcolor black \
        -text {Current Local Time:} 
    vTcl:DefineAlias "$top.lab35" "Label1" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab36 \
        -activebackground {#ffffcd} -activeforeground black -background wheat \
        -disabledforeground {#b8a786} -font font10 -foreground {#000000} \
        -highlightbackground wheat -highlightcolor black -text Composer: 
    vTcl:DefineAlias "$top.lab36" "Label2" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab37 \
        -activebackground {#ffffcd} -activeforeground black -background wheat \
        -disabledforeground {#b8a786} -font font10 -foreground {#000000} \
        -highlightbackground wheat -highlightcolor black -text Performers: 
    vTcl:DefineAlias "$top.lab37" "Label3" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab38 \
        -activebackground {#ffffcd} -activeforeground black -background wheat \
        -disabledforeground {#b8a786} -font font10 -foreground {#000000} \
        -highlightbackground wheat -highlightcolor black -text Title: 
    vTcl:DefineAlias "$top.lab38" "Label4" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab40 \
        -activebackground {#ffffcd} -activeforeground black -background wheat \
        -disabledforeground {#b8a786} -font font10 -foreground {#000000} \
        -highlightbackground wheat -highlightcolor black -text {Start Time:} 
    vTcl:DefineAlias "$top.lab40" "Label5" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab34 \
        -activebackground {#ffffcd} -activeforeground black -anchor w \
        -background wheat -disabledforeground {#b8a786} -font font10 \
        -foreground {#000000} -highlightbackground wheat \
        -highlightcolor black -justify left -text Label \
        -textvariable time_current 
    vTcl:DefineAlias "$top.lab34" "Label6" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab39 \
        -activebackground {#ffffcd} -activeforeground black -anchor w \
        -background wheat -disabledforeground {#b8a786} -font font10 \
        -foreground {#000000} -highlightbackground wheat \
        -highlightcolor black -justify left -text Label \
        -textvariable composer 
    vTcl:DefineAlias "$top.lab39" "Label7" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab41 \
        -activebackground {#ffffcd} -activeforeground black -anchor w \
        -background wheat -disabledforeground {#b8a786} -font font10 \
        -foreground {#000000} -highlightbackground wheat \
        -highlightcolor black -justify left -text Label -textvariable title 
    vTcl:DefineAlias "$top.lab41" "Label8" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab42 \
        -activebackground {#ffffcd} -activeforeground black -anchor w \
        -background wheat -disabledforeground {#b8a786} -font font10 \
        -foreground {#000000} -highlightbackground wheat \
        -highlightcolor black -justify left -text Label \
        -textvariable performers 
    vTcl:DefineAlias "$top.lab42" "Label9" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab43 \
        -activebackground {#ffffcd} -activeforeground black -anchor w \
        -background wheat -disabledforeground {#b8a786} -font font10 \
        -foreground {#000000} -highlightbackground wheat \
        -highlightcolor black -justify left -text Label \
        -textvariable start_time 
    vTcl:DefineAlias "$top.lab43" "Label10" vTcl:WidgetProc "Toplevel1" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.scr35 \
        -in $top -x 10 -y 180 -width 786 -height 382 -anchor nw \
        -bordermode ignore 
    place $top.tSi36 \
        -in $top -x 0 -relx 1 -y 0 -rely 1 -anchor se -bordermode inside 
    place $top.but34 \
        -in $top -x 360 -y 580 -anchor nw -bordermode ignore 
    place $top.lab35 \
        -in $top -x 40 -y 10 -anchor nw -bordermode ignore 
    place $top.lab36 \
        -in $top -x 40 -y 40 -anchor nw -bordermode ignore 
    place $top.lab37 \
        -in $top -x 40 -y 100 -anchor nw -bordermode ignore 
    place $top.lab38 \
        -in $top -x 40 -y 70 -anchor nw -bordermode ignore 
    place $top.lab40 \
        -in $top -x 40 -y 130 -anchor nw -bordermode ignore 
    place $top.lab34 \
        -in $top -x 260 -y 10 -width 223 -height 27 -anchor nw \
        -bordermode ignore 
    place $top.lab39 \
        -in $top -x 260 -y 40 -width 233 -height 27 -anchor nw \
        -bordermode ignore 
    place $top.lab41 \
        -in $top -x 260 -y 70 -width 483 -height 27 -anchor nw \
        -bordermode ignore 
    place $top.lab42 \
        -in $top -x 260 -y 100 -width 483 -height 27 -anchor nw \
        -bordermode ignore 
    place $top.lab43 \
        -in $top -x 260 -y 130 -width 483 -height 27 -anchor nw \
        -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

#############################################################################
## Binding tag:  _TopLevel

bind "_TopLevel" <<Create>> {
    if {![info exists _topcount]} {set _topcount 0}; incr _topcount
}
bind "_TopLevel" <<DeleteWindow>> {
    if {[set ::%W::_modal]} {
                vTcl:Toplevel:WidgetProc %W endmodal
            } else {
                destroy %W; if {$_topcount == 0} {exit}
            }
}
bind "_TopLevel" <Destroy> {
    if {[winfo toplevel %W] == "%W"} {incr _topcount -1}
}

Window show .
Window show .top34

