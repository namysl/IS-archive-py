#!/usr/bin/env python3
from ev3dev.ev3 import *
import math

R = 2.8  # promien kola
N = 360  # liczba impulsow na obrot
L = 11.8  # rozstaw kol
fi = 0
ksi = 0

x = 0  # aktualna pozycja
y = 0

x_cel = 0  # koordynaty celu
y_cel = 0

speed = 500

L_motor = LargeMotor('outA')  # silnik/kolo po lewej
R_motor = LargeMotor('outD')

L_motor.position = 0
R_motor.position = 0

L_position = L_motor.position
R_position = R_motor.position

old_L_pos = 0
old_R_pos = 0

sensor_central = UltrasonicSensor('in2')  # czujnik ultradzwiekowy (srodkowy)
sensor_left = InfraredSensor('in1')  # dwa boczne czujniki podczerwieni
sensor_right = InfraredSensor('in4')

theta = 0
dl = 0
dc = 0
dr = 0
e = 0


def calculate_position():
	"""jedz do celu"""
	global x, y, fi, L_motor, R_motor, L_position, R_position, old_L_pos, old_R_pos

	L_position = L_motor.position
	R_position = R_motor.position

	delta_L = L_position - old_L_pos  # przyrost drogi
	delta_R = R_position - old_R_pos

	D_L = 2 * math.pi * R * (delta_L / N)  # predkosc kol
	D_R = 2 * math.pi * R * (delta_R / N)

	Dc = (D_L + D_R) / 2  # droga przebyta przez srodek robota

	# unicycle:
	x += Dc * math.cos(fi)
	y += Dc * math.sin(fi)
	fi = fi + (D_R - D_L)/L

	old_L_pos = L_position
	old_R_pos = R_position

	return x, y, fi


def calculate_angle():
	"""jedz w kierunku"""
	global x, y, x_cel, y_cel, fi, ksi, e

	ksi = math.atan2((y_cel - y), (x_cel - x))  # ksi = kat do celu
	e = ksi - fi  # roznica miedzy kierunkiem gdzie chce jechac a gdzie jest

	return ksi, e


def obstacle():
	"""przeskalowanie wartosci czujnikow do wartosci w centymetrach"""
	global dc, dl, dr

	dc = sensor_central.value() / 10  # ultradzwiekowy, 255 cm max
	dl = sensor_left.value() / 100 * 70  # lewy podczerwieni, 70 cm max
	dr = sensor_right.value() / 100 * 70  # prawy podczerwieni

	print(dl, dc, dr)


def angle_from_obstacle():
	"""uklad wspolrzednych przeszkody, macierze sterujace rotacja"""
	global x, y, theta, dl, dc, dr, e
	x_central = x + dc * math.cos(theta) + 5*math.cos(theta)
	y_central = y + dc * math.sin(theta) + 5*math.sin(theta)
	x_left = x + 8*math.cos(theta) - 8*math.sin(theta) + dl*(math.cos(theta)/2-math.sqrt(3)/2*math.sin(theta))
	y_left = y + 8*math.cos(theta) + 8*math.sin(theta) + dl*(math.sin(theta)/2+math.sqrt(3)/2*math.cos(theta))
	x_right = x + 8*math.cos(theta) + 8*math.sin(theta) + dr*(math.cos(theta)/2+math.sqrt(3)/2*math.sin(theta))
	y_right = y - 8*math.cos(theta) + 8*math.sin(theta) + dr*(math.sin(theta)/2-math.sqrt(3)/2*math.cos(theta))

	xw = (x_left-x)+(x_central-x)+(x_right-x)
	yw = (y_left-y)+(y_central-y)+(y_right-y)
	beta = math.atan2(yw, xw)

	e = beta - theta
	e = math.atan2(math.sin(e), math.cos(e))


def start(meta, kp):
	"""wywolywuje funkcje sterujace robotem i uruchamia silniki"""
	global x_cel, y_cel, x, y

	x_cel = meta[0]
	y_cel = meta[1]

	drift = 2  # tolerancja w cm
	while (math.fabs(x_cel - x))**2 + (math.fabs(y_cel - y))**2 > drift**2:  # odleglosc od celu
		#calculate_position()
		#calculate_angle()

		obstacle()
		angle_from_obstacle()

		L_motor.run_timed(time_sp=50, speed_sp=(speed - e * kp))
		R_motor.run_timed(time_sp=50, speed_sp=(speed + e * kp))

	L_motor.stop()  # zatrzymuje silniki po osiagnieciu celu
	R_motor.stop()


points = [200, 0], [125, 100], [125, 200]

for i in points:
	start(i, 1000)
# najlepsze parametry: speed=500, kp=1000
