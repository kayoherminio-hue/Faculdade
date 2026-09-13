n = int(input())
s = []
n1 = 2 
n2 = 4
while n>=1:
    s.append(n/(n1*n2))
    n -= 1
    n1 += 4
    n2 += 4
print(f'{sum(s):.4f}')