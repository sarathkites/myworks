import tkinter as tk

root = tk.Tk()
root.title("C B I R")
logo = tk.PhotoImage(file="python-logo.png")

w1 = tk.Label(root, image=logo,compound = tk.CENTER).pack(side="top")



bt1 = tk.Button(root, 
              compound=tk.CENTER,
              padx = 75,
              pady=20, 
              font = "Verdana 18 bold",
              text='Train').pack(side="left")
bt2 = tk.Button(root, 
              compound=tk.CENTER,
              padx = 75, 
              pady=20, 
              font = "Verdana 18 bold",
              text='Add').pack(side="left")
bt3 = tk.Button(root, 
              compound=tk.CENTER,
              padx = 75, 
              pady=20, 
              font = "Verdana 18 bold",
              text='Test').pack(side="left")
bt4 = tk.Button(root, 
              compound=tk.BOTTOM,
              padx = 75, 
              pady=20, 
              font = "Verdana 18 bold",
              text='Exit', command=root.destroy).pack(side="right")

root.mainloop()
