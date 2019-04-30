#----------------------------------Tercer Ejercicio----------------------------------
#----------------------------------(R not↔P)↔(T v P)---------------------------------

# Operador not  ↔ o_bien_o_bien----solo es falsa si ambas tienen el mismo valor------

def o_bien_o_bien(Valor2,Valor1):
       if (Valor1==True and Valor2 ==True) or (Valor1==False and Valor2==False):
               return False
       else:
               return True


#Creando operador ↔ (si_solo_si)  //solo es verdadera si ambas tienen el mismo valor

def si_solo_si(Valor2,Valor1):
       if (Valor1==True and Valor2 ==True) or (Valor1==False and Valor2==False):
               return True
       else:
               return False

        



booleanos = [True,False]
print('R\tP\tT\t(R not ↔ P)\t(T v P)\t\t(R not ↔ P)↔(T v P) ')
print('-'*100)

for R in booleanos:        
       for P in booleanos:
                for T in booleanos:                        
                        print(R,P,T,o_bien_o_bien(R,P),'',T or P,'','',si_solo_si(o_bien_o_bien(R,P),T or P), sep='\t')






print()


#NOTAS

# alt 25 ↓
# alt 170 ¬