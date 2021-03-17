from machine import ADC, Pin, PWM
from time import sleep
from netvars import setNetVar, getNetVar, initNet

# # assuming there is a network with ssid hotspot1 and password 123456789
# connect to wifi
initNet("Livebox-ABDA", "zaJKaeqxpQPeY9vHWf")

# Setup Potentiometer
adc = ADC(0)

# Set up speaker
pin = Pin(14, Pin.OUT)
beeper = PWM(pin, duty=512)

try:
    while True:
        setNetVar("peter_ehrich_task_1", str(adc.read()))
        a = getNetVar("peter_ehrich_task_1")
        print(a)
        beeper.freq(int(a))
        sleep(0.1)
except KeyboardInterrupt:
    beeper.deinit()
