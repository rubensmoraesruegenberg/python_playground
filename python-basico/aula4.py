contador = 1

while contador <= 5:
    print("Contador:", contador)
    contador += 1


#while
numero = 1

while numero <= 10:
    print(numero)
    numero += 1

#for
for i in range(5):
    print(i)

#range
range(1, 6)      # 1 a 5 diz que começa do 1
for i in range(1, 6):
    print("Número:", i)


range(0, 10, 2)  # 0, 2, 4, 6, 8 diz que começa do 1 e com intervalos de 2 em 2
for i in range(0, 10, 2):
    print("Número:", i)

range(5) #começa do 0
for i in range(5):
    print("Número:", i)


for i in range(10): #sai do loop quando atender a condição
    if i == 5:
        break
    print(i)