# micronametag

Digital nametag with endless posibilities. Pure python microcontroller programming using an ESP8266 with an OLED display and MicroPython. All you need after setting up your device is a web browser to access the web console and start coding offline.

## Requirements

- Install git `https://git-scm.com/downloads`
- Install Python 3.6 or greater and python3-venv `https://www.python.org/downloads/`

## Setup on Linux

    apt install -y git python3 python3-venv
    
## Setup on Mac

    brew install python3 git
    
## Setup on Windows10

    choco install python3 git

## Setup development tools (all platforms)

    git clone https://github.com/sdaves/micronametag
    cd micronametag
    python3 -m venv venv
    . venv/bin/activate
    
    # with system make
    make setup 
    
    # or
    
    # without system make
    python3 -m pip install py-make
    python3 -m pymake setup

## Upload

    # with system make
    make upload
    
    # or
    
    # without system make
    python3 -m pymake upload

## Serial Console

    # with system make
    make serial
    
    # or
    
    # without system make
    python3 -m pymake serial

## Help

[Quickstart tutorial](https://docs.micropython.org/en/latest/esp8266/quickref.html)
