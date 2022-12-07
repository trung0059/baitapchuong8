n = int(input("nhập vào số n lớn hơn 1: "))
a = True
if n<2:
    a = False
elif n ==2:
    a = True
elif n%2 ==0:
    a = False
else:
    for i in range(3,n,2):
        if n%i==0:
            a = False
if a == True:
    print(n, " là số nguyên tố")
else:
    print(n," không phải là số nguyên tố")