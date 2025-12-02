import json
import os

filename = "sinhvien.json"

def nhap_sinh_vien():
    ma = input("Mã sinh viên: ")
    ten = input("Tên sinh viên: ")
    namsinh = input("Năm sinh: ")
    malop = input("Mã lớp: ")
    return {"ma": ma, "ten": ten, "namsinh": namsinh, "malop": malop}

def doc_file():
    if not os.path.exists(filename):
        return []
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

def luu_file(ds):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(ds, f, ensure_ascii=False, indent=4)

def hien_thi(ds):
    print(f"{'Mã SV':<10}{'Họ tên':<20}{'Năm sinh':<12}{'Mã lớp'}")
    for sv in ds:
        print(f"{sv['ma']:<10}{sv['ten']:<20}{sv['namsinh']:<12}{sv['malop']}")

def tim_kiem(ds, ma_tim):
    for sv in ds:
        if sv["ma"] == ma_tim:
            print("Tìm thấy:", sv)
            return
    print("Không tìm thấy sinh viên.")

# Menu
ds = doc_file()
while True:
    print("\n===== QUẢN LÝ SINH VIÊN =====")
    print("1. Thêm sinh viên")
    print("2. Xem danh sách")
    print("3. Tìm kiếm sinh viên theo mã")
    print("0. Thoát")
    chon = input("Chọn: ")
    if chon == "1":
        sv = nhap_sinh_vien()
        ds.append(sv)
        luu_file(ds)
    elif chon == "2":
        hien_thi(ds)
    elif chon == "3":
        ma = input("Nhập mã cần tìm: ")
        tim_kiem(ds, ma)
    elif chon == "0":
        break