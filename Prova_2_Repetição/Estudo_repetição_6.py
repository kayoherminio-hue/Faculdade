a = input()
if a.upper() != 'N':
    b = int(input())
    c = float(input())
    anos = []
    vel = []
    while True:
        anos.append(b)
        vel.append(c)
        a = input()
        if a.upper() == 'N':
            break
        b = int(input())
        c = float(input())
    print(f'{max(vel):.2f}\n{max(anos)}\n{sum(vel)/len(vel):.2f}')
else:
    print('zero')
    