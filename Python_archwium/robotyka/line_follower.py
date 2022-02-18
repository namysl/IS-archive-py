#!/usr/bin/env python3
from ev3dev.ev3 import *
import time


def kalibruj():
	"""Funkcja kalibrujaca polozenie rownowagi"""
	sensor = ColorSensor()
	sensor.mode = 'COL-REFLECT'  # tryb rozpoznawania intesywnosci swiatla odbitego

	print('jest na linii?')
	time.sleep(5)  # czas na ustawienie sensora na linii
	black = sensor.value()  # odczyt czujnika koloru

	print('jest poza linia?')
	time.sleep(5)
	white = sensor.value()

	r = (white + black)/2  # sygnal wymuszajacy, sr. arytm. miedzy odczytem tla i linii
	return r


def regulator_dwustawny(speed):
	r = kalibruj()

	sensor = ColorSensor()
	sensor.mode = 'COL-COLOR'
	left_m = LargeMotor('outA')  # lewy silnik
	right_m = LargeMotor('outD')  # prawy silnik

	while sensor.color != 5:  # zatrzymaj, jesli wykryto czerwony
		sensor.mode = 'COL-REFLECT'
		y = sensor.value()
		e = r - y  # uchyb, odchylenie od polozenia rownowagi

		if e < 0:  # uruchamia prawy silnik
			right_m.run_timed(time_sp=100, speed_sp=speed)

		else:  # uruchamia lewy silnik
			left_m.run_timed(time_sp=100, speed_sp=speed)

		print(sensor.color)


def regulator_proporcjonalny(speed, k):
	r = kalibruj()

	sensor = ColorSensor()
	sensor.mode = 'COL-COLOR'
	left_m = LargeMotor('outA')
	right_m = LargeMotor('outD')

	while sensor.color != 5:
		sensor.mode = 'COL-REFLECT'

		y = sensor.value()
		e = r - y
		left_predkosc = speed - (k * e)
		right_predkosc = speed + (k * e)

		left_m.run_timed(time_sp=100, speed_sp=left_predkosc)
		right_m.run_timed(time_sp=100, speed_sp=right_predkosc)


def regulator_pid(speed, kp, ki, kd):
	r = kalibruj()

	sensor = ColorSensor()
	sensor.mode = 'COL-COLOR'
	left_m = LargeMotor('outA')
	right_m = LargeMotor('outD')

	derivative = 0
	integral = 0
	e_old = 0

	while sensor.color != 5:
		sensor.mode = 'COL-REFLECT'

		y = sensor.value()
		e = r - y

		derivative = e - e_old  # czlon rozniczkujacy, przewidywane uchyby
		integral += e  # czlon calkujacy, uchyby z przeszlosci

		u = kp * e + ki * integral + kd * derivative

		left_m.run_timed(time_sp=100, speed_sp=(speed-u))
		right_m.run_timed(time_sp=100, speed_sp=(speed+u))

		e_old = e


# regulator_dwustawny(50)
# regulator_proporcjonalny(50, 5)
# regulator_pid(50, 15, 0.1, 0.01)
