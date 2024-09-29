"""
Color themes from base16 files.

Main functions: set_theme(), pick_color()

About base16 & color schemes:
- https://github.com/chriskempson/base16
- https://github.com/chriskempson/base16-default-schemes
- https://github.com/chriskempson/base16-schemes-source
"""

import os
import yaml
import random

theme_dir = "colors/"
theme_name = "ocean"
theme_path = None
color_palette = None

def get_theme_path (name:str):
    return os.path.join(theme_dir, name.removesuffix(".yaml") + ".yaml")

def read_theme (path:str):
    with open(path, 'r') as f:
        palette_data = yaml.safe_load(f)
    return ["#" + color for color in list(palette_data.values())[2:]]

def set_theme (name:str):
    global theme_name, theme_path, color_palette
    theme_name = name.removesuffix(".yaml")
    theme_path = get_theme_path(name)
    color_palette = read_theme(theme_path)

def list_themes_yaml ():
    return [f for f in os.listdir(theme_dir) if f.endswith('.yaml')]

def list_themes ():
    [print(theme.removesuffix(".yaml")) for theme in list_themes_yaml()]
    print("\nCurrent:", theme_name)

def list_colors (name:str|None=None):
    if name:
        return read_theme(get_theme_path(name or theme_name))
    else:
        return color_palette

def print_colors (name:str|None=None):
    for c in enumerate(list_colors(name or theme_name)):
        print("%2s: %s" % (c[0], c[1]))

def pick_color (n=1, any=False, range_a=None, range_b=None):
    if any or isinstance(range_a, int) or isinstance(range_b, int):
        return random.choice(color_palette[range_a:range_b])
    else:
        return color_palette[n]
