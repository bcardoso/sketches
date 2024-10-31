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
theme_path:str|None = None
color_palette:list[str] = []

def get_theme_path (name:str) -> str:
    return os.path.join(theme_dir, name.removesuffix(".yaml") + ".yaml")

def read_theme (path:str) -> list[str]:
    with open(path, 'r') as f:
        palette_data:dict[str,str] = yaml.safe_load(f)
    return ["#" + color for color in list(palette_data.values())[2:]]

def set_theme (name:str) -> None:
    global theme_name, theme_path, color_palette
    theme_name = name.removesuffix(".yaml")
    theme_path = get_theme_path(name)
    color_palette = read_theme(theme_path)

def list_themes_yaml () -> list[str]:
    return [f for f in os.listdir(theme_dir) if f.endswith('.yaml')]

def list_themes () -> None:
    [print(theme.removesuffix(".yaml")) for theme in list_themes_yaml()]
    print("\nCurrent:", theme_name)

def list_colors (name:str|None=None) -> list[str]:
    if name:
        return read_theme(get_theme_path(name or theme_name))
    else:
        return color_palette

def print_colors (name:str|None=None) -> None:
    for i, c in enumerate(list_colors(name or theme_name)):
        print("%2s: %s" % (i, c))

def pick_color (n:int=0,
                any:bool=False,
                range_a:int|None=None,
                range_b:int|None=None) -> str:
    if any or isinstance(range_a, int) or isinstance(range_b, int):
        return random.choice(color_palette[range_a:range_b])
    else:
        return color_palette[n]
