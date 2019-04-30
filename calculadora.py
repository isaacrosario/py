from tkinter import  *

    
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

    
#--------------------------SECCION 1-------------------------------

ventana = Frame(height = 250 ,width= 200)

ventana.pack(padx = 5,pady =5)

vartxt1 = StringVar()


txt1 = Entry(ventana, textvariable = vartxt1).place(x=0, y=0)   
vartxt2 = StringVar()
txt2 = Entry(ventana, textvariable = vartxt2).place(x=100, y=0)

varres = StringVar()
txtres = Entry(ventana, textvariable = varres, width =100).place(x=0,y=145)

#---------------------------SECCION 2--------------------------------


bsum = Button(ventana,command=Sumar, text = "Sumar",padx=42,pady=5,background="#58FA82").place(x=0,y=25)
bres= Button(ventana,command=Restar, text = "Restar",padx=42,pady=5,background="#58FA82").place(x=100,y=25)
bmul= Button(ventana,command=Multiplicar, text = "Multiplicar",padx=33,pady=5,background="#58FA82").place(x=0,y=65)
bdiv= Button(ventana,command=Dividir, text = "Dividir",padx=42,pady=5,background="#58FA82").place(x=100,y=65)
blim= Button(ventana,command=Limpiar, text = "Limpiar",padx=83,pady=5,background="#FAFA58").place(x=0,y=105)
ventana.mainloop()


    
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


    





