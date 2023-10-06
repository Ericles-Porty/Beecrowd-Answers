def partition(array, low, high):
 
    pivot = array[high]
 
    i = low - 1
 
    for j in range(low, high):
        if array[j] >= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1
 
def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)
 

num_linhas, num_colunas = map(int,input().split())

dados = []

for _ in range (num_linhas):
    dados.append(input().split(' '))

lista_numeros = [x for linha in dados for x in linha]


numeros = []
letras = []

for elemento in lista_numeros:
    temp = [*elemento]
    numeros.append(int(temp[0]))
    letras.append(temp[1])
v = []
d = []

for i in range(len(numeros)):
    if letras[i] == 'V':
        v.append(numeros[i])
    else:
        d.append(numeros[i])
    
size = len(v)
quickSort(v, 0, size - 1)

size = len(d)
quickSort(d, 0, size - 1)

for elemento in v:
    print(elemento,'V',sep='')

for elemento in d:
    print(elemento,'D',sep='')
