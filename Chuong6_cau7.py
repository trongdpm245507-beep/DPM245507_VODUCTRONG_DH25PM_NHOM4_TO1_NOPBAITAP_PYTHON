#Trả lời câu hỏi số 7 chương 6
def nhap_day_tang_dan():
    n = int(input("Nhập số lượng phần tử của dãy: "))
    lst = []
    
    print("Mời nhập số thứ 1: ")
    val = float(input())
    lst.append(val)
    
    for i in range(1, n):
        while True:
            val = float(input(f"Mời nhập số thứ {i+1} (phải >= {lst[i-1]}): "))
            if val >= lst[i-1]:
                lst.append(val)
                break
            else:
                print("Sai quy cách! Số nhập vào phải lớn hơn hoặc bằng số đứng trước.")
                
    print("Dãy số tăng dần đã nhập:", lst)

nhap_day_tang_dan()