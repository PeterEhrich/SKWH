from machine import Pin, TouchPad
from time import sleep

led = Pin(0,Pin.OUT)
touch = TouchPad(Pin(2))

try:
  while True:
    if touch.read() < 100:
      led.on()
    else:
      led.off()
except KeyboardInterrupt:
  led.off()
  print("done")
  
