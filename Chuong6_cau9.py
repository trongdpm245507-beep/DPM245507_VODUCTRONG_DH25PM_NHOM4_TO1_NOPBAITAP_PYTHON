#Trả lời câu hỏi số 9 chương 6
import math
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def xu_ly_mang():
    input_str = input("Nhập các số tự nhiên cách nhau bởi dấu cách: ")
    M = [int(x) for x in input_str.split()]
    le = []
    chan = []
    nguyen_to = []
    khong_nguyen_to = []
    
    for x in M:
        if x % 2 != 0:
            le.append(x)
        else:
            chan.append(x)
        if is_prime(x):
            nguyen_to.append(x)
        else:
            khong_nguyen_to.append(x)
    print(f"Dòng 1: Các số lẻ: {le} -> Tổng cộng: {len(le)} số.")
    print(f"Dòng 2: Các số chẵn: {chan} -> Tổng cộng: {len(chan)} số.")
    print(f"Dòng 3: Các số nguyên tố: {nguyen_to}")
    print(f"Dòng 4: Các số không phải nguyên tố: {khong_nguyen_to}")

xu_ly_mang()