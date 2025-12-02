#Trả lời câu hỏi số 7 chương 5
def toi_uu_chuoi():
    s = "    TRần    duY            thAnH   "
    print(f"Chuỗi ban đầu: '{s}'")
    s_sach = " ".join(s.split())
    s_hoan_thien = s_sach.title()   
    print(f"Output: '{s_hoan_thien}'")
toi_uu_chuoi()