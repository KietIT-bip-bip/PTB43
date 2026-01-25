danh_sach_1 = [1, "a" , "abc123", 12.3, False]
#---------------------------
# Duyệt danh sách 
for i in range(len(danh_sach_1)):
    print(danh_sach_1[i])

#---------------------------
# thêm mới phần từ
for value in danh_sach_1:
    print(value)



#---------------------------
# thêm mới phần từ
# append (value)

danh_sach_1.append(100)
print(danh_sach_1)

#index
danh_sach_1.insert(len(danh_sach_1) -1, "new")
print(danh_sach_1)

#---------------------------
#sửa phần tử
danh_sach_1[4] = " updated item"
print(danh_sach_1)

#---------------------------
# xóa phàn tử
#pop() : xóa ở vị trí cuối cùng của danh sách -> trả về phần tử bị xóa
del_item = danh_sach_1.pop()
print(f"{del_item} đã đc xóa khỏi danh sách {danh_sach_1}")
#pop(index) xóa ở vị trí index -> trả về phần tử bị xóa
del_item_1 = danh_sach_1.pop(-1)
print(f"{del_item_1} đã đc xóa khỏi danh sách {danh_sach_1}")
# remove(value) xóa phần tử có value trùng hợp, nếu có nhiều phaanf tử giống -. xóa ở trái
# NOTE: remove trả về lỗi nếu ko có phần tử này
del_item_2 = danh_sach_1.remove(1)
print(danh_sach_1)

#clear: xóa hết danh sách -> trở thành danh sách rỗng
print(danh_sach_1.clear())

#---------------------------
# Sắp xếp danh sách
#sort(reverse=?) neu ? la false: tang dan | ? là True giảm dần
# NOTE: nêu muốn sắp xếp -> cùng kiểu dữ liệu trong danh sách
danh_sach_2 = ["a", "m ", "A", "x", "-"]

danh_sach_2.sort(reverse=True)
print(danh_sach_2) # giam dan
danh_sach_2.sort(reverse=False)
print(danh_sach_2) # tang dan

