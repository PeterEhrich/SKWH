from typing import ByteString
from machine import Pin, Timer, ADC, PWM, UART
from time import sleep
import math

green = Pin(0, Pin.OUT)
red = Pin(4, Pin.OUT)
yellow = Pin(5, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_UP)
blue = Pin(12, Pin.OUT)
bluePWM = PWM(blue, freq=1000)
adc = ADC(0)

# Period lenghts for each led
period_green = 100
period_red = 500
period_yellow = 1000

# Boolean to control timer
timer_switch = False


def initTimer(led, period):
    timer = Timer(-1)
    timer.init(period=period, mode=Timer.PERIODIC,
               callback=lambda x: led.on() if led.value() == 0 else led.off())
    return timer


def deinitTimers(timers):
    for timer in timers:
        timer.deinit()


def setBrightness(l, input):
    l.duty(input)
    print(input)
    sleep(0.1)


while True:
    try:
        if button.value() == 0:
            if not timer_switch:
                deinitTimers([g, r, y])
                timer_switch = True
            green.on()
            red.on()
            yellow.on()
        else:
            if timer_switch:
                g = initTimer(green, period_green)
                r = initTimer(red, period_red)
                y = initTimer(yellow, period_yellow)
                timer_switch = False

        setBrightness(bluePWM, adc.read())

    except KeyboardInterrupt:
        deinitTimers([g, r, y])
        green.off()
        red.off()
        yellow.off()
        blue.off()
        break
