try:
    a = int(input('Nhập số a: '))
    b = int(input('Nhập số b: '))
    print('Tổng =', a + b)
    print('Hiệu =', a - b)
    print('Tích =', a * b)
    
    if b == 0:
        print('Không thể chia cho 0.')
    else:
        print('Thương =', a / b)
except ValueError:
    print('Dữ liệu nhập không hợp lệ. Hãy nhập số nguyên.')
except ZeroDivisionError:
    print('Không thể chia cho 0.')
finally:
    print('Kết thúc chương trình!')
