from tkinter import  *

    

#--------------------------SECCION 1-------------------------------

#CREAMOS LA VENTANAS Y LAS ENTRADAS
ventana = Frame(height = 250 ,width= 200)
ventana.pack(padx = 5,pady =5)
vartxt1 = StringVar()


txt1 = Entry(ventana, textvariable = vartxt1).place(x=0, y=0)   
vartxt2 = StringVar()
txt2 = Entry(ventana, textvariable = vartxt2).place(x=100, y=0)

varres = StringVar()
txtres = Entry(ventana, textvariable = varres, width =100).place(x=0,y=145)


    

    





