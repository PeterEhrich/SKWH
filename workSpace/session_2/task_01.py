from machine import Pin, PWM
import time
tempo = 4
tones = {
    'e3': 164.81,
    'f3': 174.61,
    'f3#': 185.00,
    'g3': 196.00,
    'a3': 220.00,
    'b3': 246.94,
    'c4': 262,
    'c4#': 277.18,
    'd4': 294,
    'e4': 330,
    'f4': 349,
    'f4#': 369.99,
    'g4': 392,
    'a4': 440,
    'b4': 494,
    'c5': 523,
    ' ': 0,
}

beeper = PWM(Pin(0, Pin.OUT), freq=440, duty=512)

feliz_navidad = [' ', ' ', 'a3', 'd4', 'c4#', 'd4',
                 'b3',
                 ' ', ' ', 'b3', 'e4', 'd4', 'b3',
                 'a3',
                 ' ', ' ', 'a3', 'd4', 'c4#', 'd4',
                 'b3', ' ', 'g3', 'g3', 'a3', 'b3', 'a3',
                 'a3', 'a3', 'a3', 'a3', 'g3', 'g3', 'f3#']

rhythm = [4, 8, 4, 4, 8, 8,
          4,
          4, 8, 4, 4, 8, 8,
          4,
          4, 8, 4, 4, 8, 8,
          4, 8, 8, 8, 8, 8, 8,
          8, 8, 8, 8, 4, 8, 8
          ]

for tone, length in zip(feliz_navidad, rhythm):
    beeper.duty(512)
    beeper.freq(round(tones[tone]))
    time.sleep(tempo/length)
    beeper.duty(0)
    time.sleep(0.01)


beeper.deinit()
