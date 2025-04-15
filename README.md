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

## Opening

Once the repository is cloned:

1. Open Visual Studio Code.
2. From the File menu, choose the "open workspace from file" menu option.
3. Navigate to the local location where you cloned the repository.
4. Open the `pico-player.code-workspace` file.

## Code Layout

## Electronics

# Hackathon

## Step 1 - Setup
Follow the pre-requisite and setup instructions above to get your local environment configured with all the necessary software.  Once the software is installed, clone the repository, and open VS Code (as described above).

## Step 2 - Lint / Testing
Python is an interpreted language.  This means that an interpreter reads the source code you write and runs it line-by-line, there is no compilation step.  Python commands and code are run from command line via the `python` executable that is installed when you installed Python on your machine.  Extra components for Python can be installed globally, or through a virtual environment (venv).  A virtual environment is useful if you need to run different versions of Python for different reasons.  The virtual environment enables you to configure / install dependencies LOCAL to the environment, so you don't wind up with conflicts in your global Python installation.

In the source code, the .venv folder contains the virtual environment configuration.  To activate a virtual environment in VS Code, use the *"Terminal"* menu at the top to open a new `Terminal` session.  This often defaults to a `cmd` terminal.  We'll want to switch to a `PowerShell` terminal.
![New Terminal Window](/assets/new_terminal.PNG)

![Switch to PowerShell](/assets/new_powershell.PNG)

With `PowerShell` as your current terminal (you can switch between terminal sessions) and in the root of the project, start typing `Li` and hit the `tab` key.  The tab key will auto-complete what you were typing based on what is currently in the directory.  If this works, it should have put `.\lint.ps1` in the prompt.  If so, hit the `Enter` key to execute the command.

This Python project has been configured with `flake8`, a static analysis linting tool used to check the syntax of the source code to make sure it follows accepted conventions and styles.  This is a useful way to make sure code remains clean, well-organized, and easier to maintain.  The linter should have no output and is configured to only check things in the `/src` folder of the repository.

## Step 3 - Pico Setup

Now that we have our environment setup, it's time to switch gears to some hardware.

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

### Electronics

The LEDs need *5V* power.  These LEDs are individually addressable via a tiny, embedded micro-controller within the LED that does the color shifting for you.  The color and brightness is sent via the `DIN` or Data In lead, `PWR` goes to the second lead, `GND` goes to the third lead, and `DOUT` or Data Out is the fourth.  By connecting the in / out of successive LEDs, we can create an array of addressable LEDs.

Each `PWR` lead gets a red wire up to the *5V* common power ("+") rail.
Each `GND` lead gets a black wire up to the *5V* common ground ("-") rail.

The first LED `DIN` pin gets a yellow (or pick your choice) wire connected to pin **#20** `(GPIO 15)`, while the `DOUT` of the first LED gets connected to the `DIN` of the second LED, thus completing our wiring.

Here is the diagram of how this should look:
![Pico Lights Wiring](/assets/pico_player_wiring_no_sound.jpg)

When you're done wiring, your setup should look similar to this:

![Pico Lights Breadboard Photo](/assets/pico_lights_wired_ph.jpg)
![Pico Lights Breadboard Illuminated Photo](/assets/pico_lights_wired_illuminated_ph.jpg)

### Coding

Having loaded the `*.uf2` firmware onto the Pico and with VSCode connected, you can also push code directly to the Pico.  For now, just create a new Python file. You can name it whatever you like with a `.py` extension.

As we mentioned before, these are not your average LEDs.  These are `WS2812` LEDs that have controllers built-in to make changing colors easier from just software.  To do this, we need several different components:

1. The Raspberry Pi Pico has an internal state machine that can be used to control / time the register on each LED
2. This state machine is exposed via a MicroPython extension that is SPECIFIC to the Raspberry Pi Pico

You may have noticed that with your Pico plugged in and your LEDs wired that the first one is illuminated (often blue).  This is because it's receiving power but not data.  To address this let's write some code that uses the state machine of the Pico.

Add this to your source file:

