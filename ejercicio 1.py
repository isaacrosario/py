#------------------------------------------PRIMER EJERCICIO---------------------------------------
#------------------------------------------(¬RvP)^T↔(T↓P)------------------------------------------


# Operador ↔ (si_solo_si)-------solo es verdadera si ambas tienen el mismo valor-------------------

def si_solo_si(Valor2,Valor1):
       if (Valor1==True and Valor2 ==True) or (Valor1==False and Valor2==False):
               return True
       else:
               return False


# Operado ↓ (nini)---------------------solo es verdara si ambas son falsas-----------------------------
def nini(Valor1,Valor2):
    if Valor1==False and Valor2==False:
        return True
    else:
        return False



booleanos = [True,False]
print('R\tP\tT\t¬R\t(¬R v P)\t(¬R v P) ^ T\t(T ↓ P)\t\t(¬R v P) ^ T  ↔  (T ↓ P)')
print('-'*105)

for R in booleanos:        
        for P in booleanos:
                for T in booleanos:                        
                        print(R,P,T,not R,(not R or P),'',(not R or P) and T,'',nini(T,P),'','',si_solo_si((not R or P) and T,nini(T,P)),sep='\t')

print()


