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


def cartoonify():
    pass


def save_image():
    pass
