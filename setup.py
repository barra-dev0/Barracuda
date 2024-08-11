import os
import platform
os.system("pip install colorama")
from colorama import Fore,init

def cls():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

cls()

ascii_art = """
       /$$                                   /$$                           /$$                    
      | $$                                  | $$                          | $$                    
  /$$$$$$$  /$$$$$$  /$$  /$$  /$$ /$$$$$$$ | $$  /$$$$$$   /$$$$$$   /$$$$$$$  /$$$$$$   /$$$$$$ 
 /$$__  $$ /$$__  $$| $$ | $$ | $$| $$__  $$| $$ /$$__  $$ |____  $$ /$$__  $$ /$$__  $$ /$$__  $$
| $$  | $$| $$  \ $$| $$ | $$ | $$| $$  \ $$| $$| $$  \ $$  /$$$$$$$| $$  | $$| $$$$$$$$| $$  \__/
| $$  | $$| $$  | $$| $$ | $$ | $$| $$  | $$| $$| $$  | $$ /$$__  $$| $$  | $$| $$_____/| $$      
|  $$$$$$$|  $$$$$$/|  $$$$$/$$$$/| $$  | $$| $$|  $$$$$$/|  $$$$$$$|  $$$$$$$|  $$$$$$$| $$      
 \_______/ \______/  \_____/\___/ |__/  |__/|__/ \______/  \_______/ \_______/ \_______/|__/      
                                                                                            

"""

color_range = [Fore.BLUE, Fore.LIGHTBLUE_EX, Fore.WHITE, Fore.LIGHTBLACK_EX]
gradient_art = ""

for line in ascii_art.splitlines():
    for i, char in enumerate(line):
        color = color_range[i % len(color_range)]
        gradient_art += f"{color}{char}"
    gradient_art += "\n"

print(gradient_art)
os.system("pip install -r requirements.txt")

exit=input("Press any key to exit")
