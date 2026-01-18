# Khai bao danh sach
list1 = [ "a", 12, 12.3, True, [1, 2, 3,]]
print("list = ", list1)
#---------------------------------
# danh sach rong
empty_list = []
if (empty_list): # [] = false
    print (' danh sach ko rong')
else:
    print(' danh sach rong')
#---------------------------------
# do dai danh sach
print(" do dai cau list1 =", len(list1)  )
print(" do dai cau empty_list = ", len(empty_list))

#---------------------------------
# truy cap phan tu dua tren index
print("list1[0]=", list1[0]) 
print(" list1[-1]",  list1[-1]) # truy cap phan tu cuoi cung
# print(empty_list[0]) # list index out of range
#------------------------ ----------
# thay doi phan tu dua tren index
list1[0] = " new value"
print(" list1 sau khi thay doi = ", list1)