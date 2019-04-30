from sklearn import tree
    



print("PINGUINO")
print("1 = Aleta ")
print("2 = Pico")
print("VACA")
print("3 = Pezuñas")
print("4 = Come hierba ")
print("MONO")
print("5 = Trepa ")
print("6 = Come banana ")
print("PALOMA")
print("7 = Vuela ")
print("8 = Tiene Pluma")






									



x=[[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7],[1,8],[2,1],[2,2],[2,3],[2,4],[2,5],[2,6],[2,7],[2,8],[3,1],[3,2],[3,3],[3,4],[3,5],[3,6],[3,7],[3,8],[4,1],[4,2],[4,3],[4,4],[4,5],[4,6],[4,7],[4,8],
[5,1],[5,2],[5,3],[5,4],[5,5],[5,6],[5,7],[5,8],[6,1],[6,2],[6,3],[6,4],[6,5],[6,6],[6,7],[6,8],[7,1],[7,2],[7,3],[7,4],[7,5],[7,6],[7,7],[7,8],[8,1],[8,2],[8,3],[8,4],[8,5],[8,6],[8,7],[8,8]]
    
	

	


y=[["Pinguino"],["Pinguino"],["Desconocido"],["Desconocido"],["Desconocido"],["Desconocido"],["Desconocido"],["Pinguino"],
["Pinguino"],["Pinguino"],["Desconocido"],["Desconocido"],["Desconocido"],["Desconocido"],["Paloma"],["Paloma o Pinguino"],
["Desconocido"],["Desconocido"],["Vaca"],["Vaca"],["Desconocido"],["Desconocido"],["Desconocido"],["Paloma"],
["Desconocido"],["Desconocido"],["Vaca"],["Vaca"],["Desconocido"],["Desconocido"],["Desconocido"],["Desconocido"],

["Desconocido"],["Desconocido"],["Desconocido"],["Desconocido"],["Mono"],["Mono"],["Desconocido"],["Desconocido"],
["Desconocido"],["Desconocido"],["Desconocido"],["Desconocido"],["Mono"],["Mono"],["Desconocido"],["Desconocido"],
["Desconocido"],["Paloma"],["Desconocido"],["Desconocido"],["Desconocido"],["Desconocido"],["Paloma"],["Paloma"],
["Pinguino"],["Pinguino o Paloma"],["Desconocido"],["Desconocido"],["Desconocido"],["Desconocido"],["Paloma"],["Paloma"]]

	

	




clf = tree.DecisionTreeClassifier()
clf = clf.fit(x,y)
print()
R= clf.predict([[1,1]])
print(R)



