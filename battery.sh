#! /usr/bin/env bash

val=$(upower -i /org/freedesktop/UPower/devices/battery_BAT1 | grep "percentage" | sed 's/[^0-9]*\([0-9]*\).*/\1/')
python3 -c "w = open('data.json', 'w+')
d = 'Charge'
val = str($val)
val = str(''' + val + ''')
w.write('{\"Charge\": \"$val\"}')
w.close"
