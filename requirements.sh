#!/bin/bash

# Check if the script is run with root privileges
if [ "$(id -u)" -ne 0 ]; then
  echo "Please run the script as root or using sudo."
  exit 1
fi

# Update package lists
apt update

# Install Python 3
apt install -y python3

#installing pip
apt-get install python3-pip

# Install FFmpeg
apt install -y ffmpeg

#install tkinter
pip install tkinter

echo "Installation complete."
