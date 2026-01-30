import tkinter as tk
from time import strftime
def update_time():
    string = strftime('%H:%M:%S %p')
    clock_label.config(text=string)
    clock_label.after(1000, update_time)
root = tk.Tk()
root.title("Digital Clock")
clock_label = tk.Label(
    root,
    font=('calibri', 60, 'bold'), 
    background='black',         
    foreground='cyan'            
)
clock_label.pack(anchor='center', padx=20, pady=20)
update_time()
root.mainloop()