import tkinter as tk
from tkinter import filedialog as fd
from PIL import ImageTk, Image

def open_image(self):
    filename = fd.askopenfilename(
        title='Choose an image',
        filetypes=(
            ('Image files', '*.png *.jpg'),
        ),
    )
    if not filename:
        return
    self.before_img = Image.open(filename)
    self.before_img_tk = ImageTk.PhotoImage(self.before_img)
    self.before_canvas.create_image(
        0,
        0,
        image=self.before_img_tk,
        anchor='center'
    )
    self.opened = True
    self.cartoonified = False


def cartoonify(self):
    # TODO add generating
    if not self.opened:
        tk.messagebox.showerror(
            title='No image opened', 
            message='To generate the image it needs to be opened first',
        )
        return
    self.after_img = self.before_img
    self.after_img_tk = ImageTk.PhotoImage(self.after_img)
    self.after_canvas.create_image(
        0,
        0,
        image=self.after_img_tk,
        anchor='center'
    )
    self.cartoonified = True


def save_image(self):
    if not self.cartoonified:
        tk.messagebox.showerror(
            title='No image generated', 
            message='To save the image it needs to be generated first',
        )
        return
    filename = fd.asksaveasfile(
        title='Choose an image',
        filetypes=(
            ('Image files', '*.jpg'),
        ),
        mode='w', 
        defaultextension='*.jpg',
    )
    if not filename:
        return
    self.after_img.save(filename)
