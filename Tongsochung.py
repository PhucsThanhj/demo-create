def tach(so):
    mang=[]
    while so > 0:
        le = so % 10
        so = so // 10
        mang.append(le)
    return set(mang)
#main
a = int(input("a: "))
b = int(input("b: "))
set1=tach(a)
set2=tach(b)
so_chung = set1 & set2
tong =0 
print("Cac so chung la: ")
for i in so_chung:
    print(i)
    tong+= i
print("Tong cac so chung la : ",tong)