```python
import rp2
from machine import (Pin)
import array, time

@rp2.asm_pio(sideset_init=rp2.PIO.OUT_LOW, out_shiftdir=rp2.PIO.SHIFT_LEFT, autopull=True, pull_thresh=24) # Line 4
def ws2812():
    """WS2812 driver for LEDs on the RP2040 state machine (Raspberry PI specific)."""
    T1 = 2
    T2 = 5
    T3 = 3
    wrap_target()  # type: ignore # noqa: F821
    label("bitloop")  # type: ignore # noqa: F821
    out(x, 1)               .side(0)[T3 - 1]  # type: ignore # noqa: F821
    jmp(not_x, "do_zero")   .side(1)[T1 - 1]  # type: ignore # noqa: F821
    jmp("bitloop")          .side(1)[T2 - 1]  # type: ignore # noqa: F821
    label("do_zero")  # type: ignore # noqa: F821
    nop()                   .side(0)[T2 - 1]  # type: ignore # noqa: F821
    wrap()  # type: ignore # noqa: F821


def create_state_machine(gpio_num: int) -> rp2.StateMachine: # Line 20
    """Creates a StateMachine instance sending output on the given pin.
    :param pin_num: The pin number to send output of the state machine to."""
    sm = rp2.StateMachine(0, ws2812, freq=8_000_000, sideset_base=Pin(gpio_num))  # type: ignore

    return sm

```

This is the base code for the state machine.  The `rp2` import enables us to use the decorator on line **`4`** and use the functions being called on lines **`10-17`**.  The `ws2812` function contains the "timings" for the LED.  An in-depth explanation is outside the scope of this hackathon.  For further reading, check out:
- https://wp.josh.com/2014/05/13/ws2812-neopixels-are-not-so-finicky-once-you-get-to-know-them/
- https://cpldcpu.com/2014/01/14/light_ws2812-library-v2-0-part-i-understanding-the-ws2812/

Next, we have the `create_state_machine` method, which takes in a GPIO Pin Number as an argument, sets the frequency the LEDs run at and provides the `ws2812` method to the state machine for controlling the timings.

To make all of this work we need a bit more code.  Add the following lines of code:

```python

# Configure the number of WS2812 LEDs.
NUM_LEDS = 2
PIN_NUM = 15 # The gpio we have the LED hooked to above
brightness = 0.5 # These are bright, so you might want to drop this down further.  A number between 0 and 1

sm = create_state_machine(PIN_NUM)

# Start the StateMachine, it will wait for data on its FIFO.
sm.active(1)

# Display a pattern on the LEDs via an array of LED RGB values.
ar = array.array("I", [0 for _ in range(NUM_LEDS)])

##########################################################################
def pixels_show():
    """Illuminates the pixels by setting the colors assigned in the stored array in memory to the state machine and sets the brightness to the default"""
    dimmer_ar = array.array("I", [0 for _ in range(NUM_LEDS)])
    for i,c in enumerate(ar):
        r = int(((c >> 8) & 0xFF) * brightness)
        g = int(((c >> 16) & 0xFF) * brightness)
        b = int((c & 0xFF) * brightness)
        dimmer_ar[i] = (g << 16) + (r << 8) + b
    sm.put(dimmer_ar, 8)
    time.sleep_ms(10)

def pixels_set(i: int, color : tuple[int, int, int]):
    """Sets an individual pixel (addressed by array index) to the given color.
    :param i: The index of the LED in the array.
    :param color: The color tuple (r, g, b) to assign."""
    ar[i] = (color[0] << 16) + (color[1] << 8) + color[2]

def pixels_fill(color: tuple[int, int, int]):
    """Fills all pixels in the array with the given color.
    :param color: The color tuple (r, g, b) to assign."""
    for i in range(len(ar)):
        pixels_set(i, color)

# Define colors for ease of use
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
ORANGE = (200, 50, 0) # Orange is a hard color for WS2812 LEDs
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
PINK = (230, 120, 80) # Pink is a hard color for WS2812 LEDs
COLORS = (BLACK, RED, YELLOW, GREEN, CYAN, BLUE, PURPLE, WHITE, PINK, ORANGE)

pixels_fill(CYAN)
pixels_show()

```

After entering the code above into your file, click the "Run" button in the status bar of VS Code to send the file to the REPL (and for the Pico to run).

Did you get the LEDs to light up?  Try experimenting with the colors.  Set different pixels to different colors or even create your own colors.

You can also create effects with the LEDs using simple control structures and some math.

Try these by adding each to your python file and hitting "play" again:

```python
def show_all_colors():
    """Loops over all of the given colors in the 'Colors' tuple and updates the array of LEDs for each color, pausing slightly in-between each color."""
    print('Rotating between all colors')
    for color in COLORS:       
        pixels_fill(color)
        pixels_show()
        time.sleep(0.2)

show_all_colors()

```

