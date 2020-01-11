import micronametag.ESP8266WebServer as server
from micronametag.decouple import config
import network
import machine

GPIO_NUM = config('GPIO_NUM', 2, int) # Builtin led

# Wi-Fi configuration
STA_SSID = config('WIFI_SSID')
STA_PSK = config('WIFI_PSK')

# Disable AP interface
ap_if = network.WLAN(network.AP_IF)
if ap_if.active():
  ap_if.active(False)
  
# Connect to Wi-Fi if not connected
sta_if = network.WLAN(network.STA_IF)
if not ap_if.active():
  sta_if.active(True)
if not sta_if.isconnected():
  sta_if.connect(STA_SSID, STA_PSK)
  # Wait for connecting to Wi-Fi
  while not sta_if.isconnected(): 
    pass

# Show IP address
print("Server started @ ", sta_if.ifconfig()[0])

# Get pin object for controlling builtin LED
pin = machine.Pin(GPIO_NUM, machine.Pin.OUT)
pin.on() # Turn LED off (it use sinking input)

# Handler for path "/" 
def handleRoot(socket, args):
  global rootPage
  # Replacing title text and display text color according 
  # to the status of LED
  response = rootPage.format(
    "Remote LED", 
    "red" if pin.value() else "green",
    "Off" if pin.value() else "On",
    "on" if pin.value() else "off",
    "Turn on" if pin.value() else "Turn off"
  )
  # Return the HTML page
  server.ok(socket, "200", response)

# Handler for path "/cmd?led=[on|off]"    
def handleCmd(socket, args):
  if 'led' in args:
    if args['led'] == 'on':
      pin.off()
    elif args['led'] == 'off':
      pin.on()
    handleRoot(socket, args)
  else:
    server.err(socket, "400", "Bad Request")

# handler for path "/switch" 
def handleSwitch(socket, args):
  pin.value(not pin.value()) # Switch back and forth
  server.ok(
    socket, 
    "200", 
    "On" if pin.value() == 0 else "Off")

def main(port=80):
  # Start the server
  server.begin(port)

  # Register handler for each path
  server.onPath("/info", handleRoot)
  server.onPath("/cmd", handleCmd)
  server.onPath("/switch", handleSwitch)

  # Setting the path to documents
  server.setDocPath("./www-console")

  try:
    while True:
      # Let server process requests
      server.handleClient()
  except:
    server.close()
