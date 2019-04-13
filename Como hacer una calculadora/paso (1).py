from tkinter import  *


# Definicion de las funciones

def Sumar():
    varres.set("Suma = " + str (float(vartxt1.get())+ float(vartxt2.get() )))
def Restar():
    varres.set("Resta = " + str (float(vartxt1.get())- float(vartxt2.get() )))

def Multiplicar():
    varres.set("Multiplicacion = " + str (float(vartxt1.get())* float(vartxt2.get() )))

def Dividir():
	varres.set("Divicion = " + str (float(vartxt1.get()) / float(vartxt2.get() ))) 
    	
def Limpiar():
    varres.set("")
    vartxt1.set("")
    vartxt2.set("")

    




