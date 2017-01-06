import time, os, shutil, json

def main():
    bgImage = ""
    while True:
        # Runs Script that gets current Battery Charge
        os.system("./battery.sh")
        time.sleep(1)
        # Reads The Charge Note: Looking for a better way
        with open('data.json', 'r') as f:
            data = json.load(f)
            val = int(data["Charge"])
        a = 100
        # Checks the values
        while a != 0:
            if val == a:
                bgImage = "./values/"+ str(val) +".png"
                if os.path.isfile(bgImage) != True:
                    # If the wallpaper doesn't exist move down a value until you find one
                    val -= 1
                    continue
            a -= 1
        if val == 0:
            # Pretty much what it says
            print("How is your computer still running?")
        if bgImage != "":
            #Copies the correct image to a temp file
            shutil.copy(bgImage, '.background-temp.png')
        # Runs another scipt that makes that temp file your background
        os.system('./background.sh')
        # Wait 1 Minute
        time.sleep(60)

main()
