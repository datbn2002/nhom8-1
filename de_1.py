# Định nghĩa lớp tugiac
class tugiac:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def chuvi(self):
        return self.a + self.b + self.c + self.d

    def canhlon(self):
        m = self.a
        if m < self.b:
            m = self.b
        if m < self.c:
            m = self.c
        if m < self.d:
            m = self.d
        return m

from tkinter import *

ds = []

# Hàm để nhận dữ liệu từ người dùng
def nhapdulieu():
    c1 = canh1.get()
    c2 = canh2.get()
    c3 = canh3.get()
    c4 = canh4.get()
    obj = tugiac(c1, c2, c3, c4)
    ds.append(obj)

# Hàm để tính toán và hiển thị kết quả
def tinhtoan():
    s = []
    cv = []
    for i in range(0, len(ds)):
        stam = 'chu vi hình ' + str(i) + ': ' + str(ds[i].chuvi()) + ', độ dài cạnh lớn = ' + str(ds[i].canhlon())
        s.append(stam)
        cv.append(ds[i].chuvi())
    
    # Hiển thị kết quả trên các Label
    label2.config(text=s[0])
    label3.config(text=s[1])
    label4.config(text=s[2])
    s2 = 'Chu vi nhỏ nhất: ' + str(min(cv))
    label5.config(text=s2)

w = Tk()
w.geometry('300x400')
w.title('Bài tập số 1')

# Label và Entry để nhập dữ liệu
Label(w, text='Hãy nhập 4 cạnh:').pack()
canh1 = DoubleVar()
canh2 = DoubleVar()
canh3 = DoubleVar()
canh4 = DoubleVar()
Entry(w, textvariable=canh1).pack()
Entry(w, textvariable=canh2).pack()
Entry(w, textvariable=canh3).pack()
Entry(w, textvariable=canh4).pack()

# Button để thêm dữ liệu và tính toán
Button(w, text='Thêm dữ liệu', command=nhapdulieu).pack()
Button(w, text='Tính toán', command=tinhtoan).pack()

# Label để hiển thị kết quả
label2 = Label(w)
label3 = Label(w)
label4 = Label(w)
label5 = Label(w)

w.mainloop()
