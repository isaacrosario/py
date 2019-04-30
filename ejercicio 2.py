#------------------------------------SEGUNDO EJERCICIO-------------------------------
#------------------------------------(R^P)¬T →(T not↔P)-----------------------------

# Operador not  ↔ o_bien_o_bien --------solo es falsa si ambas tienen el mismo valor---

def o_bien_o_bien(Valor2,Valor1):
       if (Valor1==True and Valor2 ==True) or (Valor1==False and Valor2==False):
               return False
       else:
               return True


# Operador Si_entonces → ----solo es falsa si la primera es verdadera y la segunda es falsa--
def si_entonces(Valor1,Valor2):
    if Valor1==True and Valor2==False:
        return False
    else:
        return True

       



booleanos = [True,False]
print('R\tP\tT\t¬T\t(R ^ P)\t\t(T not ↔ P) \t(R ^ P) → (T not ↔ P)')
print('-'*100)

for R in booleanos:        
       for P in booleanos:
                for T in booleanos:                        
                        print(R,P,T,not T,(R and P),'',o_bien_o_bien(T,P),'','',si_entonces(R and P,o_bien_o_bien(T,P)),sep='\t')

print()


