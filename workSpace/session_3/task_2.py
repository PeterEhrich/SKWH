from machine import Pin
from hcsr04 import HCSR04
from time import sleep 
from netvars import setNetVar, getNetVar, initNet

# # assuming there is a network with ssid hotspot1 and password 123456789
# connect to wifi
initNet("FRITZ!Box Fon WLAN 7360", "26019589887890601540")

# assume our LED is connected to Pin 26, we use it as output 
LED = Pin(14, Pin.OUT)
sensor = HCSR04(trigger_pin=5, echo_pin=4)

old_distance = -1

while True:
  distance = sensor.distance_cm()
  
  if distance is not old_distance:
    setNetVar("peter_ehrich_task_2", "moved")
  else:
    setNetVar("peter_ehrich_task_2", "still")
  
  if getNetVar("peter_ehrich_task_2")=="moved":
    LED.on()
    sleep(5)
    LED.off()
  old_distance=distance
