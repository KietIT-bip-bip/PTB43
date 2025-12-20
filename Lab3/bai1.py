# cau_kiem_tra : so_hs = ? du ?
cau_kiem_tra = input("Nhap so cau ktr:")
so_hs = input(" Nhap so hoc sinh:")

# chuyen du lieu
cau_kiem_tra = int(cau_kiem_tra)
so_hs = int(so_hs)

# ket luan
print(f""" Mỗi học sinh sẽ được làm {cau_kiem_tra//so_hs}câu kiểm tra, còn dư{cau_kiem_tra%so_hs}câu kiểm tra""" )