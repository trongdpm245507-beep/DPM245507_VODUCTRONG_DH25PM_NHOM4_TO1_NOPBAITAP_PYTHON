def BMI(height, weight):
    bmi = weight / (height ** 2)
    return bmi
def PhanLoai(bmi):
    if bmi < 18.5:
        return "Gầy"
    elif 18.5 <= bmi < 24.9:
        return "Bình thường"
    elif 25 <= bmi < 29.9:
        return "Hơi béo"
    elif 30 <= bmi < 34.9:
        return "Béo phì cấp độ 1"
    elif 35 <= bmi < 39.9:
        return "Béo phì cấp độ 2"
    else:
        return "Béo phì cấp độ 3"
def NguyCoBenh(bmi):
    if bmi < 18.5:
        return "Nguy cơ bệnh thấp"
    elif 18.5 <= bmi < 24.9:
        return "Nguy cơ bệnh trung bình"
    elif 25 <= bmi < 29.9:
        return "Nguy cơ bệnh cao"
    else:
        return "Nguy hiểm"
print("Nhap vao chieu cao (cm): ")
height = float(input())
print("Nhap vao can nang (kg): ")
weight = float(input())
bmi = BMI(height, weight)
print("BMI cua ban la = ", bmi)
print("Phan loai: ", PhanLoai(bmi))
print("Muc do nguy co benh: ", NguyCoBenh(bmi))