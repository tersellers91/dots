#! /bin/bash

sudo pacman -Rdd --noconfirm linux-firmware

sudo pacman -Syu --noconfirm linux-firmware waybar base-devel vim alacritty git python-pywal wget rofi $2 $3 $4 $5 $6 

if [ $1 == 1 ]
then
 sudo pacman -Rcns --noconfirm xfce4 xfconf xfce4-goodies libxfce4ui libxfce4util exo
fi



















