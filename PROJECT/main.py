import os
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
delete_xfce = input().upper()
console.print("Do you want to delete Artix Icons?\nYES or NO", style="purple bold")
delete_artix_icons = input().upper()
console.print("Do you want to replace your display manager with SDDM?\nYES or NO", style="purple bold")
sddm = input().upper()



if delete_xfce == 'YES':
    console.print("Deleting xfce.")
    time.sleep(0.5)
    os.system("sudo pacman -Rcns --noconfirm xfce4 xfconf xfce4-goodies libxfce4ui libxfce4util exo")
elif delete_artix_icons == 'YES':
    console.print("Deleting Artix Icons.")
    time.sleep(0.5)
    os.system("sudo pacman -Rcns --noconfirm artix-icons")


space(2)
console.print("CONTINUING", style="purple bold")
space(2)

os.system("sudo pacman -S --noconfirm git base-devel alacritty awww waybar xorg-xwayland python-pywal rofi brightnessctl wget otf-codenewroman-nerd pulseaudio")
os.system("mkdir ~/Build; cd ~/Build; git clone https://aur.archlinux.org/yay.git; cd yay; makepkg -si")
os.system("yay -S librewolf-bin")

space(2)
console.print("INSTALLING MANGOWM", style="purple bold")
space(2)

os.system("yay -S mangowm")
os.system("cd; cd Build; git clone https://github.com/tersellers91/dots.git")
os.system("cd ~/Build/dots/PROJECT/; cp -r waybar ~/.config/; cp -r mango ~/.config/")
space(2)
console.print("CLEANING UP", style="purple bold")
space(1)
os.system("yay -Yc")
space(1)
elif sddm == 'YES':
    console.print("Installing SDDM.", style="purple bold")
    os.system("sudo pacman -Rcns --noconfirm lightdm-runit")
    os.system("sudo pacman -S --noconfirm sddm-runit")
    os.system("sudo ln -s /etc/runit/sv/sddm /run/runit/service")
console.print("DONE", style="purple bold")

