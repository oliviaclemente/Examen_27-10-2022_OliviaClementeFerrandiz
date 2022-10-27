#ejercicio 7
print("ejercicio 7")
lista=[18, 50, 210, 80, 145, 333, 70, 30]
#Imprimr el número en caso de que sea múltiplo de 10 y menor que 200
try:
  lista=int(lista)
except:
  lista>200
while lista /10:
  lista=input("Números múltiplo de 10 y menor que 200")
print("Son:", lista)