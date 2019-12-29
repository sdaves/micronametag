.PHONY: setup upload serial
setup:
	python3 -m pip install pyserial esptool adafruit-ampy py-make
serial:
	python3 -m serial.tools.miniterm /dev/ttyUSB0 115200
upload:
	ampy -p /dev/ttyUSB0 put main.py