In the above code, it's a simple rotation that loops through all the colors, setting them for all the LEDs.

```python

def wheel(pos: int):
    """Creates a color 'wheel' by rotating RGB values through the whole spectrum.  Intended to be combined with other lighting effects.
    :pos: The current color value (from 0 - 255)."""
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)
 
 
def rainbow_cycle(wait: int):
    """Creates a rainbow effect with each LED fading between colors.
    :param wait: The amount of time to wait between color changes."""
    for j in range(255):
        for i in range(NUM_LEDS):
            rc_index = (i * 256 // NUM_LEDS) + j
            pixels_set(i, wheel(rc_index & 255))
        pixels_show()
        time.sleep(wait)

rainbow_cycle(0)

```

The above code creates a nice rainbow effect.


```python

def fade_in(rgb: tuple[int, int, int], speed: float = 0):
    """Fades the given color in at the given speed.
    :param rgb: The color to fade to.
    :param speed: Smaller speeds are faster.  1 is EXTREMELY SLOW, 0.01 is a good starting point."""
    step = 10
    breath_amps = [ii for ii in range(0,255,step)]
    for ii in breath_amps:
        for jj in range(NUM_LEDS):
            pixels_set(jj, rgb) # show all colors
        pixels_show(ii/255)
        time.sleep(speed)

def fade_out(rgb: tuple[int, int, int], speed: float = 0):
    """Fades the given color out at the given speed.
    :param rgb: The color to fade from.
    :param speed: Smaller speeds are faster.  1 is EXTREMELY SLOW, 0.01 is a good starting point."""
    step = 5
    breath_amps = [ii for ii in range(255,-1,-step)]
    for ii in breath_amps:
        for jj in range(NUM_LEDS):
            pixels_set(jj, rgb) # show all colors
        pixels_show(ii/255)
        time.sleep(speed)

def fade_colors():
    """Fades each color in, then out."""
    for color in COLORS:
        fade_in(color, 0.01)
        fade_out(color, 0.01)

fade_colors()

```

With this, your LEDs are completely tested and we're ready to move on to the next phase!

A quick note on organization.  As you can see, your file is probably quite long at this point with a bunch of variables scattered in different places.  This is okay for prototyping, but it makes it MUCH harder to manager.  Python has the ability to import files from other files to help keep things separated.  We can also create "modules" for import that further improve our organization.

However, the Pico can NOT load files from your machine's hard drive.  In order for imports to work as expected they have to be on the file-system of the Raspberry Pi.

In the status bar of VS Code, you should see a button for "Toggle Mpy FS".  Click this button.
![MicroPico Show FileSystem](/assets/toggle_mpy_filesystem.PNG)

Which should show a window like this in the "files" view of VS Code:
![MicroPico MPS File System](/assets/mpy_filesystem.PNG)

From here, you can create new folders / files on the Pico directly.

More on this later.

## Step 6 - Sound

A Piezo buzzer is a low-cost electronic component that creates sound from deforming a ceramic material when voltage is applied.  Different voltages cause vibrations at different rates that result in differences in the tone produced.  To vary this electric voltage, we use a process called pulse-width-modulation (PWM).  The Raspberry Pi Pico can support up to 8 independent PWM devices.  PWM can occur when a PWM-controllable component is attached to any "light green" labelled GPIO pin. 

For further reading on PWM: https://control.com/technical-articles/understanding-the-basicsof-pulse-width-modulation-pwm/

For our purposes, the Piezo buzzer is polarized, which means the leads can only be connected in one way.  Typically the buzzer has the "+" and "-" leads marked on top.  Typically, the longer pin is the anode "+", while the shorter is cathode ("-") if the buzzer is not labelled.

Add a buzzer as shown in the diagram below.

![Pico Sound Wiring](/assets/pico_player_wiring_no_button.jpg)


![Pico Sound Wiring Photo](/assets/pico_sound_ph.jpg)

## Step 7 - Control

At this point, your board should look like this:

![Pico Board](/assets/pico_player_wiring.jpg)
![Pico Board Photo](/assets/pico_sound_button_ph.jpg)

## Step 8 - Mozart

# Resources
- MicroPython documentation for RP2040 (Pico): 

# Contributing

# Licenses