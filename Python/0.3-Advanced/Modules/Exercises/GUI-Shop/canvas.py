from tkinter import *
from PIL import Image, ImageTk


def create_app():
    root = Tk()
    root.title('Cashier Program')
    root.configure(bg='gray10')
    root.geometry('1600x899+0+0')
    return root


def clear_screen(root):
    for slave in root.grid_slaves():
        slave.destroy()


def get_image(root, product_img_path):
    load = Image.open(product_img_path)
    crop = load.crop((0, 0, 200, 200))
    render = ImageTk.PhotoImage(crop)
    img = Label(root, image=render, bd=0)
    img.image = render
    return img
