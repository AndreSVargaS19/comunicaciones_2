
print ('programa que realiza la suma y resta de dos numeros \n \n')

x = input('ingrese el valor de x = ')
y = input('\n ingrese el valor de y = ')
def suma(x,y):
	" retorna la suma de dos numeros"
	return x+y

def resta(x,y):
	" retrona la resta de dos numeros"
	return x-y
	
print ('x + y = ' + str(suma(x,y)))
print ('x - y = ' + str(resta(x,y)))
	
