#! /bin/bash

mkdir Build 
cd Build && git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -si
cd && cd Build && yay -S librewolf-bin
yay -S mangowm









