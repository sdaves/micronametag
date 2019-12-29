.PHONY: setup upload serial
setup:
	python3 -m pip install pyserial esptool adafruit-ampy py-make
	ampy -p /dev/ttyUSB0 put ../../www/index.html
	ampy -p /dev/ttyUSB0 put ../../www/FileSaver.js
	ampy -p /dev/ttyUSB0 put ../../www/term.js
serial:
	python3 -m serial.tools.miniterm /dev/ttyUSB0 115200
upload:
	ampy -p /dev/ttyUSB0 put ../../lib/ESP8266WebServer.py
	ampy -p /dev/ttyUSB0 put ../../lib/TestWebServer.py
	ampy -p /dev/ttyUSB0 put ../../lib/nametag.py
	ampy -p /dev/ttyUSB0 put ../../lib/ssd1306.py
  
	ampy -p /dev/ttyUSB0 put boot.py
	ampy -p /dev/ttyUSB0 put main.py
	ampy -p /dev/ttyUSB0 put webrepl_cfg.py
