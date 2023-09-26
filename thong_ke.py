import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ tệp CSV và đặt cột đầu tiên là cột chỉ mục
df = pd.read_csv('diemPython.csv', index_col=0, header=0)

# Lấy tất cả dữ liệu từ DataFrame thành một mảng NumPy
data = df.values

# In dữ liệu
print(data)

# Tính tổng số sinh viên tham gia thi
tong_sinh_vien = data[:, 1].sum()
print(f'Tổng số sinh viên dự thi: {tong_sinh_vien}')

# Tính điểm cao nhất của lớp và số sinh viên đạt điểm A
diem_A = data[:, 3]
diem_Bc = data[:, 4]
max_diem_A = diem_A.max()
lop_max_diem_A = df.index[diem_A.argmax()]
so_sv_dat_diem_A = (diem_A == max_diem_A).sum()
print(f'Lớp có nhiều điểm A nhất là {lop_max_diem_A} với {so_sv_dat_diem_A} sinh viên đạt điểm A.')

# Vẽ biểu đồ
plt.plot(range(len(diem_A)), diem_A, 'r-', label="Diem A")
plt.plot(range(len(diem_Bc)), diem_Bc, 'g-', label="Diem B +")
plt.xlabel('Lớp')
plt.ylabel('Số sinh viên đạt điểm')
plt.legend(loc='upper right')
plt.show()
