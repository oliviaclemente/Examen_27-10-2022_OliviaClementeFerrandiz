#ejercicio 2
print("ejercicio 2")
cadena = "zeréP nauJ,01"
c=cadena [::-1].split(",")
print(c[1] +" ha sacado un " + c[0] +" de nota.")
print("")

#ejercicio 3
print("ejercicio 3")
numero_magico=12345679
numero_usuario= int(input("Introduce un número de usuario entre 1 y 9:"))
numero_usuario *=9 
numero_magico *= numero_usuario
print(numero_magico)
print("")

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