# micronametag

Digital nametag with endless posibilities. Pure python microcontroller programming using an ESP8266 with an OLED display and MicroPython. After device setup use a web browser to code offline.

# Hardware

![DevBoard](https://i.imgur.com/tBAKK0w.png)

[ESP8266 Dev Board](https://heltec.org/project/wifi-kit-8/)

Open Hardware & Open Software

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
    cd examples/nametag
    python3 -m venv ../../venv
    source ../../venv/bin/activate
    pip install py-make
    pymake setup # or make setup
    
## Security
    
Copy the `.envtemplate` file to a new file called `.env` and edit the following application security settings:

    WEBREPL_PASSWORD=WEBREPL_PASSWORD_
    WIFI_SSID=net
    WIFI_PSK=password

## Upload

    source ../../venv/bin/activate
    pymake upload # or make upload

## Serial Console

    source ../../venv/bin/activate
    pymake serial # or make serial

## Help

[Quickstart tutorial](https://docs.micropython.org/en/latest/esp8266/quickref.html)
