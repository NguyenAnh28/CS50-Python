import sys
from pyfiglet import Figlet
import random

if len(sys.argv) == 1:
    is_random_font = True
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    is_random_font = False
else:
    print("Input Error")
    sys.exit(1)

msg = input("Input: ")

# import activation
figlet = Figlet()

list = figlet.getFonts()

if is_random_font == False:
    try:
        figlet.setFont(font=sys.argv[2])
        print(f"Output:\n{figlet.renderText(msg)}")
    except:
        print("Input Error")
        sys.exit(1)
elif is_random_font == True:
    figlet.setFont(font=random.choice(list))
    print(f"Output:\n{figlet.renderText(msg)}")

