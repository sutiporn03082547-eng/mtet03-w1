import tkinter as tk

def button_click(char):
    if char == '=':
        try:
            display_var.set(str(eval(display_var.get())))
        except:
            display_var.set("Error")
    elif char == 'C':
        display_var.set("")
    else:
        display_var.set(display_var.get() + str(char))

# ตั้งค่าหน้าต่างโปรแกรม
root = tk.Tk()
root.title("Purple Calculator")
root.configure(bg="#F3E8FF") # พื้นหลังสีม่วงพาสเทล

# หน้าจอแสดงผล
display_var = tk.StringVar()
display = tk.Entry(root, textvariable=display_var, font=('Arial', 24, 'bold'), 
                   bg="#E9D5FF", fg="#4C1D95", bd=0, justify="right")
display.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15, pady=15, padx=10)

# ปุ่มกดต่างๆ
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row_val = 1
col_val = 0

for btn in buttons:
    # แยกสีปุ่มตัวเลขกับปุ่มเครื่องหมายให้ดูสวยงาม
    bg_color = "#C084FC" if btn not in ['=', 'C', '/', '*', '-', '+'] else "#9333EA"
    
    tk.Button(root, text=btn, font=('Arial', 18), bg=bg_color, fg="white", 
              activebackground="#7E22CE", activeforeground="white", bd=0, width=4, height=2,
              command=lambda b=btn: button_click(b)).grid(row=row_val, column=col_val, padx=5, pady=5)
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()