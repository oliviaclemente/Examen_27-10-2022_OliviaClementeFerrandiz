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



