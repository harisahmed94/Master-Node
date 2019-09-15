from machine import Pin
from network import LoRa
import socket
import machine
import ustruct

# make `S1` an input with the pull-up enabled
p_in = Pin('G17', mode=Pin.IN, pull=Pin.PULL_UP)

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

    if p_in() == 0:
        # sending '1' on the other device
        s.setblocking(True)
        pkt = ustruct.pack('b', 1)
        print(pkt)
        s.send(pkt)
