import random
import tkinter as tk
from tkinter import messagebox

def xoc_dia():
    ket_qua = [random.choice(["Chẵn", "Lẻ"]) for _ in range(4)]
    so_chan = ket_qua.count("Chẵn")
    so_le = ket_qua.count("Lẻ")
    
    if so_chan in [0, 2, 4]:
        ket_qua_cuoi = "Chẵn"
    else:
        ket_qua_cuoi = "Lẻ"
    
    messagebox.showinfo("Kết Quả Xóc Đĩa", f"Kết quả: {ket_qua} \n Tổng kết: {ket_qua_cuoi}")

def dat_cuoc():
    messagebox.showinfo("Đặt Cược", "Bạn đã đặt cược tất cả!")

def huy_cuoc():
    messagebox.showinfo("Hủy Cược", "Bạn đã hủy cược!")

# Tạo giao diện
root = tk.Tk()
root.title("Anh Bi - Xóc Đĩa")
root.geometry("300x250")

tk.Label(root, text="Chào mừng đến với trò chơi Xóc Đĩa Anh Bi!", wraplength=280).pack(pady=10)
btn_xoc = tk.Button(root, text="Xóc Đĩa", command=xoc_dia, font=("Arial", 14), bg="green", fg="white")
btn_xoc.pack(pady=10)

btn_dat_cuoc = tk.Button(root, text="All Đặt Cược", command=dat_cuoc, font=("Arial", 12), bg="blue", fg="white")
btn_dat_cuoc.pack(pady=5)

btn_huy_cuoc = tk.Button(root, text="Hủy Cược", command=huy_cuoc, font=("Arial", 12), bg="red", fg="white")
btn_huy_cuoc.pack(pady=5)

root.mainloop()
