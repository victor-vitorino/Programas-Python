a = int(input('Entre com um valor: '))
for num in range(a+1):
    div = 0
    for x in range(1, num+1):
        resto = num % x
       # print(x, resto)
        if resto ==0:
            div += 1

    if div ==2:
        print(num)