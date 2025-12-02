#Trả lời câu hỏi số 10 chương 6
def nhap_matrix(ten, rows, cols):
    print(f"--- Nhập ma trận {ten} ({rows}x{cols}) ---")
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            val = int(input(f"{ten}[{i}][{j}] = "))
            row.append(val)
        matrix.append(row)
    return matrix

def in_matrix(matrix):
    for row in matrix:
        print(row)

def matrix_hoan_vi(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    mt_hv = [[0 for _ in range(rows)] for _ in range(cols)]
    
    for i in range(rows):
        for j in range(cols):
            mt_hv[j][i] = matrix[i][j]
    return mt_hv

def main_matrix():
    r = int(input("Nhập số dòng: "))
    c = int(input("Nhập số cột: "))
    
    A = nhap_matrix("A", r, c)
    B = nhap_matrix("B", r, c)
    Tong = []
    for i in range(r):
        row = []
        for j in range(c):
            row.append(A[i][j] + B[i][j])
        Tong.append(row)
        
    print("\nTổng hai ma trận A + B:")
    in_matrix(Tong)
    print("\nMa trận hoán vị của A:")
    in_matrix(matrix_hoan_vi(A))
    
    print("\nMa trận hoán vị của B:")
    in_matrix(matrix_hoan_vi(B))

main_matrix()