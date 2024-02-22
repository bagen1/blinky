from gpiozero import LED
from time import sleep

led_green = LED(18)
led_yellow1 = LED(15)
led_red = LED(14) 
led_yellow2 = LED(23)

try:
    while True:
        led_yellow1.on()
        sleep(1)
        led_yellow1.off()
        sleep(1)
        led_green.on()
        sleep(1)
        led_green.off()
        sleep(1)
        led_red.on()
        sleep(1)
        led_red.off()
        sleep(1)
        led_yellow2.on()
        sleep(1)
        led_yellow2.off()
        sleep(1)
except KeyboardInterrupt:
    pass
