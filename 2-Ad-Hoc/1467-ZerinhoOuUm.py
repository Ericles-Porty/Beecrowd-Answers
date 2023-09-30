try :
    while True:
        num = (input().split(' '))
        A = int(num[0])
        B = int(num[1])
        C = int(num[2])
        
        #empates
        if A == 1 and B == 1 and C == 1:   
            print("*")
            continue
        if A == 0 and B == 0 and C == 0:
            print("*")
            continue

        #vitoria do A
        if A == 0 and B == 1 and C == 1:
            print("A")
            continue
        if A == 1 and B == 0 and C == 0:
            print("A")
            continue

        #vitoria do B
        if A == 1 and B == 0 and C == 1:
            print("B")
            continue
        if A == 0 and B == 1 and C == 0:
            print("B")
            continue

        #vitoria do C
        if A == 0 and B == 0 and C == 1:
            print("C")
            continue
        if A == 1 and B == 1 and C == 0:
            print("C")
            continue
except: 
    exit()