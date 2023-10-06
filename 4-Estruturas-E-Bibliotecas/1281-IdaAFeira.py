idas = int(input())
produtosR = []
precosR = []
dic = {}
for x in range(idas):
    qtProdutos = int(input())
    for j in range(qtProdutos):
        i = input().split()
        produto, preco = i[0], i[1]

        dic[produto]= preco

    compra = int(input())
    total = 0

    for z in range(compra):
        i = input().split()
        produto, qt = i[0], i[1]
        qt = int(qt)
        total += float(dic[produto]) * qt

    print(f'R$ %.2f' % total)
