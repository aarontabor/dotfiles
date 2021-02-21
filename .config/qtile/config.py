from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
alt = "mod1"

terminal = "alacritty"


keys = [
    # Switch between windows in current stack pane
    Key([mod], "k", lazy.layout.down(), desc="Move focus down in stack pane"),
    Key([mod], "j", lazy.layout.up(), desc="Move focus up in stack pane"),

    # Move windows up or down in current stack
    Key([mod, "shift"], "k", lazy.layout.shuffle_down(), desc="Move window down in current stack "),
    Key([mod, "shift"], "j", lazy.layout.shuffle_up(), desc="Move window up in current stack "),

    # Resize windows in Mondad-* views
    Key([mod], "equal", lazy.layout.grow(), desc="Increase size of current window"),
    Key([mod], "minus", lazy.layout.shrink(), desc="Decrease size of current window"),
    Key([mod, "shift"], "equal", lazy.layout.grow_main(), desc="Increase size of master window"),
    Key([mod, "shift"], "minus", lazy.layout.shrink_main(), desc="Decrease size of master window"),
    Key([mod], "0", lazy.layout.normalize(), desc="Reset secondary window sizes"),

    # Swap current window with master in Monad views
    Key([mod], "Return", lazy.layout.swap_main(), desc="Swap current window with master"),

    # Flip master region in Monad views (e.g., from left to right)
    Key([mod, "shift"], "Return", lazy.layout.flip(), desc="Flip the master region"),


    # Moving between (Physical) Screens
    Key([mod], "h", lazy.to_screen(0), desc="Move to Left Screen"),
    Key([mod], "l", lazy.to_screen(1), desc="Move to Right Screen"),

    # Working with Floating Windows
    Key([mod], "f", lazy.window.toggle_floating(), desc="Toggle Float"),
    Key([alt], "Tab", lazy.group.next_window(), lazy.window.bring_to_front(), desc="Alt-tab btwn Windows"),

    # Qtile System Commands
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.restart(), desc="Restart qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown qtile"),

    # Launch Rofi
    Key([mod], "space", lazy.spawn("rofi -show drun"), desc="Launch an Application"),

    # Volume Hotkeys
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle"), desc="Toggle Audio"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer set Master 1%- unmute"), desc="Decrease Audio"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer set Master 1%+ unmute"), desc="Increase Audio"),
]


groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(), desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=False), desc="Switch to & move focused window to group {}".format(i.name)),
    ])


layout_theme = {
        'border_width':0,
        'margin': 15,
        'fullscreen_border_width':0,
    }

layouts = [
    layout.Max(),
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
]


screens = [
    Screen(
        wallpaper='~/.background.jpg',
        wallpaper_mode='fill',
        # bottom=bar.Bar([ widget.CurrentLayout(), ], 30),
    ),
    Screen(
        wallpaper='~/.background.jpg',
        wallpaper_mode='fill',
        # bottom=bar.Bar([ widget.CurrentLayout(), ], 30),
    ),
]


mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]


dgroups_key_binder = None
dgroups_app_rules = []  # type: List
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
wmname = "QTile"
