# tinh tong cac so chan tu 1 - n dk ( so nguyen(int), n > 0 )
n = -1
while n <=  0:
    n = int(input("nhập số nguyên n > 0:"))

tong = 0
for i in range(2,n + 1, 2):
    tong += i

print(f" tổng các số chăn từ 1 - {n} là: {tong}")
