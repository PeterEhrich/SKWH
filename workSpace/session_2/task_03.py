from hcsr04 import HCSR04
from time import sleep
from machine import Pin, PWM

sensor = HCSR04(trigger_pin=12, echo_pin=14)
beeper = PWM(Pin(0, Pin.OUT), duty=512)

threshold = 100 #distance threshold in cm
max_freq = 1000
min_freq = 0

def scale_distance_to_frequency(distance):
  if distance<0:
    return max_freq
  
  elif distance > threshold:
    return min_freq
    
  else:
    fraction = abs((distance/threshold)-1)
    current_freq = max_freq*fraction
    return int(current_freq)

try:
  while True:
    distance = sensor.distance_cm()
    scaled_frequency = scale_distance_to_frequency(distance)
    print(scaled_frequency)
    beeper.freq(scaled_frequency)
    sleep(0.01)
    
except KeyboardInterrupt:
  beeper.deinit()
  
  



