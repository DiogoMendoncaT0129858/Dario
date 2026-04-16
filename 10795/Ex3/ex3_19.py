a = 1
b = 1

print(a, end=" ")
for i in range(59):
    temp = a
    a = b
    b = temp + b
    print(b, end=" ")