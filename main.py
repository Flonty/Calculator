def calc(a,b,znak):
    if znak=="+":
        print(a+b)
    elif znak=="-":
        print(a-b)
    elif znak=="*":
        print(a*b)
    elif znak=="/":
        print(a/b)
    else:
        print("Введите один из следующих знаков: +,-,*,/")