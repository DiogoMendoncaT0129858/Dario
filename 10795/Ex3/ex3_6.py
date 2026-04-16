primos = []
n = 2

while len(primos) < 10:
    e_primo = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            e_primo = False
            break
    if e_primo:
        primos.append(n)
    n += 1

print(primos)