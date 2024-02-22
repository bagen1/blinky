from gpiozero import LED
from time import sleep

led_green = LED(18)
led_yellow1 = LED(15)
led_red = LED(14) 
led_yellow2 = LED(23)

leds = [led_yellow1, led_green,led_red, led_yellow2]

try:
    while True:
        for led in leds:
            led.on()
            sleep(1)
            led.off()
            sleep(1)
except KeyboardInterrupt:
    for led in leds:
        led.off()
