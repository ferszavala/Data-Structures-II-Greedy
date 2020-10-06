#Dada una cantidad solicitada, calcular el número de monedas (o billetes) a entregar. 
#Nota: la cantidad puede variar, pero las denominaciones de las monedas (o billetes) siempre serán: 100, 50, 20, 10, 5, 2, 1

monedas = [100,50,20,10,5,2,1]
l = len(monedas)

num=input("Ingrese el numero que desea: ")
num = int(num)
for i in range(l):
        bil = num//monedas[i]    
        num = num%monedas[i] 
        print("La cantidad de billetes o monedas de "+str(monedas[i])+" es: "+str(bil))
        
        
        
