# First test with T-PicoC3
print("Let's connect to Wifi")

import digitalio, board, time, busio
from adafruit_espatcontrol import adafruit_espatcontrol

# from https://github.com/Xinyuan-LilyGO/T-PicoC3/blob/main/example/Micropython/esp32c3_port/esp_at_port.py
#  UART(bus_num, baudrate=115200, tx=Pin(8), rx=Pin(9), cts=Pin(10), rts=Pin(11),txbuf=1024,rxbuf=1024)

TX = board.GP8 # board.ESP_RX
RX = board.GP9 # board.ESP_TX
resetpin = digitalio.DigitalInOut(board.GP10) # ESP_WIFI_EN
rtspin = digitalio.DigitalInOut(board.GP11) # board.ESP_RTS
uart = busio.UART(TX, RX, timeout=0.1)
debugflag = False

print("ESP AT commands")
# For Boards that do not have an rtspin like challenger_rp2040_wifi set rtspin to False.
esp = adafruit_espatcontrol.ESP_ATcontrol(
    uart, 115200, reset_pin=resetpin, rts_pin=rtspin, debug=debugflag
)
print("Resetting ESP module")
esp.hard_reset()

first_pass = True
while True:
    try:
        if first_pass:
            # Some ESP do not return OK on AP Scan.
            # See https://github.com/adafruit/Adafruit_CircuitPython_ESP_ATcontrol/issues/48
            # Comment out the next 3 lines if you get a No OK response to AT+CWLAP
            print("Scanning for AP's")
            for ap in esp.scan_APs():
                print(ap)
            print("Checking connection...")
            # secrets dictionary must contain 'ssid' and 'password' at a minimum
            print("Connecting...")
            esp.connect(secrets)
            print("Connected to AT software version ", esp.version)
            print("IP address ", esp.local_ip)
            first_pass = False
        print("Pinging 8.8.8.8...", end="")
        print(esp.ping("8.8.8.8"))
        time.sleep(10)
    except (ValueError, RuntimeError, adafruit_espatcontrol.OKError) as e:
        print("Failed to get data, retrying\n", e)
        print("Resetting ESP module")
        esp.hard_reset()
        continue
