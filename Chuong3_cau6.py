#Câu 6: Nhập một số n có tối đa 2 chữ số. Hãy cho biết cách đọc ra dạng chữ.
def doc_so(n):
    hang_donvi = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    hang_chuc = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi", "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]
    if n < 10:
        if n == 0:
            return "không"
        return hang_donvi[n]
    
    elif n < 20:
        if n == 10:
            return "mười"
        elif n == 15:
            return "mười lăm"
        else:
            return "mười " + hang_donvi[n % 10]
    
    else:
        chuc = n // 10
        dv = n % 10
        s = hang_donvi[chuc] + " mươi"
        if dv == 0:
            return s
        elif dv == 1:
            return s + " mốt"
        elif dv == 4:
            return s + " tư"
        elif dv == 5:
            return s + " lăm"
        else:
            return s + " " + hang_donvi[dv]
#===chạy thử === 
n = int(input("Nhập số n (0-99): "))
print(doc_so(n))