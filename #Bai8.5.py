#Bai8.5
nam = int(input("nhap nam"))
if(nam % 400 == 0) or ((nam % 4 == 0) and (nam % 100 != 0)):
    print(nam,"la nam nhuan")
else:
    print(nam,"khong phai la nam nhuan")