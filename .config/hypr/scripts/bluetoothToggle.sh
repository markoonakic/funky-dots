#!/bin/bash

# Check the current Bluetooth status
status=$(bluetoothctl show | awk '/Powered/ {print $2}')

# Toggle Bluetooth based on the current status
if [ "$status" == "yes" ]; then
    echo "Turning Bluetooth off..."
    bluetoothctl power off
else
    echo "Turning Bluetooth on..."
    bluetoothctl power on
fi
