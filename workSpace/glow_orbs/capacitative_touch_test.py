from machine import Pin, TouchPad, PWM
from time import sleep
from netvars import setNetVar, getNetVar, initNet

# connect to wifi
initNet("WLAN-168808", "53476413711784902142")
print("connected")

#RGB LED
blue = PWM(Pin(26))
green = PWM(Pin(27))
red = PWM(Pin(14))

# base frequency for PWM is 1000Hz
blue.freq(1000)
green.freq(1000)
red.freq(1000)

def rgb(r=255,g=255,b=255):
  blue.duty(b*4)          # set duty cycle
  green.duty(g*4)          # set duty cycle
  red.duty(r*4)          # set duty cycle

#Capacitative Touch Pins
touch1 = TouchPad(Pin(2))
touch2 = TouchPad(Pin(12))

try:
  while True:
    sleep(0.5)
    
    # Touch logic
    if touch1.read() < 100:
      setNetVar("orb1", "touch")
    else:
      setNetVar("orb1","none")
    
    if touch2.read() <100:
      setNetVar("orb2", "touch")
    else:
      setNetVar("orb2","none")
    
    #Light Logic
    if getNetVar("orb1") == "touch" and getNetVar("orb2")=="touch":
      rgb(255,255,255)
    elif getNetVar("orb1") == "touch" or getNetVar("orb2")=="touch":
      rgb(255,0,0)
    else:
      rgb(0,0,0)
    
except KeyboardInterrupt:
  blue.deinit()
  red.deinit()
  green.deinit()
  print("done")
  

