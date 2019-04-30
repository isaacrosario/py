#------------------------------QUINTO EJERCICIO---------------------------------
#------------------------------(R v P) ^ (T → P)-------------------------------


#Operador Si entonces → ---solo es falsa si la primera es verdadera y la segunda es falsa
def si_entonces(Valor1,Valor2):
    if Valor1==True and Valor2==False:
        return False
    else:
        return True


booleanos = [True,False]
print('R\tT\tP\t(R v P)\t\t(T → P)\t\t(R v P) ^ (T → P) ')
print('-'*75)

for R in booleanos:        
       for P in booleanos:
                for T in booleanos:                        
                        print(R,T,P,R or P,'',si_entonces(T,P),'','',(R or P) and si_entonces(T,P), sep='\t')

print()

