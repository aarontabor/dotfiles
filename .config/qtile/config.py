from typing import List

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, KeyChord, Screen
from libqtile.lazy import lazy

mod = "mod4"
alt = "mod1"

terminal = "alacritty"


groups = [Group(i) for i in "mldcrx"]

keys = [

    # Moving between (Physical) Screens
    ## TODO: How does this ordering get assigned? Is this based on the order I specify in xrandr?
    Key([mod], "7", lazy.to_screen(2), desc="Move to Left Screen"),
    Key([mod], "8", lazy.to_screen(0), desc="Move to Right Screen"),
    Key([mod], "9", lazy.to_screen(1), desc="Move to Right Screen"),

    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus left"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus up"),

    # Move windows
    KeyChord([mod], "m", [
        Key([], "h", lazy.layout.shuffle_left(), desc="Move window left"),
        Key([], "j", lazy.layout.shuffle_down(), desc="Move window down"),
        Key([], "k", lazy.layout.shuffle_up(), desc="Move window up"),
        Key([], "l", lazy.layout.shuffle_right(), desc="Move window right"),
    ], mode="Move Window"),

    # Resize windows
    KeyChord([mod], "r", [
        Key([], "h", lazy.layout.grow_left(), desc="Resize window left"),
        Key([], "j", lazy.layout.grow_down(), desc="Resize window down"),
        Key([], "k", lazy.layout.grow_up(), desc="Resize window up"),
        Key([], "l", lazy.layout.grow_right(), desc="Resize window right"),
    ], mode="Resize Window"),

    # Working with Floating Windows
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle Float"),
    Key([alt], "Tab", lazy.group.next_window(), lazy.window.bring_to_front(), desc="Alt-tab btwn Windows"),

    Key([mod], "1", lazy.to_layout_index(0), desc="Single Column"),
    Key([mod], "2", lazy.to_layout_index(1), desc="Two Column"),
    Key([mod], "3", lazy.to_layout_index(2), desc="Three Column"),
    Key([mod], "4", lazy.to_layout_index(3), desc="Four Column"),
    Key([mod], "Return", lazy.layout.toggle_split(), desc="Toggle Column Splits"),

    # Group Management
    KeyChord([mod], "g", [Key([mod], i.name, lazy.group[i.name].toscreen()) for i in groups]),
    KeyChord([mod, "shift"], "g", [Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=False)) for i in groups]),

    # Qtile System Commands
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "r", lazy.restart(), desc="Restart qtile"),
    Key([mod, "shift"], "q", lazy.shutdown(), desc="Shutdown qtile"),

    # Launch Rofi
    Key([mod], "space", lazy.spawn("rofi -show drun"), desc="Launch an Application"),
]

layout_theme = {
        'border_width':0,
        'margin': 30,
        'fair': True,
        'split': True,
        'wrap_focus_columns': True,
        'wrap_focus_rows': True,
        'wrap_focus_stacks': True,
    }

layouts = [layout.Columns(num_columns=i, **layout_theme) for i in range(1,5)]


screen_settings = {
        'wallpaper': '~/.background.jpg',
        'wallpaper_mode': 'fill',
    }

def make_bar():
    return bar.Bar([
        widget.GroupBox(),
        widget.Chord(),
    ], 30)

screens = [Screen(**screen_settings, top=make_bar()) for _i in range(3)]


mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]


dgroups_key_binder = None
dgroups_app_rules = []  # type: ListR
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"
wmname = "QTileMaybe use key-sequence for this - for example, <mod>-g + a"
