print("[1] phong Standard")
print("[2] phong Superior Garden View")
print("[3] phong Superior Ocean View")
print("[4] phong Garden View Bungalow")
print("[5] phong Pool View Bungalow")
print("[6] phong Family Room")
print("[7] phong Beach Front Bungalow")
print("[8] phong VIP Sea View")
a = int(input("quy khach chon phong so: "))
b = int(input("so dem o lai: "))
a1 = 1260000
a2 = 1550000
a3 = 1830000
a4 = 2120000
a5 = 2540000
a6 = 4800000
if a == 1:
	print("gia 1 dem la 1,260,000 đồng")
	if 1<b <=3:
		c = a1*0.25
	if b>3:
		c = a1*0.3
	print("tong tien phong cua quy khach la",a1+(c-1)*b)
elif a == 2:
	print("gia 1 dem la 1,550,000 đồng")
	if 1<b <=3:
		c = a2*0.25
	if b>3:
		c = a2*0.3
	print("tong tien phong cua quy khach la",a2+(c-1)*b)
elif a == 3 or a == 4:
	print("gia 1 dem la  1,830,000 đồng")
	if 1<b <=3:
		c = a3*0.25
	if b>3:
		c = a3*0.3
	print("tong tien phong cua quy khach la",a3+(c-1)*b)
elif a == 5 or a == 6:
	print("gia 1 dem la 2,120,000 đồng")
	if 1<b <=3:
		c = a4*0.25
	if b>3:
		c = a4*0.3
	print("tong tien phong cua quy khach la",a4+(c-1)*b)
elif a == 7:
	print("gia 1 dem la 2,540,000 đồng")
	if 1<b <=3:
		c = a5*0.25
	if b>3:
		c = a5*0.3
	print("tong tien phong cua quy khach la",a5+(c-1)*b)
else:
	print("gia 1 dem la 4,800,000 đồng")
	if 1<b <=3:
		c = a6*0.25
	if b>3:
		c = a6*0.3
	print("tong tien phong cua quy khach la",a6+(c-1)*b)