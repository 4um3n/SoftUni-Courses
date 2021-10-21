from tkinter import Tk


def create_app():
    root = Tk()
    root.title("GUI Product shop")
    root.configure(bg='gray10')
    return root


tk = create_app()
