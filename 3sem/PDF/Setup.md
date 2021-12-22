# Setup

## Remote Access
You are not going to connect a keyboard and monitor to your Raspberry PI.You are going to use the Raspberry PI **Headless**

## Raspberry Pi OS - SD Card
The Raspberry Pi needs an operating system to work. 

Raspberry Pi OS is the official supported operating system.

### Install Raspberry Pi OS using Raspberry Pi Imager
Raspberry Pi Imager is the quick and easy way to install Raspberry Pi OS and other operating systems to a microSD card, ready to use with the Raspberry Pi.

Download and install Raspberry Pi Imager to a computer with an SD card reader. Put the SD card you'll use with your Raspberry Pi into the reader and run Raspberry Pi Imager.

[www.raspberrypi.org/software](https://www.raspberrypi.org/software/)

<div style="page-break-after: always;"></div>

## Configure remote SSH access
In the root directory of the microSD card (normally labelled boot) create an empty file called **ssh**.

When the Pi boots, it looks for the **ssh** file. If it is found, **SSH is enabled** and the file is deleted.

The content of the file does not matter - *it can contain text, or nothing at all*

![ssh](https://github.com/officegeek/image/raw/main/ssh.png)

### SSH Access
Standard username and password:

- *pi*
- *raspberry*

*Remember to change that!*

You can use a terminal og a Windows program like PuTTY (www.putty.org)

## Wi-Fi
In the root directory of the microSD card (*normally labelled boot*) create an empty file called **wpa_supplicant.conf**

The content of the file:

    country=DK
    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
    update_config=1

    network={
        ssid="your_wifi_name"
        psk="your_wifi_password"
    }

The next time you boot up your Raspberry Pi, this file will automatically be moved to **/etc/wpa_supplicant/wpa_supplicant.conf**

If you need to edit the file, the location is: */etc/wpa_supplicant/*

<div style="page-break-after: always;"></div>

## Mobile HotSpot
Setup your phone to be a WiFi hotspot.
Connect the Raspberry Pi and your computer to that hotspot.

You can now use SSH to connect to the Raspberry Pi

<img src="https://github.com/officegeek/image/raw/main/mobil.jpg" width="220" />

<div style="page-break-after: always;"></div>

# Sense HAT

## Sense HAT layout
<img src="https://github.com/officegeek/image/raw/main/SenseHatOverview.png" width="280" />

## Sense HAT put together
<img src="https://github.com/officegeek/image/raw/main/ASSEMBLE_SENSE_HAT.png" width="200" />


### Sense Hat - error
If the Sense Hat return an error like: *OSError: Cannot detect RPi-Sense FB device*

Run this command in a terminal window:

- *sudo nano /boot/config.txt*

Scroll to the bottom of the file and add this line;

- *dtoverlay=rpi-sense*

Save the file and reboot the Raspberry Pi

<div style="page-break-after: always;"></div>

# Python Demo
Use this Python demo script.

Create a Python file:

    from sense_hat import SenseHat
    sense = SenseHat()
    sense.show_message("Hello world")

**Run it**


# VNC
Sometimes it is not convenient to work directly on the Raspberry Pi. Maybe you would like to work on it from another device by remote control.

VNC is a graphical desktop sharing system that allows you to remotely control the desktop interface of one computer (running VNC Server) from another computer or mobile device (running VNC Viewer). 

VNC Viewer transmits the keyboard and either mouse or touch events to VNC Server, and receives updates to the screen in return.

See more at [VNC](https://www.raspberrypi.org/documentation/remote-access/vnc/)

# Documentation
Use [www.raspberrypi.org](https://www.raspberrypi.org) as your primary source.

