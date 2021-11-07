from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.motor import MoveTank, OUTPUT_A, OUTPUT_D

cl = ColorSensor()
tank = MoveTank(OUTPUT_A, OUTPUT_D)

while cl.color != 5:
	print(cl.color_name)
	tank.on(left_speed=10, right_speed=10)

tank.on(left_speed=0, right_speed=0)
print(cl.color_name)
