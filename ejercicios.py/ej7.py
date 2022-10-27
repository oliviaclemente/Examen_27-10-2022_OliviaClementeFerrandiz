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