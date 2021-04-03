from machine import Pin, TouchPad, PWM
from time import sleep
from netvars import setNetVar, getNetVar, initNet
import neopixel
import math
import time
import _thread

def color(position, r,g,b):
  pixels[position]=(r,g,b)
  pixels.write()

# remove all colors
def clearAll():
  for i in range(n):
    color(i,0,0,0)

def search(x):
    if x==0:
      pixels[n-1]=(0,0,0)
    else:
      pixels[x-1]=(0,0,0)
        
    pixels[x]=(50,50,50)  
    pixels.write()
    sleep(0.03)
   
def breathing(x,breathing_speed):  
    pixels.fill((int(((math.sin(x*breathing_speed)+1)/2)*255),0,0))  
    pixels.write()
    sleep(0.001)
    
#Capacitative Touch Pins
touchpad = TouchPad(Pin(12))
 
# EVENT LOOP #
remote_orb_action = "none"
local_orb = "orb2"
remote_orb = "orb1"

def network_task(touch):
  print("Starting Network Task")
  while True:
    if touch.read() < 450:
      setNetVar(local_orb,"touch")
      #print("Set Touch")
    else:
      setNetVar(local_orb,"none")
      #print("Set None")
    
    global remote_orb_action    
    remote_orb_action = getNetVar(remote_orb)
    #print(remote_orb_action)
    sleep(1)
 
def light_task(touch):
  print("Starting Light Task")
  
  search_counter=0
  breathing_counter=0
  breathing_speed = 0.15
  toggle = False
  
  try:
    while True:    
      if touch.read() < 450 and remote_orb_action=="touch":
        breathing(breathing_counter,breathing_speed)
        breathing_counter+=breathing_speed
       
      elif touch.read() > 450 and remote_orb_action=="touch":
        search(search_counter)
        search_counter=(search_counter+1)%n
      
      elif touch.read() < 450 and remote_orb_action=="none":
        search(search_counter)
        search_counter=(search_counter+1)%n
      
      else:
        search_counter=0
        breathing_counter=0
        clearAll()
       
  except KeyboardInterrupt:
    clearAll()
    print("done")



# SETUP #
# During Setup all LEDS will be green to indicate the orb is still connecting to the network
n=24 # number of leds
p=0 # connected Pin
pixels = neopixel.NeoPixel(Pin(p),n)

# Make all pixels green before setup
pixels.fill((0,255,0))
pixels.write()
    
# connect to wifi
initNet("WLAN-168808", "53476413711784902142")
print("connected")

setNetVar(local_orb,"none")
setNetVar(remote_orb,"none")

clearAll()
pixels.write()

# Start Network and Light Thread
try:
  t1 = _thread.start_new_thread( light_task, (touchpad,) )
  t2 = _thread.start_new_thread( network_task, (touchpad,) )
except KeyboardInterrupt:
  clearAll()
  t1.join()
  t2.join()















