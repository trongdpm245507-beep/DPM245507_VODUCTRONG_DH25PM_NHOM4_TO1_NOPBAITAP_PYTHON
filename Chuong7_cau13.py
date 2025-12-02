from xml.dom.minidom import parse

def doc_nhomthietbi():
    nhoms = []
    tree = parse("nhomthietbi.xml")
    root = tree.documentElement
    for n in root.getElementsByTagName("nhom"):
        ma = n.getElementsByTagName("ma")[0].childNodes[0].data
        ten = n.getElementsByTagName("ten")[0].childNodes[0].data
        nhoms.append({"ma": ma, "ten": ten})
    return nhoms

def doc_thietbi():
    tb_list = []
    tree = parse("ThietBi.xml")
    root = tree.documentElement
    for tb in root.getElementsByTagName("thietbi"):
        manhom = tb.getAttribute("manhom")
        ma = tb.getElementsByTagName("ma")[0].childNodes[0].data
        ten = tb.getElementsByTagName("ten")[0].childNodes[0].data
        tb_list.append({"manhom": manhom, "ma": ma, "ten": ten})
    return tb_list


def hien_thi_nhom(nhoms):
    print("\n=== DANH SÁCH NHÓM THIẾT BỊ ===")
    for n in nhoms:
        print(f"{n['ma']:>5}  -  {n['ten']}")

def hien_thi_thietbi(tb_list):
    print("\n=== DANH SÁCH THIẾT BỊ ===")
    for tb in tb_list:
        print(f"{tb['ma']:<6} {tb['ten']:<15} (Nhóm: {tb['manhom']})")

def loc_theo_nhom(tb_list, ma_nhom):
    print(f"\n=== THIẾT BỊ TRONG NHÓM {ma_nhom} ===")
    found = False
    for tb in tb_list:
        if tb["manhom"] == ma_nhom:
            print(f"{tb['ma']:<6} {tb['ten']}")
            found = True
    if not found:
        print("→ Không có thiết bị nào trong nhóm này.")

def nhom_co_nhieu_tb_nhat(tb_list, nhoms):
    dem = {}
    for tb in tb_list:
        dem[tb["manhom"]] = dem.get(tb["manhom"], 0) + 1
    max_count = max(dem.values())
    print("\n=== NHÓM CÓ SỐ LƯỢNG THIẾT BỊ NHIỀU NHẤT ===")
    for ma, so in dem.items():
        if so == max_count:
            ten = next((n["ten"] for n in nhoms if n["ma"] == ma), ma)
            print(f"{ten} ({ma})  →  {so} thiết bị")

if __name__ == "__main__":
    nhoms = doc_nhomthietbi()
    thietbis = doc_thietbi()

    while True:
        print("\n===== QUẢN LÝ THIẾT BỊ =====")
        print("1. Hiển thị danh sách Nhóm thiết bị")
        print("2. Hiển thị toàn bộ Thiết bị")
        print("3. Lọc thiết bị theo Mã nhóm")
        print("4. Xuất nhóm có nhiều thiết bị nhất")
        print("0. Thoát")
        chon = input("Chọn: ")

        if chon == "1":
            hien_thi_nhom(nhoms)
        elif chon == "2":
            hien_thi_thietbi(thietbis)
        elif chon == "3":
            ma = input("Nhập mã nhóm (vd: n1, n2, n3): ")
            loc_theo_nhom(thietbis, ma)
        elif chon == "4":
            nhom_co_nhieu_tb_nhat(thietbis, nhoms)
        elif chon == "0":
            break
        else:
            print("❌ Lựa chọn không hợp lệ!")