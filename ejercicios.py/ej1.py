#ejercicio 1
print("ejercicio 1")
var_1 = "Módulo 1 de Python"
var_1_mayusculas = var_1.upper()
print(var_1_mayusculas)
print(len(var_1))

var_2= len(var_1) / 7
print(var_2)
print(round(var_2, 4))

funcion1= 12 - (4 * 2) - (2 + 2)
print(funcion1)

funcion2= 12 - 4 * (2 - 2) + 2
print(funcion2)

funcion3= input("Introduce su edad:")
try: 
  funcion3=int(funcion3)
except:
  funcion3=0
if 1<= funcion3 <= 18:
  print("Menor de edad")
else:
  print("Mayor de edad")
print("")