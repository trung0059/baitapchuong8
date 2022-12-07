#Bai8.16
a = int(input("nhập số a: "))
b = int(input("nhập số b: "))
while(a*b!=0):
    if a>b:
        a%=b
    else:
        b%=a
print(a+b)