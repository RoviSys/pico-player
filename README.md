# pico-player
Developed for a hackathon, this project walks individuals through the process of wiring, coding, and testing an "analog" media player using simple piezo buzzers and Python on Raspberry PI Pico micro-controllers.

# Getting Started
Raspberry Pi Pico is a low-cost micro-controller (almost a computer) that is simple to use for low-power applications and control.  Perfect for prototyping, hobbying, and in some limited situations, production use.  At it's core is the `RP2040` or the Raspberry Pi 2040.  This is the primary IC (integrated circuit) or the "brain" of the controller.  The board handles mapping of the pins of the RP2040 to a larger form-factor and delivering many useful features and peripherals.  Below is a pin diagram often called a "pinout" that shows the capabilities of the various "pins" on the Pico (all of which map back to a pin on the black IC in the middle of the board).

![Pico Pinout](/assets/pico_pinout.png)

In this hackathon we'll be building on top of this powerful platform to gain some applied knowledge of software and hardware concepts.

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
![Pico Breadboard](/assets/pico_player_wiring_no_rails.jpg)

Place the pico in the middle so there are an even number of open pin-holes on either side and the USB port is easily accessible.  From here, plug the USB cable into the Pico, then the other end into a USB port on your laptop.  Your setup should look like this:

![Pico Breadboard USB Photo](/assets/pico_usb_ph.jpg)

### Programming
We could write in c for the Pico. Unless you're a c expert and very familiar with register programming and embedded code this has a very high learning curve.  To reduce this learning curve, we can leverage Python which runs at a higher layer of abstraction.
To support that, we need firmware that allows us to run Python natively.  MicroPython provides just such a solution.  MicroPython is a platform that runs a limited subset of Python (CPython) that provides a convenient API to access the features of the Pico and runs Python natively on the Pico without needing a full operating system install.

Before we can do any work, we need to load a Micro Python uf2 bootloader firmware on the Pico so we can natively run Python code on the Raspberry Pi.

Firmware is a layer of code that interacts directly with hardware that serves as an abstraction for high-level software to be written independent of low-level register programming / hardware integration.
The firmware type depends on the micro controller in use and MicroPython is compatible with MANY different processors and micro controllers.

For the Pico, there are two flavors for the Pico 1:

- Pico https://micropython.org/download/RPI_PICO/
- Pico W (wireless) - https://micropython.org/download/RPI_PICO_W/

1. Download the appropriate firmware version for the Pico you're using.
2. When the download is complete, you should see the Pico as a new "drive" on your computer
3. Copy the uf2 file you downloaded to the root of the Raspberry Pi Pico "drive"
4. Doing so will cause the Pico to re-start.  When it re-starts you will NO LONGER see it in your "drive" list.

> For more detailed instructions, see here: https://docs.micropython.org/en/latest/rp2/tutorial/intro.html

### Hello, World!
At this point, your VS Code should automatically detect the new Pico and connect to it using the Pico VS Code Extension.  If it does not, try closing the workspace and re-opening it (with the Pico plugged in and the firmware loaded).  You can confirm this as a new terminal instance will pop up that looks like this:

![Pico Python REPL in VS Code](/assets/pico_connected_vscode.PNG)

Now we'll test things out by blinking the on-board LED on the pico.

We can issue commands through the REPL (Read-Eval-Print Loop is an abbreviation essentially for a command-line interpreter) directly to the Pico to test things out.

Write the following line of code in the REPL next to the `>>>`

```py
# Pico W
from machine import (Pin) # Then hit enter

Pin("LED", Pin.OUT).toggle() # Then hit enter

# if you have a Pico
from machine import (Pin) #  Then hit enter

Pin(25, Pin.OUT).toggle() # Then hit enter
```

If successful, you should see the on-board LED turn on:

![Pico LED on Photo](/assets/pico_led_on_ph.jpg)

Congratulations, you've complete the "Hello, World!" equivalent of a Raspberry Pi Pico with MicroPython.

## Step 4 - Rails
The Raspberry Pi Pico can be powered through several different mechanisms:

1. The `VSYS` Pin (**#39**)
2. USB Power

Like all hardware, certain characteristics determine how much "power" a device requires to operate.  The Pico is flexible and can be powered using a meager *1.8* (V) volts (only a bit more than a single AA battery), up to *5.5V* (often if you're coming from USB).  Delivering a higher voltage or lower voltage can cause damage to the Pico.

Similarly, a lot of electronic devices also have such characteristics.  Most commonly when working with Raspberry Pi's or Arduino's as a hobbyist, components use *3V* or *5V*.  The Pico uses a "buck-boost" converter so any voltage (of at least *1.8V*) can be boosted to *3.3V* on the `3V3(OUT)` pin (**#36**).

For this hackathon, we'll have a couple of devices that run on *3V* logic.  To support these devices, we'll take advantage of the "rails" of the breadboard (the side pieces labelled with + / -) to "extend" the connections so we can power multiple devices in parallel from the Pico's `3V3(OUT)` pin.  We do this by connecting a jumper wire (red is the convention for positive) from row 5 of our breadboard (where the Pico `3V3(OUT)` pin is) to the common "+" rail of the breadboard.

For complete circuits, we also need to ground the common **3V3 rail** we're creating, so we add a black wire to one of the `GND` pins of the Pico (**#37** for example) to the common ground rail "-" of the breadboard.

With this complete, any device that needs *3V* power can be plugged in to the common rail, and grounded to the common ground.

When we run on USB power, the `VBUS` Pin (**#40**) on the Pico exposes the voltage received from the USB connection (which happens to be *5V*).  We also have some components that require *5V* logic, so we run another set of ground / hot wires from the `VBUS` (and another GND pin, like **#3**) to the OPPOSITE rail on the breadboard.

Please see the images below for diagrams and example wiring.

![Pico Rail Configuration](/assets/pico_player_wiring_no_lights.jpg)
![Pico Rail Configuration Photo](/assets/pico_rails_wired_ph.jpg)

## Step 5 - Lights

The LEDs need *5V* power.  These LEDs are individually addressable via a tiny, embedded micro-controller within the LED that does the color shifting for you.  The color and brightness is sent via the `DIN` or Data In lead, `PWR` goes to the second lead, `GND` goes to the third lead, and `DOUT` or Data Out is the fourth.  By connecting the in / out of successive LEDs, we can create an array of addressable LEDs.

Each `PWR` lead gets a red wire up to the *5V* common power ("+") rail.
Each `GND` lead gets a black wire up to the *5V* common ground ("-") rail.

The first LED `DIN` pin gets a yellow (or pick your choice) wire connected to pin **#20** `(GPIO 15)`, while the `DOUT` of the first LED gets connected to the `DIN` of the second LED, thus completing our wiring.

TODO: More here and we have to load some code onto the pico.

![Pico Lights Wiring](/assets/pico_player_wiring_no_sound.jpg)
![Pico Lights Breadboard Photo](/assets/pico_lights_wired_ph.jpg)
![Pico Lights Breadboard Illuminated](/assets/pico_lights_wired_illuminated_ph.jpg)

## Step 6 - Sound

![Pico Sound Wiring](/assets/pico_player_wiring_no_button.jpg)

## Step 7 - Control

At this point, your board should look like this:

![Pico Board](/assets/pico_player_wiring.jpg)

## Step 8 - Mozart

# Resources
- MicroPython documentation for RP2040 (Pico): 

# Contributing

# Licenses