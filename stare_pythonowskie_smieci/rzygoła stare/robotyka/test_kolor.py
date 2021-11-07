from ev3dev2.sensor.lego import ColorSensor
import time

cl = ColorSensor()

while True:
    print(cl.color)
    time.sleep(1)
