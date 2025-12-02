import csv
import random
from pathlib import Path

FILENAME = "random10x10.csv"

def write_csv_random(filename=FILENAME, rows=10, cols=10, low=0, high=100):
    """Ghi file CSV: rows dòng × cols số ngẫu nhiên, phân tách ';'."""
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=';', quoting=csv.QUOTE_NONE)
        for _ in range(rows):
            row = [random.randint(low, high) for _ in range(cols)]
            writer.writerow(row)
    print(f"✔ Đã tạo file: {Path(filename).resolve()}")

def read_and_sum(filename=FILENAME):
    """Đọc file CSV và in tổng từng dòng."""
    print("\n=== Tổng mỗi dòng ===")
    with open(filename, newline="", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=';')
        for i, row in enumerate(reader, start=1):
            nums = [int(x) for x in row if x != ""]
            s = sum(nums)
            print(f"Dòng {i:>2}: {nums}  ->  Tổng = {s}")

if __name__ == "__main__":
    write_csv_random()

    read_and_sum()