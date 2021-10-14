from tkinter import *
from products import *
from authentication import *
from PIL import Image, ImageTk


def clear_screen(root):
    for slave in root.grid_slaves():
        slave.destroy()


def render_main_screen(root):
    clear_screen(root)
    root.geometry("600x200+0+0")

    login_button = Button(root, text=f"Login", command=lambda: render_login_screen(root))
    login_button.configure(activebackground='maroon4', activeforeground='snow2',
                           bg='orchid4', fg='white', width=14, height=2, bd=0)
    login_button.grid(column=0, row=0, padx=5)

    register_button = Button(root, text=f"Register", command=lambda: render_register_screen(root))

    register_button.configure(activebackground='purple4', activeforeground='snow2',
                              bg='purple3', fg='white', width=14, height=2, bd=0)
    register_button.grid(column=1, row=0, padx=5)

    exit_button = Button(root, text=f"Exit", command=lambda: exit())
    exit_button.configure(activebackground='brown4', activeforeground='snow2',
                          bg='brown3', fg='white', width=14, height=2, bd=0)
    exit_button.grid(column=2, row=0, padx=5)


def login(root, username, password):
    if login_validator(username, password):
        render_products_screen(root, username)
        return
    
    render_login_screen(root, error='Wrong username or password!')


def render_login_screen(root, error=None):
    clear_screen(root)
    root.geometry("600x200+0+0")

    Label(root, text=f"Enter username: ", bg='gray10', fg='snow2').grid(column=0, row=0)
    username = StringVar()
    username_entry = Entry(root, textvariable=username)
    username_entry.configure(bg='gray10', fg='snow2', bd=0)
    username_entry.grid(column=1, row=0)

    Label(root, text=f"Enter password:", bg='gray10', fg='snow2').grid(column=0, row=1)
    password = StringVar()
    password_entry = Entry(root, textvariable=password, show='*')
    password_entry.configure(bg='gray10', fg='snow2', bd=0)
    password_entry.grid(column=1, row=1)

    login_button = Button(root, text='Login', command=lambda: login(root, username.get(), password.get()))
    login_button.configure(activebackground='maroon4', activeforeground='snow2', bg='orchid4', fg='white', bd=0)
    login_button.grid(column=0, row=2, padx=14, pady=5)

    back_button = Button(root, text='Back', command=lambda: render_main_screen(root))
    back_button.configure(activebackground='brown4', activeforeground='snow2', bg='brown3', fg='white', bd=0)
    back_button.grid(column=1, row=2, padx=14, pady=5)

    if error is not None:
        Label(root, text=f"{error}", bg='gray10', fg='IndianRed2').grid(column=3, row=2)


def register(root, user):
    error = register_validator(**user)
    if error:
        render_register_screen(root, error)
        return

    render_login_screen(root)


def render_register_screen(root, error=None):
    clear_screen(root)
    root.geometry("600x200+0+0")

    Label(root, text=f"Enter username:", bg='gray10', fg='snow2').grid(column=0, row=0)
    username = StringVar()
    username_entry = Entry(root, textvariable=username)
    username_entry.configure(bg='gray10', fg='snow2', bd=0)
    username_entry.grid(column=1, row=0, pady=1)

    Label(root, text=f"Enter password:", bg='gray10', fg='snow2').grid(column=0, row=1)
    password = StringVar()
    password_entry = Entry(root, textvariable=password)
    password_entry.configure(bg='gray10', fg='snow2', bd=0)
    password_entry.grid(column=1, row=1, pady=1)

    Label(root, text=f"Enter your first name:", bg='gray10', fg='snow2').grid(column=0, row=2)
    first_name = StringVar()
    first_name_entry = Entry(root, textvariable=first_name)
    first_name_entry.configure(bg='gray10', fg='snow2', bd=0)
    first_name_entry.grid(column=1, row=2, pady=1)

    Label(root, text=f"Enter your last name:", bg='gray10', fg='snow2').grid(column=0, row=3)
    last_name = StringVar()
    last_name_entry = Entry(root, textvariable=last_name)
    last_name_entry.configure(bg='gray10', fg='snow2', bd=0)
    last_name_entry.grid(column=1, row=3, pady=1)

    Label(root, text=f"Is this user an admin?", bg='gray10', fg='snow2').grid(column=0, row=4, pady=3)
    is_admin = BooleanVar()
    check_button = Checkbutton(root, variable=is_admin)
    check_button.configure(bg='gray10', fg='black', activebackground='gray10', activeforeground='black')
    check_button.grid(column=1, row=4, sticky=W+E)

    user = {
        'username': username,
        'password': password,
        'first_name': first_name,
        'last_name': last_name,
        'is_admin': is_admin
    }

    register_button = Button(root, text=f"Register", command=lambda: register(root, user))
    register_button.configure(activebackground='purple4', activeforeground='snow2', bg='purple3', fg='white', bd=0)
    register_button.grid(column=0, row=5, pady=5)

    back_button = Button(root, text=f"Back", command=lambda: render_main_screen(root))
    back_button.configure(activebackground='brown4', activeforeground='snow2', bg='brown3', fg='white', bd=0)
    back_button.grid(column=1, row=5, pady=5)

    if error is not None:
        Label(root, text=f"{error}", bg='gray10', fg='IndianRed2').grid(column=2, row=0, rowspan=4, padx=5)


