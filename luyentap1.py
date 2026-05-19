so_nguyen = 10
so_thuc = 3.5
chuoi = "Xin chao Python"
# n ra màn hình
print("=== BAI 1 ===")
print("So nguyen:", so_nguyen)
print("So thuc:", so_thuc)
print("Chuoi:", chuoi)
PI = 3.14
r = 5
chu_vi = 2 * PI * r
print("\n=== BAI 2 ===")
print("Chu vi hinh tron la:", chu_vi)
print("\n=== BAI 3 ===")
# Nhập dữ liệu từ bàn phím
a = int(input("Nhap so nguyen thu nhat: "))
b = int(input("Nhap so nguyen thu hai: "))
# Tính toán
tong = a + b
hieu = a - b
tich = a * b
# Kiểm tra chia cho 0
if b != 0:
    thuong = a / b
else:
    thuong = "Khong the chia cho 0"
# In kết quả
print("Tong =", tong)
print("Hieu =", hieu)
print("Tich =", tich)
print("Thuong =", thuong)
print("\n=== BAI 4 ===")
# Định nghĩa hàm
def sum_two_numbers(x, y):
    return x + y
# Gọi hàm
ket_qua = sum_two_numbers(5, 7)
print("Tong cua 2 so la:", ket_qua)
print("\n=== BAI 5 ===")
# Khai báo biến
name = "Nguyen Van A"
age = 20
average_score = 8.5
# Hiển thị kiểu dữ liệu
print("Kieu du lieu cua name:", type(name))
print("Kieu du lieu cua age:", type(age))
print("Kieu du lieu cua average_score:", type(average_score))
# Xử lý dữ liệu
age_next_year = age + 1
doubled_score = average_score * 2
# In thông tin
print("\nThong tin ca nhan:")
print("Ten:", name)
print("Tuoi:", age)
print("Diem trung binh:", average_score)
print("Tuoi nam sau:", age_next_year)
print("Diem trung binh nhan doi:", doubled_score)