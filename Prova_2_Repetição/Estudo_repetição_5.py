a = input().split()
r = []
while True:
    if 'FIM' in a:
        break
    a[0] = int(a[0])
    a[1] = int(a[1])
    a[2] = int(a[2])

    if (a[0] >= a[1]+a[2]) or (a[1] >= a[0]+a[2]) or (a[2] >= a[0]+a[1]):
        r.append('INVALIDO')
    elif a[0] != a[1] and a[1] != a[2] and a[0] != a[2]:
        r.append('ESCALENO')
    elif a[0] == a[1] and a[1] == a[2]:
        r.append('EQUILATERO')
    else:
        r.append('ISOSCELES')

    a = input().split()

b = 0
while b < len(r):
    print(r[b])
    b += 1