import os
DB_PATH = "database.txt"
def luu_file(path, data_line):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "a", encoding="utf-8") as f:
        f.write(data_line.strip() + "\n")

def doc_file(path):
    arr = []
    if not os.path.exists(path):
        return arr
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(";")
            if len(parts) != 3:
                continue
            masp, tensp, dongia = parts[0], parts[1], parts[2]
            try:
                dongia = float(dongia)
            except ValueError:
                continue
            arr.append([masp, tensp, dongia])
    return arr

def xuat_ds(dssp, title=None):
    if title:
        print(title)
    if not dssp:
        print("(Danh sách rỗng)")
        return
    print(f"{'Mã SP':<10} {'Tên sản phẩm':<25} {'Đơn giá':>10}")
    print("-" * 50)
    for masp, tensp, dongia in dssp:
        print(f"{masp:<10} {tensp:<25} {dongia:>10.2f}")
    print()

def sort_giam_theo_gia(dssp):
    dssp.sort(key=lambda row: row[2], reverse=True)

def chuc_nang_them():
    masp = input("Nhập mã SP: ").strip()
    tensp = input("Nhập tên SP: ").strip()
    while True:
        try:
            dongia = float(input("Nhập đơn giá: "))
            break
        except ValueError:
            print("Đơn giá không hợp lệ, mời nhập lại!")
    line = f"{masp};{tensp};{dongia}"
    luu_file(DB_PATH, line)
    print("✔ Đã lưu sản phẩm vào file.\n")

def chuc_nang_xem():
    dssp = doc_file(DB_PATH)
    xuat_ds(dssp, "Danh sách sản phẩm:")

def chuc_nang_sap_xep_giam():
    dssp = doc_file(DB_PATH)
    sort_giam_theo_gia(dssp)
    xuat_ds(dssp, "Sản phẩm sau khi sắp xếp giá (giảm dần):")

def chuc_nang_xoa_file():
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
        print("✔ Đã xoá database.txt\n")
    else:
        print("File chưa tồn tại.\n")
def menu():
    while True:
        print("===== QUẢN LÝ SẢN PHẨM (Text File) =====")
        print("1. Thêm sản phẩm (lưu vào file)")
        print("2. Xem danh sách sản phẩm")
        print("3. Sắp xếp theo đơn giá giảm dần và in")
        print("4. (Tùy chọn) Xoá file dữ liệu")
        print("0. Thoát")
        chon = input("Chọn: ").strip()
        print()

        if chon == "1":
            chuc_nang_them()
        elif chon == "2":
            chuc_nang_xem()
        elif chon == "3":
            chuc_nang_sap_xep_giam()
        elif chon == "4":
            chuc_nang_xoa_file()
        elif chon == "0":
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ!\n")

if __name__ == "__main__":
    menu()