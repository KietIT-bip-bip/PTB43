# ứng  dụng tạo câu hơi tính toán
# cách chơi
# 1. start
#2. exit
#3 skip ( continue/pass)
#3. nhập số luong câu hỏi : n (for)
#   4 nếu trả lời sai -> bắt ng ùng trl lại ( while )
#------------------
import random

# bắt đầu trò chơi
while True:
    choice = input("nhập 'start' để chơi, nhấn 'exit' để thoát:" )
    choice = choice.lower().strip() # chuyen ve thuong + xoa het khoang trang dau cuoi
    if choice == 'exit':
        print("chương trình kết thúc, Bye!")
        break
    if choice != 'start':
        print( "lựa chọn không hợp lợi")
        continue    
    # số lượng câu hỏi
    #input: n
    n = int(input(" Nhập số lượng câu hỏi"))
    while n <= 0:
        print(" số lượng câu hỏi phải lớn hơn 0")
        n = int(input("nhập lại số lần câu hỏi:"))
    # tao cau hoi dua tren so luong cau hoi
    for so_lan in range(1, n + 1):
        a = random.randint (1, 10)
        b = random.randint (1, 10)
        correct = a + b
        # in ca hoi
        question = f" {a} + {b} = "
        ans = ""
        #kiem tra cau tra loi
        while(ans == ""):
            ans = input(question)
            if ans.lower().strip() == "skip":
                print("Đã bỏ qua câu hỏi này!")
                break
            if int(ans) == correct:
                print("Đúng ->")
                break
            else:
                print("Sai xx")
                ans = ""