def reduce_product(root, current_user, product_id):
    error_id = reduce_product_quantity(product_id)
    if error_id:
        render_products_screen(root, current_user, error_id)
        return

    add_product_to_user_products(current_user, product_id)
    render_products_screen(root, current_user)


def render_products_screen(root, current_user, error_id=None):
    clear_screen(root)
    root.geometry("1600x899+0+0")

    r, c = 2, 0
    products = get_products_content()
    for product in products:
        product_id = product.get('id')
        product_name = product.get('name')
        product_img_path = product.get('img_path')
        product_count = product.get('quantity')

        load = Image.open(product_img_path)
        crop = load.crop((0, 0, 200, 200))
        render = ImageTk.PhotoImage(crop)
        img = Label(root, image=render, bd=0)
        img.image = render

        Label(root, text=f"{product_name}", bg='grey10', fg='snow2').grid(column=c, row=r-2, pady=5)
        Label(root, text=f"Quantity: {product_count}", bg='grey10', fg='snow2').grid(column=c, row=r-1, pady=5)
        img.grid(column=c, row=r)

        buy_button = Button(root, text=f"Buy {product_name}")
        buy_button.configure(command=lambda pd_id=product_id: reduce_product(root, current_user, pd_id))
        buy_button.configure(bg='LightPink2', fg='black', activebackground='LightPink3', activeforeground='black', bd=0)
        buy_button.grid(column=c, row=r+1, pady=20)

        if product_id == error_id:
            Label(root, text=f"Product out of stock", bg='gray10', fg='IndianRed2').grid(column=c, row=r+2, pady=25)

        c += 1
        if c % 8 == 0:
            r += 5
            c = 0

    back_button = Button(root, text=f"Back", command=lambda: render_main_screen(root))
    back_button.configure(activebackground='brown4', activeforeground='snow2', bg='brown3', fg='white', bd=0)
    back_button.grid(column=0, row=r+3, pady=25)

    list_bought_products_button = Button(root, text=f"List bought products")
    list_bought_products_button.configure(command=lambda: list_bought_products(root, current_user))
    list_bought_products_button.configure(activebackground='LightPink3', activeforeground='black',
                                          bg='LightPink2', fg='black', bd=0)
    list_bought_products_button.grid(column=1, row=r+3, pady=25)

    if is_user_admin(current_user):
        add_product_button = Button(root, text="Add product")
        add_product_button.configure(command=lambda: render_add_product_screen(root, current_user))
        add_product_button.configure(activebackground='LightPink3', activeforeground='black',
                                     bg='LightPink2', fg='black', bd=0)
        add_product_button.grid(column=2, row=r+3, pady=25)

        increase_product_button = Button(root, text=f"Increase product quantity")
        increase_product_button.configure(command=lambda: render_increase_product_quantity_screen(root, current_user))
        increase_product_button.configure(activebackground='LightPink3', activeforeground='black',
                                          bg='LightPink2', fg='black', bd=0)
        increase_product_button.grid(column=3, row=r+3, pady=25)


def add_product(root, product, current_user):
    error = add_product_to_inventory(product)
    if not error:
        render_products_screen(root, current_user)
        return

    render_add_product_screen(root, current_user, error)


