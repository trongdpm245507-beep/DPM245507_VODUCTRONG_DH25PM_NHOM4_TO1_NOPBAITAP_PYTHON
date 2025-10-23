#Câu 12: Xuất bảng cửu chương
for i in range(2, 10):  # Duyệt từ 2 đến 9
    print(f"\n🔹 Bảng cửu chương {i}:")
    for j in range(1, 11):  # Mỗi bảng nhân từ 1 đến 10
        print(f"{i} x {j} = {i * j}")