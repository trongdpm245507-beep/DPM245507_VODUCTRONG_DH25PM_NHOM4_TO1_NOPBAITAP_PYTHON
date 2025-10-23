#Câu 7: Nhập vào một ngày (ngày, tháng, năm). Tìm ngày kế sau ngày vừa nhập (ngày/tháng/năm).
import datetime

# Nhập ngày, tháng, năm
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

try:
    # Tạo đối tượng ngày
    ngay_hien_tai = datetime.date(nam, thang, ngay)
    # Cộng thêm 1 ngày
    ngay_ke_tiep = ngay_hien_tai + datetime.timedelta(days=1)
    
    # In kết quả
    print("Ngày kế tiếp là:", ngay_ke_tiep.strftime("%d/%m/%Y"))

except ValueError:
    print("Ngày không hợp lệ, vui lòng nhập lại!")