def render_add_product_screen(root, current_user, error=None):
    clear_screen(root)
    root.geometry("800x200+0+0")

    Label(root, text=f"Enter product name", bg='grey10', fg='snow2').grid(column=0, row=0)
    product_name = StringVar()
    product_name_entry = Entry(root, textvariable=product_name)
    product_name_entry.configure(bg='gray10', fg='snow2', bd=0)
    product_name_entry.grid(column=1, row=0)

    Label(root, text=f"Enter product quantity", bg='grey10', fg='snow2').grid(column=0, row=1)
    product_quantity = StringVar()
    product_quantity_entry = Entry(root, textvariable=product_quantity)
    product_quantity_entry.configure(bg='gray10', fg='snow2', bd=0)
    product_quantity_entry.grid(column=1, row=1)

    Label(root, text=f'Enter product image name with the extension: ', bg='grey10', fg='snow2').grid(column=0, row=2, padx=5)
    img_path = StringVar()
    img_path_entry = Entry(root, textvariable=img_path)
    img_path_entry.configure(bg='gray10', fg='snow2', bd=0)
    img_path_entry.grid(column=1, row=2)
    Label(root, text=f'Example: "image-name.jpeg"', bg='grey10', fg='snow2').grid(column=2, row=2, padx=5)

    product = {
        "name": product_name,
        "quantity": product_quantity,
        "img_path": img_path
    }

    add_product_button = Button(root, text=f"Add product", command=lambda: add_product(root, product, current_user))
    add_product_button.configure(activebackground='LightPink3', activeforeground='black',
                                 bg='LightPink2', fg='black', bd=0)
    add_product_button.grid(column=1, row=3, pady=5)

    back_button = Button(root, text=f"Back", command=lambda: render_products_screen(root, current_user))
    back_button.configure(activebackground='brown4', activeforeground='snow2', bg='brown3', fg='white', bd=0)
    back_button.grid(column=0, row=3)

    Label(root, text=f" The image file must be in:\n"
                     f" /Current-Directory-Path/DB/Images", bg='grey10', fg='Indianred2').grid(column=2, row=3, pady=5)

    if error is not None:
        Label(root, text=error, bg='grey10', fg='IndianRed2').grid(column=2, row=4, pady=25)


def list_bought_products(root, current_user):
    current_user_products = get_current_user_products(current_user)
    if current_user_products:
        render_list_user_products_screen(root, current_user_products, current_user)
        return

    render_products_screen(root, current_user)


def render_list_user_products_screen(root, products, current_user):
    clear_screen(root)
    root.geometry("1600x899+0+0")

    r, c = 2, 0
    for product_id, items in products.items():
        product_name = items['name']
        product_img_path = items['img_path']
        product_count = items['quantity']

        load = Image.open(product_img_path)
        crop = load.crop((0, 0, 200, 200))
        render = ImageTk.PhotoImage(crop)
        img = Label(root, image=render, bd=0)
        img.image = render

        Label(root, text=f"{product_name}", bg='grey10', fg='snow2').grid(column=c, row=r - 2, pady=5)
        Label(root, text=f"Quantity: {product_count}", bg='grey10', fg='snow2').grid(column=c, row=r - 1, pady=5)
        img.grid(column=c, row=r)

        c += 1
        if c % 8 == 0:
            r += 5
            c = 0

    back_button = Button(root, text=f"Back", command=lambda: render_products_screen(root, current_user))
    back_button.configure(activebackground='brown4', activeforeground='snow2', bg='brown3', fg='white', bd=0)
    back_button.grid(column=0, row=r+2, pady=25)


def increase_quantity(root, current_user, product, quantity):
    error = increase_product_quantity(product, quantity)
    if error is not None:
        render_increase_product_quantity_screen(root, current_user, error)
        return

    render_products_screen(root, current_user)


def render_increase_product_quantity_screen(root, current_user, error=None):
    clear_screen(root)
    root.geometry("450x250+0+0")

    Label(root, text=f"Enter product name: ", bg='grey10', fg='snow2').grid(column=0, row=0, pady=25, padx=25)
    product_name = StringVar()
    product_name_entry = Entry(root, textvariable=product_name)
    product_name_entry.configure(bg='gray10', fg='snow2', bd=0)
    product_name_entry.grid(column=1, row=0, pady=25, padx=25)

    Label(root, text=f"Enter quantity: ", bg='grey10', fg='snow2').grid(column=0, row=1, pady=25, padx=25)
    product_quantity = StringVar()
    product_quantity_entry = Entry(root, textvariable=product_quantity)
    product_quantity_entry.configure(bg='gray10', fg='snow2', bd=0)
    product_quantity_entry.grid(column=1, row=1, pady=25, padx=25)

    increase_button = Button(root, text=f"Increase product quantity")
    increase_button.configure(command=lambda: increase_quantity(root, current_user,
                                                                product_name.get(), product_quantity.get()))
    increase_button.configure(activebackground='LightPink3', activeforeground='black',
                              bg='LightPink2', fg='black', bd=0)
    increase_button.grid(column=1, row=2, pady=25, padx=25)

    back_button = Button(root, text=f"Back", command=lambda: render_products_screen(root, current_user))
    back_button.configure(activebackground='brown4', activeforeground='snow2', bg='brown3', fg='white', bd=0)
    back_button.grid(column=0, row=2, pady=25, padx=25)

    if error is not None:
        Label(root, text=error, bg='grey10', fg='IndianRed2').grid(column=2, row=2, pady=25, padx=25)
