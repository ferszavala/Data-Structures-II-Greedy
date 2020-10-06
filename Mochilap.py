#Dada la capacidad en kilogramos de una mochila, y una lista de objetos (indicando su peso y valor), 
#determinar cuáles objetos se incluirán en la mochila tratando de maximizar la ganancia.*/
capacidad_real = 5
c=0
peso = [1, 2, 2, 2]
ganancia = [5, 3, 2, 20]
mochila_optima =[]
perk = []
capacidad = 7

def funcion(cap, peso, ganancia):
    for i in range(0,4,1):
        c=0
        perk[i][0] = peso[i]
        perk[i][1] = ganancia[i]/peso[i]
        perk[i][2] = i
    for i in range(1,4,1):
        for j in range(i,0,-1):
            aux = [perk[j][0], perk[j][1], perk[j][2]]
            perk[j][0] = perk[j-1][0] 
            perk[j][1] = perk[j-1][1] 
            perk[j][2] = perk[j-1][2] #swap
            perk[j-1][0] = aux[0] 
            perk[j-1][1] = aux[1] 
            perk[j-1][2] = aux[2]
    for i in range(0,4,1):
        if perk[i][0]<cap :
            mochila_optima[perk[i][2]] = 1
            cap=cap-perk[i][0]
            c=int(c+int(perk[i][1])*int(perk[i][0]))
            
    print("La ganancia es : "+c+1)

#funcion(capacidad, peso, ganancia);
    print(str(mochila_optima)+" ")