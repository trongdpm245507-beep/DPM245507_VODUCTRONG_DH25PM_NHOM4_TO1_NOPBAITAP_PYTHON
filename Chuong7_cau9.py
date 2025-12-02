import os
filename = "sanpham.txt"

def nhap_san_pham():
    ma = input("Nhập mã sản phẩm: ")
    ten = input("Nhập tên sản phẩm: ")
    dongia = input("Nhập đơn giá: ")
    danhmuc = input("Nhập danh mục: ")
    return f"{ma};{ten};{dongia};{danhmuc}\n"

def luu_file(data):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(data)

def doc_file():
    if not os.path.exists(filename):
        print("Chưa có dữ liệu.")
        return
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            ma, ten, dongia, danhmuc = line.strip().split(";")
            print(f"{ma:<10}{ten:<20}{dongia:<10}{danhmuc}")

def tim_kiem(ma_tim):
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith(ma_tim + ";"):
                print("Tìm thấy:", line.strip())
                return
    print("Không tìm thấy sản phẩm.")

while True:
    print("\n===== QUẢN LÝ SẢN PHẨM =====")
    print("1. Thêm sản phẩm")
    print("2. Xem danh sách")
    print("3. Tìm kiếm sản phẩm theo mã")
    print("0. Thoát")
    chon = input("Chọn: ")
    if chon == "1":
        data = nhap_san_pham()
        luu_file(data)
    elif chon == "2":
        doc_file()
    elif chon == "3":
        ma_tim = input("Nhập mã cần tìm: ")
        tim_kiem(ma_tim)
    elif chon == "0":
        break