#! /usr/bin/env bash
dconf write /org/gnome/desktop/background/picture-uri  "'file://$(pwd)/.background-temp.png'"
dconf write /org/gnome/desktop/screensaver/picture-uri  "'file://$(pwd)/.background-temp.png'"
