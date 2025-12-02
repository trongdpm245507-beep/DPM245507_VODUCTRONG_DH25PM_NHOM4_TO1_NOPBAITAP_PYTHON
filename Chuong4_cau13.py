# Trả lời câu hỏi số 13 chương 4
def tinh_tong_uoc_so(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0: 
            tong += i
    return tong

def kiem_tra_so_hoan_thien(n):
    tong_uoc = tinh_tong_uoc_so(n)
    
    if tong_uoc == n:
        return True
    else:
        return False 
def kiem_tra_so_thinh_vuong(n):
    tong_uoc = tinh_tong_uoc_so(n)
    if tong_uoc > n:
        return True 
    else:
        return False 

def main():
    n1 = 6
    if kiem_tra_so_hoan_thien(n1):
        print(f"{n1} là số hoàn thiện.")
    else:
        print(f"{n1} KHÔNG phải số hoàn thiện.")
    n2 = 12
    if kiem_tra_so_thinh_vuong(n2):
        print(f"{n2} là số thịnh vượng.")
    else:
        print(f"{n2} KHÔNG phải số thịnh vượng.")
main()