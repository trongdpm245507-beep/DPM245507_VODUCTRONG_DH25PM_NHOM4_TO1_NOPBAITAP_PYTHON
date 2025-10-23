#Câu 18: Vẽ các hình dưới đây
# Nhập chiều cao
n = int(input("Nhập chiều cao n: "))

print("Hình vuông:")
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()

print("\nHình tam giác vuông (vuông dưới trái):")
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()

print("\nHình tam giác vuông (vuông trên trái):")
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()