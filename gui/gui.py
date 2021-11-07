import tkinter as tk

class Gui(tk.Tk):
    width = 1000
    height = 500
    
    def __init__(self):
        super().__init__()

        window_size = [
            self.width,
            self.height,
            int((self.winfo_screenwidth()/2) - (self.width/2)),
            int((self.winfo_screenheight()/2) - (self.height/2)),
        ]

        self.title('Cartoonify')
        self.configure(background='#DDBEBE')
        self.iconbitmap('resources/icon.ico')
        self.resizable(False, False)
        self.geometry("{}x{}+{}+{}".format(*window_size))

        self.mainloop()

if __name__ == "__main__":
    gui = Gui()
    gui.mainloop()
