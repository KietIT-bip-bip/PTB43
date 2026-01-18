# xac dinh canh tam giac#
#  input do dai 3 canh a b c
a = -1
b = -1
c = -1
while ( a or b and c) <= 0 :
    print("-----------------------------")
    print( " nhap do dai 3 canh a, b, c > 0")
    a = int(input( ' Nhập độ dài canh a(a>0):'))
    b = int(input(" NHập độ dài canh b ( b>0 ):"))
    c = int(input( ' Nhâp độ dài cạnh c (c>0):'))

if a + b > c and a + c > b and b + c > a:
    print(" 3 canh tren tao thanhn 1 tam giac")
else:
    print(" 3 canh tren tao thanh 1 tam giac")