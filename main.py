a=int(input("впишите первое число: "))
b=int(input("впишите второе число"))
znak=input("впишите действие")
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