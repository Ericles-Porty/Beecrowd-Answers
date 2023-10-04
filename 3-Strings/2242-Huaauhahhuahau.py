def verifica(risada):
    if(risada == risada[::-1]):
        return True
    elif(len(risada) == 0):
        return False
    else:
        return False


def corta_consoantes(risada):
    risada_tratada = ""
    for i in risada:
        if(i in ("aeiou")):
            risada_tratada += i
    return risada_tratada


risada = str(input("")).lower()

vogais = corta_consoantes(risada)

if(verifica(vogais)):
    print("S")
else:
    print("N")