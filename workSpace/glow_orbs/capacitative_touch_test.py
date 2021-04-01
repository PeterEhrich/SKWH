from machine import Pin, TouchPad, PWM
from time import sleep
from netvars import setNetVar, getNetVar, initNet
import neopixel

# connect to wifi
initNet("WLAN-168808", "53476413711784902142")
print("connected")

# number of leds
n=24
# connected Pin
p=0

pixels = neopixel.NeoPixel(Pin(p),n)

# colors the led at position in (r,g,b)
def color(position, r,g,b):
  pixels[position]=(r,g,b)
  pixels.write()

# remove all colors
def clearAll():
  for i in range(n):
    color(i,0,0,0)

# remove color from led at position
def clear(position):
  color(position,0,0,0)


# the color (r,g,b) should run x times like a cycle 
def cycle(r,g,b,wait,x): 
  # before setting new colors, clear the ring
  clearAll()
  
  # the cycle should run x times
  for j in range(x):
    for i in range(n):
      # clear the previous led
      if(i==0):
        clear(n-1)
      else:
        clear(i-1)
      
      # color the current led
      color(i,r,g,b)
      
      # wait, color is displayed this time
      sleep(wait)

#Capacitative Touch Pins
touch = TouchPad(Pin(12))

try:
  while True: 
    
    if touch.read() < 450:
      pixels.fill((255,0, 255))
      pixels.write()
    else:
      clearAll()
    
    # Touch logic
    #if touch1.read() < 300:
    #  setNetVar("orb1", "touch")
    #else:
      #setNetVar("orb1","none")
    
    #if touch2.read() <300:
      #setNetVar("orb2", "touch")
    #else:
      #setNetVar("orb2","none")
    
    #Light Logic
    #if getNetVar("orb1") == "touch" and getNetVar("orb2")=="touch":
      #rgb(255,255,255)
    #elif getNetVar("orb1") == "touch" or getNetVar("orb2")=="touch":
      #rgb(255,0,0)
    #else:
      #rgb(0,0,0)
     
    #sleep(0.25) 
    #print(touch1.read())
    
except KeyboardInterrupt:
  clearAll()
  print("done")
  




