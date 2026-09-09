a = int(input())
i = 1
while True:
    i += 1 
    if a%i == 0 and i!=a:
        print('Não é primo')
        break
    elif a==i:
        print('É primo')
        break
    