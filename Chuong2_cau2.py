# Câu 2: Tính giờ phút giây
t = int(input("Nhấp số giây: "))
hour=(t//3600)%24
minute = (t%3600)//60
second = (t%3600)%60
print(round(hour), ":",round(minute), ":",round(second))