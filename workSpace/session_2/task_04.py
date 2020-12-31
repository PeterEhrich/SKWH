import Stepper
from machine import Pin
import time

# for the ESP8266 
In1 = Pin(5,Pin.OUT) # IN1-> GPIO2 
In2 = Pin(4,Pin.OUT) # IN1-> GPIO0 
In3 = Pin(0,Pin.OUT) # IN1-> GPIO4 
In4 = Pin(2,Pin.OUT) # IN1-> GPIO5 

stepper = Stepper.create(In1,In2,In3,In4, delay=1)
full_rotation = 509

#Button
button = Pin(14,Pin.IN,Pin.PULL_UP)
button_prev_state = button.value()

# initialize variable to hold time when button is pressed
start = 0


def move_motor(time_delta):
  print("Time delta: " + str(delta) + "ms")
  if time_delta < 200:
    print("Short click")
    stepper.step((1/8)*full_rotation)
  else:
    print("Long click")
    stepper.step((1/2)*full_rotation)
    
  print("Rotation finished")
  print("----------------------------")

try:
  while True:
    if button.value() == 0 and button_prev_state == 1:
      start = time.ticks_ms() # get millisecond counter
      button_prev_state = button.value()
      
    elif button.value() == 1 and button_prev_state == 0:
      delta = time.ticks_diff(time.ticks_ms(), start) # compute time difference
      move_motor(delta)
      button_prev_state = button.value()
   
except KeyboardInterrupt:
    print("done")
  


#s1 = Stepper.create(In1,In2,In3,In4, delay=10)

#s1.step(509,-1)

#s1 = Stepper.create(In1,In2,In3,In4, delay=1)

#s1.step(509)
