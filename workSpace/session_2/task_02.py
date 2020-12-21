from hcsr04 import HCSR04
from time import sleep

sensor = HCSR04(trigger_pin=14, echo_pin=12)
sleep(1)
i=0

while True:
  distance = sensor.distance_cm()
  print(i, ': Distance:', distance, 'cm')
  i+=1
  sleep(0.1)
