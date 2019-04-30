
	

def add(x, y):	
   return x + y


def subtract(x, y):
	   return x - y


def multiply(x, y):
   		return x * y


def divide(x, y):
	   return x / y

while True:
	
	print("Seleccina operacion.")
	print("1. Suma")
	print("2. Resta")
	print("3. Multiplica")
	print("4. Divide")
	print("5. Salir")


	eleccion = input("Introdusca Seleccion(1/2/3/4/5):")
	if eleccion == '5':
		exit()
	num1 = int(input("Introdusca primer numero: "))
	num2 = int(input("Introdusca segundo numero: "))
	
	if eleccion == '1':
	   print("*********************************")
	   print("")
	   print(num1,"+",num2,"=", add(num1,num2))
	   print("")
	   print("*********************************")
	   

	elif eleccion == '2':
	   print("*********************************")
	   print("")
	   print(num1,"-",num2,"=", subtract(num1,num2))
	   print("")
	   print("*********************************")

	elif eleccion == '3':
	   print("*********************************")
	   print("")
	   print(num1,"*",num2,"=", multiply(num1,num2))
	   print("")
	   print("*********************************")
	
	elif eleccion == '4':
	   print("*********************************")
	   print("")
	   print(num1,"/",num2,"=", divide(num1,num2))
	   print("")
	   print("*********************************")
	


	else:
	   print("Entrada Invalida")