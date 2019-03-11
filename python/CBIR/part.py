import tkinter as tk
from PIL import ImageTk, Image


LARGE_FONT= ("Verdana", 12)


class CBIRUI(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageTest, PageTrain,PageAdd):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        file = 'CBIR.png'
        px = 20
        py = 10
        fnt = "Verdana 14 bold"

        logo = ImageTk.PhotoImage(Image.open(file))
        w1 = tk.Label(self, image=logo,compound = tk.CENTER)
        w1.image = logo
        w1.pack(pady=10,padx=10)
        
        bt1 = tk.Button(self, 
              compound=tk.CENTER,
              padx = px,
              pady=py, 
              font = fnt,
              command=lambda: controller.show_frame(PageTrain),
              text='Train').pack(side="left")
        
        bt2 = tk.Button(self, 
              compound=tk.CENTER,
              padx = px,
              pady=py, 
              font = fnt,
              text='Add').pack(side="left")
        
        bt3 = tk.Button(self, 
              compound=tk.CENTER,
              padx = px,
              pady=py, 
              font = fnt,
              text='Test').pack(side="left")
        
        bt4 = tk.Button(self, 
              compound=tk.BOTTOM,
              padx = px,
              pady=py, 
              font = fnt,
              text='Exit', command=controller.destroy).pack(side="right")


class PageTrain(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label = tk.Label(self, text="Page Train!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTest))
        button2.pack()


class PageTest(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Test!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageTrain))
        button2.pack()
        
class PageAdd(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Add!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageTrain))
        button2.pack()
        

app = CBIRUI()
app.mainloop()
