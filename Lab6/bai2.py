# in cac số chẵn từ 1 - n
n = -1
while n <= 0:
    n = int(input("Nhap so nguyen n > 0:"))
# [<gia tri can tra ve> for i in range(...) if <dieu kien>]
danh_sach_chan = [ i for i in range (1, n + 1) if i % 2 == 0]
print(f"danh sach so chan tu 1 den {n} laf: {danh_sach_chan}")