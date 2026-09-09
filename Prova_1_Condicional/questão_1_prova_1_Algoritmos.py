n = int(input())

conta = 5
if n > 10:
    conta += min(n, 50) - 10
if n > 50:
    conta += (min(n, 80) - 50) * 2
if n > 80:
    conta += (n - 80) * 3
print(conta)
