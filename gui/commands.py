import tkinter as tk
from tkinter import filedialog as fd
import math
import numpy as np
from PIL import ImageTk, Image
import tensorflow as tf

def open_image(self):
    filename = fd.askopenfilename(
        title='Choose an image',
        filetypes=(
            ('Image files', '*.png *.jpg'),
        ),
    )
    if not filename:
        return
    self.before_img = Image.open(filename).resize((math.ceil(0.3*self.width), math.ceil(0.3*self.width)))
    self.before_img_tk = ImageTk.PhotoImage(self.before_img)
    self.before_canvas.create_image(
        math.ceil(0.3*self.width)/2+2,
        math.ceil(0.3*self.width)/2+2,
        image=self.before_img_tk,
        anchor='center'
    )
    self.after_canvas.delete("all") 
    self.opened = True
    self.cartoonified = False


def cartoonify(self):
    if not self.opened:
        tk.messagebox.showerror(
            title='No image opened', 
            message='To generate the image it needs to be opened first',
        )
        return
    self.after_img = generate(self.before_img)
    self.after_img_tk = ImageTk.PhotoImage(self.after_img)
    self.after_canvas.create_image(
        math.ceil(0.3*self.width)/2+2,
        math.ceil(0.3*self.width)/2+2,
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


def generate(img_in):
    model = tf.saved_model.load(r'resources\saved_model')
    f = model.signatures["serving_default"]
    img = np.array(img_in.convert("RGB"))
    img = np.expand_dims(img, 0).astype(np.float32) / 127.5 - 1
    img_out = f(tf.constant(img))['output_1']
    img_out = ((img_out.numpy().squeeze() + 1) * 127.5).astype(np.uint8)
    return Image.fromarray(img_out)
