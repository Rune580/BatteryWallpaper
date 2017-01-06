#!/usr/bin/env python3
import subprocess
import time, os, shutil, json
from subprocess import run


def get_battery_percentage():
    battery_percentage_command = "cat $(find /sys/class/power_supply/ -name 'BAT*' | head -n 1)/capacity"
    result = run(
        battery_percentage_command,
        shell=True,
        stdout=subprocess.PIPE,
        universal_newlines=True)
    return result.stdout.strip()


def main():
    background_image = ""
    while True:
        # Runs Script that gets current Battery Charge
        battery_percentage = int(get_battery_percentage())
        percentage_index = battery_percentage
        # Checks the values
        while percentage_index != 0 and not os.path.isfile(background_image):
            background_image = "./values/{}.png".format(str(percentage_index))
            percentage_index -= 1

        if battery_percentage == 0:
            # Pretty much what it says
            print("How is your computer still running?")
        if background_image != "":
            # Copies the correct image to a temp file
            shutil.copy(background_image, '.background-temp.png')
            print(background_image)
        # Runs another scipt that makes that temp file your background
        os.system('./background.sh')
        # Wait 1 Minute
        time.sleep(60)


main()
