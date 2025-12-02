import time

hinh_1 = """
    *
    * *
    * * *
* * * * * * 
* * *
* *
*
"""

hinh_2 = """
    *
    * *
    * * *
* * * * * * 
* * *
* *
*
"""

hinh_3 = """
        * * * *
        * * *
        * *
        *
      * *
    * * *
  * * * *
"""

hinh_4 = """
        * * * *
        *   *
        * *
        *
      * *
    *   *
  * * * *
"""

danh_sach_hinh = [hinh_1, hinh_2, hinh_3, hinh_4]

print("Bắt đầu vẽ hình...")

for index, hinh in enumerate(danh_sach_hinh):
    print(f"--- Hình thứ {index + 1} ---")
    print(hinh) #

    if index < len(danh_sach_hinh) - 1:
        print("Đang đợi 5 giây để xuất hiện hình tiếp theo...")
        time.sleep(5) 

print("Đã vẽ xong tất cả các hình!")