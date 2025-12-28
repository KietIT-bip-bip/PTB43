# VONG LAP VO HAN
# While < điều kiện > lặp lại cho đén khi điều kiện sai

# nhập nguyên chẵn a

a = input(" Nhap so nguyen chan a:")
while(int(a) % 2 !=0 or int(a) < 0):
    a = input(" Nhập lại một một số chẵn :")
print( " số chẵn a là", a)