#ejercico 7
print("ejercicio 7")
n=  [18, 50, 210, 80, 145, 333, 70, 30]
n.remove(18)
n.remove(145)
print("n=",n)

try:
  n=int(n)
except:
  n=0
while not  0<= n <= 200:
  n=input("")
try:
  n=int(n)
except:
  n=0
print("Número multiples de 10 y menores a 200:")
print(50, 80, 70, 30)

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

#ejercicio 2
print("ejercicio 2")
cadena = "zeréP nauJ,01"
c=cadena [::-1].split(",")
print(c[1] +" ha sacado un " + c[0] +" de nota.")

#ejercicio 3
print("ejercicio 3")
numero_magico=12345679
numero_usuario= int(input("Introduce un número de usuario entre 1 y 9:"))
numero_usuario *=9 
numero_magico *= numero_usuario
print(numero_magico)

#ejercicio 6
print("ejercicio 6")
funcion_modificar=[-2, -1, 0, 0, 1, 2, 3, 3, 4, 5]
funcion_modificar.sort()
funcion_modificar.remove(0)
funcion_modificar.remove(3)
print("funcion_modificar=", funcion_modificar)

def separar(funcion_modificar1):
  pares= []
  impares= []
  for i in funcion_modificar1:
    if i%2 == 0:
      pares.append(i)
    else: 
      impares.append(i)
    pares.sort()
    impares.sort()
    return pares, impares
funcion_modificar1 = [funcion_modificar]
pares,impares= separar(funcion_modificar)
print("Pares:", pares)

suma_funcion=0
for funcion_modificar1 in funcion_modificar:
  suma_funcion += funcion_modificar1
print(suma_funcion)

pares.insert(0,suma_funcion)
print(pares)

suma_funcion = 0
for funcion in pares[2::]:
  suma_funcion += funcion_modificar
print(funcion_modificar)
print(pares[0] == pares[-1::])



