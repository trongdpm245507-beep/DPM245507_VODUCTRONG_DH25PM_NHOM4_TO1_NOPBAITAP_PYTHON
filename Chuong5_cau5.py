#Trả lời câu hỏi số 5 chương 5
def thong_ke_chuoi():
    s = input("Nhập vào một chuỗi bất kỳ: ")

    hoa = 0
    thuong = 0
    so = 0
    khoang_trang = 0
    nguyen_am = 0
    phu_am = 0
    ky_tu_dac_biet = 0

    list_nguyen_am = "ueoaiUEOAI"
    
    for char in s:

        if char.isupper():
            hoa += 1

        if char.islower():
            thuong += 1

        if char.isdigit():
            so += 1

        if char.isspace():
            khoang_trang += 1

        if char.isalpha(): 
            if char in list_nguyen_am:
                nguyen_am += 1
            else:
                phu_am += 1

        if not char.isalnum() and not char.isspace():
            ky_tu_dac_biet += 1

    print("-" * 20)
    print(f"Chữ in hoa: {hoa}")
    print(f"Chữ in thường: {thuong}")
    print(f"Chữ số: {so}")
    print(f"Ký tự đặc biệt: {ky_tu_dac_biet}")
    print(f"Khoảng trắng: {khoang_trang}")
    print(f"Nguyên âm: {nguyen_am}")
    print(f"Phụ âm: {phu_am}")

thong_ke_chuoi()