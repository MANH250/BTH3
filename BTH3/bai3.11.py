import math

def benefit(t, n, k):
    # Chuyển lãi suất từ phần trăm sang thập phân
    monthly_rate = t / 100
    # Tính số tiền nhận được sau k tháng
    total_amount = n * (1 + monthly_rate) ** k
    return total_amount

# Nhập lãi suất, số vốn ban đầu và số tháng từ bàn phím
try:
    t = float(input("Nhập lãi suất tiết kiệm (%/tháng): "))
    n = float(input("Nhập số vốn ban đầu: "))
    k = int(input("Nhập số tháng gửi: "))
    
    # Kiểm tra tính hợp lệ của các giá trị đầu vào
    if t < 0 or n < 0 or k < 0:
        print("Vui lòng nhập các giá trị dương.")
    else:
        ket_qua = benefit(t, n, k)
        print(f"Số tiền nhận được sau {k} tháng là: {round(ket_qua, 2)}")
except ValueError:
    print("Vui lòng nhập các giá trị hợp lệ.")
