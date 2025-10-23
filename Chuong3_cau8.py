#Câu 8: Nhập vào 2 giá trị a, b và phép toán ‘+’, ‘-’, ‘*’, ‘/’ . Hãy xuất kết quả theo đúng phép toán đã nhập.
a = float(input("Nhập giá trị a: "))
b = float(input("Nhập giá trị b: "))
pheptoan = input("Nhập phép toán (+, -, *, /): ")

if pheptoan == '+' :
    kq = a + b
elif pheptoan == '-' :
    kq = a - b
elif pheptoan == '*' :
    kq = a * b
elif pheptoan == '/' :
    if b != 0:
        kq = a / b
    else :
        kq = "Lỗi!!!"
else:
    kq = "Phép toán không hợp lệ!"

print("Kết quả: ", kq)