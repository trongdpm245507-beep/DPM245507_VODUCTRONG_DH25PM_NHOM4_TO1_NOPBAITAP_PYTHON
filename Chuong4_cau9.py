import math
def canbac2longnhau(x, n):
    result = x
    for _ in range(n):
        result = math.sqrt(result)
        return result
x = float(input("Nhập số x: "))
n = int(input("Nhập số n: "))
result = canbac2longnhau(x, n)
print(f"Kết quả căn bậc hai lồng nhau của", x, "với", n, "lần là:",result)