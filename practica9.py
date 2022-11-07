import msvcrt #teclas
import time
import random
from threading import Thread
import os
lista = []
velocidad1 = 0
velocidad2 = 0

def genNumero():
	numero = random.randint(1, 3)
	if(numero == 1):
		return 0.5
	elif(numero == 2):
		return 1
	else:
		return 2

class PrimerHilo(Thread):
	def run(self):
		global velocidad1
		while True:
			tecla = msvcrt.kbhit() and (msvcrt.getwch())
			if(tecla == 'q'):
				os.system("pause")
				velocidad1 = float(input("Ingrese la nueva velocidad: \n"))
			else:
				if len(lista) < 12:
					print("Un auto ha entrado")
					lista.append(1)
					print("Autos en el estacionamiento: ", len(lista))
					print(float(velocidad1))
					time.sleep(velocidad1) 
				else:
					print("No hay lugar para mas autos")
					time.sleep(velocidad1)

class SegundoHilo(Thread):
	def run(self):
		global velocidad2
		while True:
			tecla = msvcrt.kbhit() and (msvcrt.getwch())
			if(tecla == 'c'):
				os.system("pause")
				velocidad2 = float(input("Ingrese la nueva velocidad: \n"))
			else:
				if len(lista) > 0:
					print("Un auto ha salido")
					lista.pop(0)
					print("Autos en el estacionamiento: ", len(lista))
					print(float(velocidad2))
					time.sleep(velocidad2)
				else:
					time.sleep(velocidad2)

def main():
	global lista
	global velocidad1
	global velocidad2

	velocidad1 = genNumero()
	velocidad2 = genNumero()
	print(velocidad1,velocidad2)
	os.system("pause")

	primero = PrimerHilo()
	segundo = SegundoHilo()
	primero.start()
	segundo.start()

main()






