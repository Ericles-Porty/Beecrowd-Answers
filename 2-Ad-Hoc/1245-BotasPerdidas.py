def menor(a, b):
    if a < b:
        return a
    else:
        return b
   

while True:
    try:
        n = int(input())
    except:
        break
    quantidade_pares = 0
    tamanhos_L, tamanhos_D = [0]*61, [0]*61
    for _ in range(n):
        line = input().split(' ')
        tamanho = int(line[0])
        lado = str(line[1])
        if lado == 'D':
            tamanhos_D[tamanho] += 1
        else:
            tamanhos_L[tamanho] += 1
    for i in range(len(tamanhos_L)):
        quantidade_pares += menor(tamanhos_D[i], tamanhos_L[i])
    print(quantidade_pares)
