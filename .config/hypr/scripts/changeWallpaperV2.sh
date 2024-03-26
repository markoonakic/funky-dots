#!/usr/bin/env sh

# set variables
RofiConf=$HOME/.config/rofi/wallSelect.rasi
cacheDir=$HOME/.cache/wallpapers

fullPath=$(echo "$ctlLine" | awk -F '|' '{print $NF}' | sed "s+~+$HOME+")
wallPath=$HOME/Pictures/Wallpapers


# scale for monitor x res
x_monres=$(hyprctl -j monitors | jq '.[] | select(.focused==true) | .width')
monitor_scale=$(hyprctl -j monitors | jq '.[] | select (.focused == true) | .scale' | sed 's/\.//')
x_monres=$(( x_monres * 17 / monitor_scale ))


# set rofi override
elem_border=$(( hypr_border * 3 ))
r_override="element{border-radius:50px;} listview{columns:6;spacing:100px;} element{padding:0px;orientation:vertical;} element-icon{size:${x_monres}px;border-radius:0px;} element-text{padding:20px;}"


# launch rofi menu
currentWall=$HOME/Pictures/Wallpapers/jack.png
RofiSel=$(ls ${wallPath} | while read rfile
do
    echo -en "$rfile\x00icon\x1f$HOME/Pictures/Wallpapers/${rfile}\n"
done | rofi -dmenu -theme-str "${r_override}" -config "${RofiConf}" -select "${currentWall}")


# apply wallpaper
swww query || swww init

swww img "${wallPath}/${RofiSel}" --transition-fps 60 --transition-type wipe --transition-duration 2.5

