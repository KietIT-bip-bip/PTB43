# Đề: nhập 2 số:
# 1. tìm số lớn hơn
# 2. tính tổng 2 số
# 3. chia lấy phần nguyên
# ===================================
# xác định kiểu dữ liệu 
#truyền 2 số vào từ bàn phím với input
a = input (" a: ")
b = input(" b:")
print(a, type(a))
print(b, type(b))
# ===================================
# ép kiểu str -> int
# string -> float ( có thể có dấu .)
# str -> int ( không thể có dấu .)
# float -> (bị bỏ phần nguyên chỉ lấy phần thập phân)
a = int(a)
b = int(b)
# ==================================================================
# tính số lớn hơn
if a > b : 
    print ("a lon hon b" )
else :
    print ( "b lon hon a")

# ==================================================================
# tính số lớn hơn
print ( " tong 2 so", a+b)

# ==================================================================
# tính số lớn hơn
chia_lay_phan_nguyen = a//b
print("chia lay phan nguyen", chia_lay_phan_nguyen)
chia_phan_du = a%b
print("chia lay phan du", chia_phan_du)