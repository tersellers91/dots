#! /bin/bash

if [ $1 == 1 ] 
then
 sudo pacman -Rcns --noconfirm artix-icons
else
	echo "Continue"
fi
