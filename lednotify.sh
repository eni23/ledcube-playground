#!/bin/bash

IFACE=org.freedesktop.Notifications
MEMBER=Notify

dbus-monitor --monitor "interface='$IFACE',member='$MEMBER'" |
while read -r line; do

    if [ "$(echo $line | grep 'mail-notification')" ]; then
      blinkstick --pulse --set-color='#00ff00' --duration=1000 --repeat=3
    fi

    if [ "$(echo $line | grep 'notify-send')" ]; then
      blinkstick --pulse --set-color='#0040ff' --duration=100
    fi

done
