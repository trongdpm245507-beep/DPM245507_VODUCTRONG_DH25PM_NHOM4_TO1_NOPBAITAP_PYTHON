#Câu 9: Nhập vào 1 tháng, xuất ra tháng đó thuộc quý mấy trong năm.
thang = int(input("Nhập tháng (1-12): "))

if 1 <= thang <= 3:
    print("Tháng", thang, "thuộc quý I (từ tháng 1 đến tháng 3)")
elif 4 <= thang <= 6:
    print("Tháng", thang, "thuộc quý II (từ tháng 4 đến tháng 6)")
elif 7 <= thang <= 9:
    print("Tháng", thang, "thuộc quý III (từ tháng 7 đến tháng 9)")
elif 10 <= thang <= 12:
    print("Tháng", thang, "thuộc quý IV (từ tháng 10 đến tháng 12)")
else:
    print("Tháng vừa nhập không hợp lệ!")