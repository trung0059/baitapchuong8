#Bai8.17
a = int(input("nhap so a:"))
b = int(input("nhap so b:"))
c=a*b
for i in range(b,c+1):
    if i%a == 0 and i%b==0:
        d = i 
        break
print(i)
