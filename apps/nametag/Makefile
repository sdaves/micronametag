.PHONY: setup upload serial
setup:
	python3 -m pip install pyserial esptool adafruit-ampy py-make
	ampy -p /dev/ttyUSB0 put ../../www
	ampy -p /dev/ttyUSB0 put ../../lib
serial:
	python3 -m serial.tools.miniterm /dev/ttyUSB0 115200
upload:  
	ampy -p /dev/ttyUSB0 put .env
	ampy -p /dev/ttyUSB0 put webrepl_cfg.py
	ampy -p /dev/ttyUSB0 put server.py
	ampy -p /dev/ttyUSB0 put boot.py
	ampy -p /dev/ttyUSB0 put main.py
