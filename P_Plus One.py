def plus_one(digits):
    n = len(digits)
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        else:
            digits[i] = 0
    return[1] + digits

# Nhập số nguyên lớn từ người dùng dưới dạng mảng các chữ số
digits = list(map(int, input("Nhap so nguyen lon: ").split()))

# Gọi hàm plus_one để tăng số nguyên lớn và lưu kết quả vào biến result
result = plus_one(digits)
print("So nguyen lon sau khi tang: ", result)


