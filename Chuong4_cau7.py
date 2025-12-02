import math

print("Tính độ dài đoạn AB")

try:
    xA = float(input("Nhập toạ độ xA: "))
    yA = float(input("Nhập toạ độ yA: "))

    xB = float(input("Nhập toạ độ xB: "))
    yB = float(input("Nhập toạ độ yB: "))

    
    do_dai_AB = math.sqrt(math.pow(xB - xA, 2) + math.pow(yB - yA, 2))
    
    print(f"Độ dài của đoạn thẳng AB là: {do_dai_AB}")

except ValueError:
    print("Lỗi: Vui lòng chỉ nhập số.")