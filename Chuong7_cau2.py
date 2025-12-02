import os

DB_PATH = "csdl_so.txt"
def luu_file(path, data_line: str):
    """Ghi 1 dòng vào file (giữ nguyên, thêm \n)."""
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "a", encoding="utf-8") as f:
        f.write(data_line.strip() + "\n")

def doc_file(path):
    """Đọc file -> trả về list[list[str]] (các phần tử là chuỗi số)."""
    arrSo = []
    if not os.path.exists(path):
        return arrSo
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            data = line.strip()
            if not data:
                continue
            arr = data.split(',')
            arrSo.append(arr)
    return arrSo

def tao_du_lieu_mau():
    mau = [
        "5,-4,7,9,3,20",
        "5,-4,37,-19,24,-21",
        "15,9,0,-38,-3,15",
        "5,-4,77,-9,3,-7",
        "55,44,27",
        "-50,26",
    ]
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    for line in mau:
        luu_file(DB_PATH, line)
    print("✔ Đã tạo dữ liệu mẫu vào", DB_PATH, "\n")

def nhap_them_1_dong():
    s = input("Nhập 1 dòng số (phân tách bằng dấu phẩy, ví dụ: 1,-3,5,0): ").strip()
    if s:
        luu_file(DB_PATH, s)
        print("✔ Đã lưu.\n")

def in_list_tung_dong(arrSo):
    print("Các dòng sau khi tách thành list:")
    for row in arrSo:
        nums = [int(x) for x in row]
        print(nums)
    print()

def xuat_so_am_tren_moi_dong(arrSo):
    print("Các số âm trên mỗi dòng:")
    for row in arrSo:
        nums = [int(x) for x in row]
        am = [n for n in nums if n < 0]
        if am:
            for n in am:
                print(n, end="\t")
        else:
            print("(không có)", end="")
        print()
    print()

def main():
    while True:
        print("=== XỬ LÝ SỐ TRONG TEXT FILE ===")
        print("1. Tạo dữ liệu mẫu")
        print("2. Nhập thêm 1 dòng số vào file")
        print("3. Đọc file và in từng dòng (list)")
        print("4. Đọc file và in các số âm trên mỗi dòng")
        print("0. Thoát")
        chon = input("Chọn: ").strip()
        print()

        if chon == "1":
            tao_du_lieu_mau()
        elif chon == "2":
            nhap_them_1_dong()
        elif chon == "3":
            arrSo = doc_file(DB_PATH)
            in_list_tung_dong(arrSo)
        elif chon == "4":
            arrSo = doc_file(DB_PATH)
            xuat_so_am_tren_moi_dong(arrSo)
        elif chon == "0":
            break
        else:
            print("Lựa chọn không hợp lệ!\n")

if __name__ == "__main__":
    main()