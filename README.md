# pico-player
Developed for a hackathon, this project walks individuals through the process of wiring, coding, and testing an "analog" media player using simple piezo buzzers and Python on Raspberry PI Pico micro-controllers.

# Getting Started

## Pre-requisites
To work on this hackathon, some software is needed prior to being able to run the code in this repository.

- [VS Code](https://code.visualstudio.com/) -> [Download Link⭷](https://code.visualstudio.com/docs/?dv=win64user)
- [Python 3.11.9](https://www.python.org/downloads/release/python-3119/) -> [(Download Link⭷)](https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe)
- [Python VS Code Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) -> [(Download Link⭷)](vscode:extension/ms-python.python)
- [Pylance VS Code Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) -> [(Download Link⭷)](vscode:extension/ms-python.vscode-pylance)
- [Raspberry Pi Pico VS Code Extension](https://marketplace.visualstudio.com/items?itemName=raspberry-pi.raspberry-pi-pico) -> [(Download Link⭷)](vscode:extension/raspberry-pi.raspberry-pi-pico)

## Cloning

```cmd
mkdir C:\Projects
mkdir C:\Projects\hackathon
cd Projects\hackathon
git clone https://github.com/RoviSys/pico-player.git -b hackathon
```

## Code Layout

## Electronics

# Hackathon

## Step 1 - Setup

Follow the pre-requisite and setup instructions above to get your local environment configured with all the necessary software.  Once the software is installed, clone the repository.

## Step 2 - Lint / Testing

Python is an interpreted language.  This means that an interpreter reads the source code you write and runs it line-by-line, there is no compilation step.  Python commands and code are run from command line via the `python` executable that is installed when you installed Python on your machine.  Extra components for Python can be installed globally, or through a virtual environment (venv).  A virtual environment is useful if you need to run different versions of Python for different reasons.  The virtual environment enables you to configure / install dependencies LOCAL to the environment, so you don't wind up with conflicts in your global Python installation.

In the source code, the .venv folder contains the virtual environment configuration.  To activate a virtual environment in VS Code, use the *"Terminal"* menu at the top to open a new `Terminal` session.  This often defaults to a `cmd` terminal.  We'll want to switch to a `PowerShell` terminal.
![New Terminal Window](/assets/new_terminal.PNG)

![Switch to PowerShell](/assets/new_powershell.PNG)


## Step 3 - Pico Setup

![Pico Breadboard](/assets/pico_wiring_no_rails.PNG)

Place the pico in the middle so there are an even number of open pin-holes on either side and the USB port is easily accessible.  From here, plug the USB cable into the Pico, then the other end into a USB port on your laptop.  

Before we can do any work, we need to load a Micro Python uf2 bootloader on the Pico so we can natively run Python code on the Raspberry Pi (as it doesn't have it's own OS).

TODO: uf2 load instructions

At this point, your VS Code should automatically detect the new Pico and connect to it using the Pico VS Code Extension.

Now we'll test things out by blinking the on-board LED on the pico.


## Step 4 - Rails

![Pico Rail Configuration](/assets/pico_wiring_no_lights.PNG)

## Step 5 - Lights

![Pico Lights Wiring](/assets/pico_player_wiring_no_sound.PNG)

## Step 6 - Sound

![Pico Sound Wiring](/assets/pico_player_wiring_no_button.PNG)

## Step 7 - Control

At this point, your board should look like this:

![Pico Board](/assets/pico_player_wiring.PNG)

## Step 8 - Mozart

# Contributing

# Licenses