import math
print("Tính logarit cơ số a của x")
try:
    a = float(input("Nhập cơ số a: "))
    x = float(input("Nhập giá trị x: "))
    if a <= 0 or a == 1:
        print("Lỗi: Cơ số 'a' phải lớn hơn 0 và khác 1.")
    elif x <= 0:
        print("Lỗi: Giá trị 'x' phải lớn hơn 0 (để logarit có nghĩa).")
    else:
        ket_qua_log = math.log(x) / math.log(a)        
        print(f"log cơ số {a} của {x} là: {ket_qua_log}")
except ValueError:
    print("Lỗi: Vui lòng chỉ nhập số.")