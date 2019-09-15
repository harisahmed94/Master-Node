import pycom
from network import LoRa
import socket
import machine


pycom.heartbeat(False)

# initialise LoRa in LORA mode
# Please pick the region that matches where you are using the device:
# Asia = LoRa.AS923
# Australia = LoRa.AU915
# Europe = LoRa.EU868
# United States = LoRa.US915
# more params can also be given, like frequency, tx power and spreading factor
lora = LoRa(mode=LoRa.LORA, region=LoRa.EU868)

# create a raw LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

while True:
    # get any data received...
    s.setblocking(False)
    data = s.recv(64)
    print(data)

    #check if the data is 1
    if data == b'\x01':
        pycom.rgbled(0x00FF00)  # Green
    else:
        pycom.rgbled(False)
