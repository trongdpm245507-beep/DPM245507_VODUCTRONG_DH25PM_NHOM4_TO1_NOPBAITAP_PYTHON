#Trả lời câu hỏi số 8 chương 6
def sap_xep_giam_dan():
    n = int(input("Nhập số lượng phần tử N: "))
    M = []   
    for i in range(n):
        val = float(input(f"Nhập phần tử M[{i}]: "))
        M.append(val)
    M.sort(reverse=True)    
    print("Dãy số sau khi sắp xếp giảm dần:", M)
sap_xep_giam_dan()