# input : n
# output : day so tu 1 -> (sum>n)
n = -1
while n < 0 :
    # neu n < 0 yeu cau lap lai
    n = int(input( "Nhap n (n>0): "))

sum = 0
i = 0
print(" day so tu 1 den tong vuot qua n:", end= ' ')
while sum <= n:
    sum += 1
    print( i, end= ' ')
    i += 1 