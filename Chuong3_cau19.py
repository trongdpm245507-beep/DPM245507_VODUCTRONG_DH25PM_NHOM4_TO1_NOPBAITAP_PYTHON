#Câu 19: Tính giá trị biểu thức S
import math

# Nhập giá trị x và n
x = float(input("Nhập x: "))
n = int(input("Nhập n: "))

S = 0
for i in range(n + 1):
    tu_so = x ** (2 * i + 1)
    mau_so = math.factorial(2 * i + 1)
    S += tu_so / mau_so

print("Giá trị của S(x, n) =", S)