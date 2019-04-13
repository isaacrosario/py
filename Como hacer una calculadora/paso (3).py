#CREANDO LOS BOTONES

bsum = Button(ventana,command=Sumar, text = "Sumar",padx=42,pady=5,background="#58FA82").place(x=0,y=25)
bres= Button(ventana,command=Restar, text = "Restar",padx=42,pady=5,background="#58FA82").place(x=100,y=25)
bmul= Button(ventana,command=Multiplicar, text = "Multiplicar",padx=33,pady=5,background="#58FA82").place(x=0,y=65)
bdiv= Button(ventana,command=Dividir, text = "Dividir",padx=42,pady=5,background="#58FA82").place(x=100,y=65)
blim= Button(ventana,command=Limpiar, text = "Limpiar",padx=83,pady=5,background="#FAFA58").place(x=0,y=105)
ventana.mainloop()






