#!/bin/bash

pacman_updates=$(checkupdates | wc -l)
yay_updates=$(yay -Qua | wc -l)

# Build JSON
json="{\"text\": \"󰣇 $((pacman_updates + yay_updates))\", \"tooltip\": \"󱧘 Official: $pacman_updates\n󱧘 AUR: $yay_updates\"}"

# Output JSON
echo $json