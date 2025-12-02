#Trả lời câu 8 chương 5
def lay_ten_co_duoi(path):
    vi_tri_slash = path.rfind('\\')
    if vi_tri_slash != -1:
        ten_file = path[vi_tri_slash + 1 : ]
    else:
        ten_file = path
    return ten_file

def lay_ten_khong_duoi(path):
    ten_co_duoi = lay_ten_co_duoi(path)
    vi_tri_dot = ten_co_duoi.rfind('.')
    if vi_tri_dot != -1:
        ten_khong_duoi = ten_co_duoi[ : vi_tri_dot]
    else:
        ten_khong_duoi = ten_co_duoi
    return ten_khong_duoi

duong_dan = r"d:\music\muabui.mp3"
print(f"Đường dẫn: {duong_dan}")
print(f"Tên có đuôi: {lay_ten_co_duoi(duong_dan)}")
print(f"Tên không đuôi: {lay_ten_khong_duoi(duong_dan)}")