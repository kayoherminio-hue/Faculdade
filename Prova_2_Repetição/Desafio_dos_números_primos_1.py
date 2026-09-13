qnt = int(input())
while qnt > 12 or qnt < 2:
    print('Informe um valor entre 2 e 12!')
    qnt = int(input())
cont = 0
b = []

while qnt > cont:
    a = int(input())
    cont2 = 1
    while True:
        cont2 += 1
        if a%cont2 == 0 and a !=cont2:
            break
        elif a == cont2:
            cont +=1
            b.append(a)
            break

c = 0
while c < len(b):
    print(b[c], end = " ")
    c += 1