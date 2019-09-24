#archivo para la funciones de un calculadora y una calculadora cientifica
 
import numpy as np
from math import *
 
class calculadora:
	def suma(float,x,y):
		return x+y
		
	def resta(float,x,y):
		return x-y
		
	def multiplicacion(float,x,y):
		return x*y
		
	def division(float,x,y):
		if (y==0):
			print('la division por cero no existe')
		else:
			return x/y
		
		
		
class cientifica(calculadora):
	def seno(float,x):
		return np.sin(x)
		
	def coseno(float,x):
		return np.cos(x)
		
	def exponencial(float,x):
		return np.exp(x)
	
resultado = cientifica()

print('Bienvenido a la calculadora \n')
print(' 1. suma\n 2. resta\n 3. multiplicacion\n 4. division\n 5. seno\n 6.coseno\n 7. exponencial')

z = input('que operacion desea ejecutar : ')

if (z==1):
	x = input('ingrese el primer valor : ')
	y = input('ingrese el segundo valor : ')
	print ('\nla suma es : '+ str(resultado.suma(x,y)))
elif (z == 2):
	x = input('ingrese el primer valor : ')
	y = input('ingrese el segundo valor : ')
	print('\nla resta es : '+ str(resultado.resta(x,y)))
elif (z == 3):
	x = input('ingrese el primer valor : ')
	y = input('ingrese el segundo valor : ')
	print('\nla multiplicacion es : '+ str(resultado.multiplicacion(x,y)))
elif (z == 4):
	x = input('ingrese el primer valor : ')
	y = input('ingrese el segundo valor : ')
	print('\nla division es : '+ str(resultado.division(x,y)))
elif (z == 5):
	x = input('ingrese el  valor : ')
	print('\nel seno del valor dado es : '+ str(resultado.seno(x)))
elif (z == 6):
	x = input('ingrese el  valor : ')
	print('\nel coseno del valor dado es : '+ str(resultado.coseno(x)))
elif (z == 7):
	x = input('ingrese el  valor : ')
	print('\nla exponencial de el numero dado es : '+ str(resultado.exponencial(x)))
	
	
	
	
	
	
	
	
	

