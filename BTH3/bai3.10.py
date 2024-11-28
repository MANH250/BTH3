import math

def Tinh(R):
    if R <= 0:
        return "Bán kính phải là một số dương."
    
    chu_vi = 2 * math.pi * R
    dien_tich = math.pi * R**2
    
    return f"Chu vi hình tròn: {chu_vi}\nDiện tích hình tròn: {dien_tich}"

# Nhập bán kính từ bàn phím
try:
    R = float(input("Nhập bán kính hình tròn: "))
    ket_qua = Tinh(R)
    print(ket_qua)
except ValueError:
    print("Vui lòng nhập một số hợp lệ.")
