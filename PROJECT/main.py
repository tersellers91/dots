import subprocess
import pyfiglet
import time
from rich.console import Console
console = Console()
console.print(pyfiglet.figlet_format("INSTALL SCRIPT", font="swamp_land"), style="bold")
def space(count):
    for i in range(count):
        print()
space(9)
console.print("Welcome to the INSTALL SCRIPT!", style="bold red")
space(4)
console.print("By deafult, this script will do the following:", style="bold red")
space(1)
console.print("   Install waybar and mangowm.", style="blue bold")
console.print("   Install and setup yay package manager.", style="blue bold")
console.print("   Install Librewolf as the default browser.", style="blue bold")
console.print("   Use the configs from https://github.com/tersellers91/dots/tree/main/PROJECT.", style="blue bold")

space(1)

console.print("Do you want to delete xfce4? \nYES or NO", style="purple bold")
delete_xfce = input()
console.print("Do you want to delete Artix Icons?\nYES or NO", style="purple bold")
delete_artix_icons = input()



if delete_xfce == 'YES':
    console.print("Deleting xfce.")
    time.sleep(0.5)
    subprocess.run(["./setup.sh", "1"])
    #console.print("Deleting xfce.\r", end="")
    #time.sleep(0.5)
    #console.print("Deleting xfce..\r", end="")
    #time.sleep(0.5)
    #console.print("Deleting xfce...\r", end="")
    #time.sleep(0.5)
elif delete_artix_icons = 'YES':
    console.print("Deleting Artix Icons.")
    time.sleep(0.5)
    subprocess.run(["./remove.sh", "1"])
else:
    subprocess.run(["./setup.sh"])

space(2)
console.print("CONTINUING", style="purple bold")
space(2)

subprocess.run(["./yay.sh"])

subprocess.run(["./config.sh"])

space(2)

console.print(("DONE", style="purple bold")




