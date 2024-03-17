#!/bin/bash

## Files
DIR=$HOME/Pictures/Wallpapers
PICS=($(ls "${DIR}"))

## Random Wallpaper
random_pic=$(printf "%s\n" "${PICS[RANDOM % ${#PICS[@]}]}")

swww query || swww init

swww img "${DIR}/${random_pic}" --transition-type none