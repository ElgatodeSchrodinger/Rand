import getch
primos = []
flag = 1
cantPrimos = 0
contador = 0
if(len(primos)==0):
    flag+=1
    primos.append(flag)
    cantPrimos += 1
while True:
    flag += 1   
    while contador < cantPrimos:
        if not (flag % primos[contador]):
            contador = 0
            break
        else:
            contador += 1
    if(contador):
        print("{} es primo ".format(flag))
        primos.append(flag)
        cantPrimos += 1
        contador = 0