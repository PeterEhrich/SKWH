from machine import Pin, TouchPad, PWM
from time import sleep
from netvars import setNetVar, getNetVar, initNet
import neopixel
import math
import time
import uasyncio

    
# SETUP #

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
  
def search(x):
    #if x==0:
      #pixels[n-1]=(0,0,0)
    #else:
      #pixels[x-1]=(0,0,0)
        
    pixels[x]=(50,50,50)  
    pixels.write()
    sleep(0.03)
    
    
def breathing(x,breathing_speed):  
    pixels.fill((int(((math.sin(x*breathing_speed)+1)/2)*255),0,0))  
    pixels.write()
    sleep(0.001)
    
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

#Capacitative Touch Pins
touch = TouchPad(Pin(12))
 
# EVENT LOOP #
search_counter=0
breathing_counter=0
breathing_speed = 0.15
toggle = False
orb2 = "touch"

async def getTouch():
  print("Starting Get Task")
  while True:
    orb2 = getNetVar("orb2")
    print("hi")
    await uasyncio.sleep(5)

async def setTouch():
  print("Starting Set Task")
  while True:
    if touch.read() < 450:
      setNetVar("orb1","touch")
    else:
      setNetVar("orb1","none")
    await uasyncio.sleep(5)

async def update_light():
  print("Starting orb")
  try:
    while True: 
      if touch.read() < 450 and orb2=="touch":
        breathing(breathing_counter,breathing_speed)
        breathing_counter+=breathing_speed
       
      elif touch.read() > 450 and orb2=="touch":
        search(search_counter)
        search_counter=(search_counter+1)%n
      
      elif touch.read() < 450 and orb2=="none":
        search(search_counter)
        search_counter=(search_counter+1)%n
      
      else:
        search_counter=0
        breathing_counter=0
        clearAll()
        
      await uasyncio.sleep_ms(100)
    
       
  except KeyboardInterrupt:
    clearAll()
    print("done")


event_loop = uasyncio.get_event_loop()
event_loop.create_task(getTouch())
event_loop.create_task(setTouch())

sleep(3)
event_loop.create_task(update_light())

event_loop.run_forever()











