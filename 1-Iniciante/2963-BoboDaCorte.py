n = int(input())
index_maior = 0
maior = 0
for i in range(n):
    x = int(input())
    if x > maior:
        maior = x
        index_maior = i

if index_maior == 0:
    print("S")
else:
    print("N")