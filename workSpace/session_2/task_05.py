from machine import Pin, ADC, PWM
from time import sleep

analogPin = ADC(0)
servoPin = Pin(5, Pin.OUT)
pwm = PWM(servoPin, freq=50)

try:
    while True:
        analogVal = analogPin.read()
        pwm.duty(int(analogVal/10))

except KeyboardInterrupt:
    pwm.deinit()
