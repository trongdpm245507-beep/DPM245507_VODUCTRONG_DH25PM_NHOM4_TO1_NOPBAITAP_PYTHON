#Câu 3: Tính điểm trung bình
toan = float(input("Nhập điểm toán: "))
ly = float(input("Nhập điểm lý: "))
hoa = float(input("Nhập điểm hóa: "))
print("Điểm toán = ", toan)
print("Điểm lý = ", ly)
print("Điểm hóa = ", hoa)
dtb = (toan+ly+hoa)/3
print("Điểm trung bình = ", dtb)
print("Điểm làm tròn = ", round(dtb,2))