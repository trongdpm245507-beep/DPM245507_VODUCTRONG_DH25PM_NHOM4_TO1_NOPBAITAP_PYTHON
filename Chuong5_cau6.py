#Trả lời câu hỏi số 6 chương 5
import re

def NegativeNumberInStrings(s):
    cac_so_am = re.findall(r'-\d+', s)
    
    print(f"Các số nguyên âm tìm thấy trong chuỗi '{s}':")
    for so in cac_so_am:
        print(so)

input_str = "abc-5xyz-12k9l--p"
NegativeNumberInStrings(input_str)