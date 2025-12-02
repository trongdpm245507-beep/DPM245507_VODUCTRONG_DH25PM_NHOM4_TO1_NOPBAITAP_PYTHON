#Trả lời câu 6 chương 6
import random

def tao_list_ngau_nhien_khong_trung():
    n = int(input("Nhập số lượng phần tử N: "))
    lst = []
    while len(lst) < n:
        r = random.randint(1, 100) 
        if r not in lst: 
            lst.append(r)           
    print("List ngẫu nhiên không trùng:", lst)

tao_list_ngau_nhien_khong_trung()