# Chương trình máy tính thực hiện các phép tính đơn giản
# Program make a simple calculator that can add, subtract, multiply and divide using functions

# Hàm cộng hai số
def add(x, y):
    return x + y

# Hàm trừ hai số
def subtract(x, y):
    return x - y

# Hàm nhân hai số
def multiply(x, y):
    return x * y

# Hàm chia hai số
def divide(x, y):
    return x / y

print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Nhập lựa chọn từ người dùng
choice = input("Enter choice (1/2/3/4): ")

# Nhập hai số từ người dùng
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Thực hiện phép tính dựa trên lựa chọn của người dùng
if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Invalid input")
