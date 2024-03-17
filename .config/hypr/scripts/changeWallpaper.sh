#!/bin/bash

## Files
DIR=$HOME/Pictures/Wallpapers
PICS=($(ls "${DIR}"))

dir="$HOME/.config/rofi/launchers/type-7"
theme='style-5'

## Rofi Command
rofi_command="rofi -dmenu -p 'choose...' \
              -theme '${dir}/${theme}.rasi'"

menu() {
    for pic in "${PICS[@]}"; do
        printf "${pic}\n"
    done
}

swww query || swww init

main() {
    choice=$(menu | eval "$rofi_command")
    swww img "${DIR}/${choice}" --transition-fps 60 --transition-type wipe --transition-duration 2.5
}

killall -f || main
