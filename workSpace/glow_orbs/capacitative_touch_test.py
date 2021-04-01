from machine import Pin, TouchPad, PWM
from time import sleep
from netvars import setNetVar, getNetVar, initNet
import neopixel
import math

# connect to wifi
#initNet("WLAN-168808", "53476413711784902142")
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
  
def search(x):
    if x==0:
      pixels[n-1]=(0,0,0)
    else:
      pixels[x-1]=(0,0,0)
        
    pixels[x]=(50,50,50)  
    pixels.write()
    sleep(0.02)
    return (search_counter+1)%n
    
def breathing(x,breathing_speed):  
    pixels.fill((int(((math.sin(x*breathing_speed)+1)/2)*255),0,0))  
    pixels.write()
    sleep(0.001)
    return x+=breathing_speed
    
def police(toogle):
  clearAll()
  
  if toggle:
    for i in range(0,12):
      pixels[i]=(255,0,0)
  else:
    for i in range(13,23):
      pixels[i]=(0,0,255)
  
  pixels.write()
  sleep(0.25)
  return not toggle

#Capacitative Touch Pins
touch = TouchPad(Pin(12))

#Variables for different lighting modes
search_counter=0
breathing_counter=0
breathing_speed = 0.15
toggle = False

try:
  while True: 
    
    if touch.read() < 450:
      #search_counter=search(search_counter)
      #breathing_counter=breathing(breathing_counter,breathing_speed)
      toggle = police(toggle)
      
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
  





