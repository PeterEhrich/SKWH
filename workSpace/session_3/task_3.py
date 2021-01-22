from machine import I2C, Pin 
import ssd1306
from random import randrange
from time import sleep

# ESP32 reset pin for display must be 1 - this is pin16 
# should be done in ssd1306.py - if not uncommend the next 2 lines
#pin16 = Pin(16, Pin.OUT)
#pin16.value(1)

# Pins according the schematic https://heltec.org/project/wifi-kit-32/
i2c = I2C(-1, scl=Pin(15), sda=Pin(4))

#display size
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

quotes = ["Be yourself; everyone else is already taken.",
"Two things are infinite: the universe and human stupidity; and I'm not sure about the universe.",
"So many books, so little time.",
"A room without books is like a body without a soul.",
"Be the change that you wish to see in the world."]

while True:
  quote = quotes[randrange(len(quotes))]
  print(quote)
  
  text_y = 0
  row = []
  counter=0
  words = quote.split()
  for i,word in enumerate(words):
    row.append(word)
    counter +=1
    
    if counter == 3:
      oled.text(" ".join(row), 0, text_y)
      text_y+=10
      row = []
      counter = 0
      
    if i == len(words)-1:
      oled.text(" ".join(row), 0, text_y)
  
  oled.show()
  sleep(60)
  oled.fill(0)
