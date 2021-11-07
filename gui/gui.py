import tkinter as tk
from commands import open_image, cartoonify
from PIL import ImageTk, Image

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

        # canvases
        self.before_canvas = tk.Canvas(
            self,
            bg='#C89595',
            width=0.3*self.width,
            height=0.3*self.width,
        )  
        self.before_canvas.place(
            relx=0.05,
            rely=0.2,
        )

        self.after_canvas = tk.Canvas(
            self,
            bg='#C89595',
            width=0.3*self.width,
            height=0.3*self.width,
        )  
        self.after_canvas.place(
            relx=0.65,
            rely=0.2,
        )


        # labels
        self.arrow_img = ImageTk.PhotoImage(Image.open(
            r'resources\arrow.png').resize((int(0.2*self.width), int(0.1*self.width)))
        )
        self.arrow_label = tk.Label(
            self,
            bg='#DDBEBE',
            image=self.arrow_img,
        )
        self.arrow_label.place(
            relx=0.4,
            rely=0.4,
        )


        # buttons
        self.open_button = tk.Button(
            self,
            bg='#6C4A4A',
            fg='#EDEDED',
            font='Helvetica 12 bold',
            text='Open an image',
            command=lambda: open_image(self),
        )
        self.open_button.place(
            relx=0.125,
            rely=0.85,
            relheight=0.07,
            relwidth=0.15,
        )

        self.cartoon_button = tk.Button(
            self,
            bg='#6C4A4A',
            fg='#EDEDED',
            font='Helvetica 12 bold',
            text='Cartoonify',
            command=lambda: cartoonify(self),
        )
        self.cartoon_button.place(
            relx=0.425,
            rely=0.7,
            relheight=0.07,
            relwidth=0.15,
        )

        self.mainloop()


if __name__ == "__main__":
    gui = Gui()
    gui.mainloop()
