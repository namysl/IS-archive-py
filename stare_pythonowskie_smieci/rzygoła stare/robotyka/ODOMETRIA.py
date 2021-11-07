#!/usr/bin/env python3
from ev3dev.ev3 import *
import math


R = 2.8  # promien kola
N = 360  # liczba impulsow na obrot
L = 11.8  # rozstaw kol
fi = 0
e = 0
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


def start(meta, kp):
	"""wywolywuje funkcje sterujace robotem i uruchamia silniki"""
	global x_cel, y_cel, x, y

	x_cel = meta[0]
	y_cel = meta[1]
	print(x_cel, y_cel)

	drift = 2  # tolerancja w cm
	while (math.fabs(x_cel - x))**2 + (math.fabs(y_cel - y))**2 > drift**2:  # odleglosc od celu
		calculate_position()
		calculate_angle()
		L_motor.run_timed(time_sp=10, speed_sp=(speed - e * kp))
		R_motor.run_timed(time_sp=10, speed_sp=(speed + e * kp))

	L_motor.stop()  # zatrzymuje silniki po osiagnieciu celu
	R_motor.stop()


points = [200, 0], [125, 100], [125, 200]  # wspolrzedne

for i in points:
	start(i, 200)
# jak na razie najlepiej dla speed = 500 i kp = 200
