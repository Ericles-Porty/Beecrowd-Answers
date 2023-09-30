total = int(input())
print(total)

n100 = 0
n50 = 0
n20 = 0
n10 = 0
n5 = 0
n2 = 0
n1 = 0

while total >= 100:
    total -= 100
    n100 += 1
    
while total >= 50:
    total -= 50
    n50 += 1

while total >= 20:
    total -= 20
    n20 += 1

while total >= 10:
    total -= 10
    n10 += 1

while total >= 5:
    total -= 5
    n5 += 1

while total >= 2:
    total -= 2
    n2 += 1

while total >= 1:
    total -= 1
    n1 += 1

print(f'{n100} nota(s) de R$ 100,00')
print(f'{n50} nota(s) de R$ 50,00')
print(f'{n20} nota(s) de R$ 20,00')
print(f'{n10} nota(s) de R$ 10,00')
print(f'{n5} nota(s) de R$ 5,00')
print(f'{n2} nota(s) de R$ 2,00')
print(f'{n1} nota(s) de R$ 1,00')