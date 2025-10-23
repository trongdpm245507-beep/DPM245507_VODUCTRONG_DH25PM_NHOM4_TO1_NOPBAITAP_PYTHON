#Câu 17: Viết lại coding dưới đây bằng cách dùng từ khóa break thay thế cho biến done
n, m = 0, 100
while n != m:
    n = int(input())
    if n < 0:
        break
    print("n =", n)