from tkinter import *
from products import *
from authentication import *
from PIL import Image, ImageTk


def clear_screen(root):
    for slave in root.grid_slaves():
        slave.destroy()


def render_main_screen(root):
    clear_screen(root)

    Button(root, text=f"Login", bg='green', fg='white', command=lambda: render_login_screen(root)).\
        grid(column=0, row=0, padx=25, pady=25)

    Button(root, text=f"Register", bg='yellow', fg='black', command=lambda: render_register_screen(root)).\
        grid(column=1, row=0, padx=25, pady=25)

    Button(root, text=f"Exit", bg='red', fg='yellow', command=lambda: exit()).grid(column=2, row=0, pady=25, padx=25)


def login(root, username, password):
    if login_validator(username, password):
        render_products_screen(root, username)
        return
    
    render_login_screen(root, error='Wrong username or password!')


def render_login_screen(root, error=None):
    clear_screen(root)

    Label(root, text=f"Enter username: ").grid(column=0, row=0)
    username = StringVar()
    Entry(root, textvariable=username).grid(column=1, row=0)

    Label(root, text=f"Enter password:").grid(column=0, row=1)
    password = StringVar()
    Entry(root, textvariable=password).grid(column=1, row=1)

    Button(root, text='Login', bg='green', fg='white', command=lambda: login(root, username.get(), password.get())).\
        grid(column=0, row=2, padx=20, pady=20)

    Button(root, text='Back', bg='red', fg='yellow', command=lambda: render_main_screen(root)).\
        grid(column=1, row=2, padx=20, pady=20)

    if error is not None:
        Label(root, text=f"{error}").grid(column=3, row=2)


def register(root, user):
    error = register_validator(**user)
    if error:
        render_register_screen(root, error)
        return

    render_login_screen(root)


def render_register_screen(root, error=None):
    clear_screen(root)

    Label(root, text=f"Enter username:").grid(column=0, row=0)
    username = StringVar()
    Entry(root, textvariable=username).grid(column=1, row=0)

    Label(root, text=f"Enter password:").grid(column=0, row=1)
    password = StringVar()
    Entry(root, textvariable=password).grid(column=1, row=1)

    Label(root, text=f"Enter your first name:").grid(column=0, row=2)
    first_name = StringVar()
    Entry(root, textvariable=first_name).grid(column=1, row=2)

    Label(root, text=f"Enter your last name:").grid(column=0, row=3)
    last_name = StringVar()
    Entry(root, textvariable=last_name).grid(column=1, row=3)

    Label(root, text=f"Is this user an admin?").grid(column=0, row=4)
    is_admin = BooleanVar()
    Checkbutton(root, variable=is_admin).grid(column=1, row=4)

    user = {
        'username': username,
        'password': password,
        'first_name': first_name,
        'last_name': last_name,
        'is_admin': is_admin
    }

    Button(root, text=f"Register", bg='green', fg='white', command=lambda: register(root, user)).\
        grid(column=0, row=5)

    Button(root, text=f"Back", bg='red', fg='yellow', command=lambda: render_main_screen(root)).\
        grid(column=1, row=5)

    if error is not None:
        Label(root, text=f"{error}").grid(column=2, row=5)


def reduce_product(root, current_user, product_id):
    error_id = reduce_product_quantity(product_id)
    if error_id:
        render_products_screen(root, current_user, error_id)
        return

    add_product_to_user_products(current_user, product_id)
    render_products_screen(root, current_user)


def render_products_screen(root, current_user, error_id=None):
    clear_screen(root)

    r, c = 2, 0
    products = get_products_content()
    for i in range(len(products)):
        product_id = products[i].get('id')
        product_name = products[i].get('name')
        product_img_path = products[i].get('img_path')
        product_count = products[i].get('quantity')

        load = Image.open(product_img_path)
        crop = load.crop((0, 0, 200, 200))
        render = ImageTk.PhotoImage(crop)
        img = Label(root, image=render)
        img.image = render

        Label(root, text=f"{product_name}").grid(column=c, row=r-2, pady=5)
        Label(root, text=f"Quantity: {product_count}").grid(column=c, row=r-1, pady=5)
        img.grid(column=c, row=r)
        Button(root, text=f"Buy {product_name}", bg='yellow',
               command=lambda pd_id=product_id: reduce_product(root, current_user, pd_id)).\
            grid(column=c, row=r+1, pady=20)

        if product_id == error_id:
            Label(root, text=f"Product out of stock", fg='red').grid(column=c, row=r+2, pady=20)

        c += 1
        if c % 8 == 0:
            r += 5
            c = 0

    Button(root, text=f"Back", bg='red', fg='yellow', command=lambda: render_main_screen(root)).\
        grid(column=0, row=r+3, pady=25)

    Button(root, text=f"List bought products", bg='green', fg='white',
           command=lambda: list_bought_products(root, current_user)).grid(column=1, row=r+3, pady=25)

    if is_user_admin(current_user):
        Button(root, text="Add product", bg='green', fg='white',
               command=lambda: render_add_product_screen(root, current_user)).grid(column=2, row=r+3, pady=25)

        Button(root, text=f"Increase product quantity", bg='green', fg='white',
               command=lambda: render_increase_product_quantity_screen(root, current_user)).\
            grid(column=3, row=r+3, pady=25)


def add_product(root, product, current_user):
    error = add_product_to_inventory(product)
    if not error:
        render_products_screen(root, current_user)
        return

    render_add_product_screen(root, current_user, error)


def render_add_product_screen(root, current_user, error=None):
    clear_screen(root)

    Label(root, text=f"Enter product name").grid(column=0, row=0)
    product_name = StringVar()
    Entry(root, textvariable=product_name).grid(column=1, row=0)

    Label(root, text=f"Enter product quantity").grid(column=0, row=1)
    product_quantity = StringVar()
    Entry(root, textvariable=product_quantity).grid(column=1, row=1)

    Label(root, text=f'Enter product image name with the extension: ').grid(column=0, row=2, padx=5)
    img_path = StringVar()
    Entry(root, textvariable=img_path).grid(column=1, row=2)
    Label(root, text=f'Example: "image-name.jpeg"').grid(column=2, row=2, padx=5)

    product = {
        "name": product_name,
        "quantity": product_quantity,
        "img_path": img_path
    }

    Button(root, text=f"Add product", bg='green', fg='white',
           command=lambda: add_product(root, product, current_user)).grid(column=1, row=3, pady=5)

    Button(root, text=f"Back", bg='red', fg='yellow', command=lambda: render_products_screen(root, current_user)).\
        grid(column=0, row=3)

    Label(root, text=f" The image file must be in:\n"
                     f" /Current-Directory-Path/DB/Images", fg='red').grid(column=2, row=3, pady=5)

    if error is not None:
        Label(root, text=error, fg='red').grid(column=2, row=4, pady=25)


def list_bought_products(root, current_user):
    current_user_products = get_current_user_products(current_user)
    if current_user_products:
        render_list_user_products_screen(root, current_user_products, current_user)
        return

    render_products_screen(root, current_user)


def render_list_user_products_screen(root, products, current_user):
    clear_screen(root)

    r, c = 2, 0
    for product_id, items in products.items():
        product_name = items['name']
        product_img_path = items['img_path']
        product_count = items['quantity']

        load = Image.open(product_img_path)
        crop = load.crop((0, 0, 200, 200))
        render = ImageTk.PhotoImage(crop)
        img = Label(root, image=render)
        img.image = render

        Label(root, text=f"{product_name}").grid(column=c, row=r - 2, pady=5)
        Label(root, text=f"Quantity: {product_count}").grid(column=c, row=r - 1, pady=5)
        img.grid(column=c, row=r)

        c += 1
        if c % 8 == 0:
            r += 5
            c = 0

    Button(root, text=f"Back", bg='red', fg='yellow',
           command=lambda: render_products_screen(root, current_user)).grid(column=0, row=r+2, pady=25)


def increase_quantity(root, current_user, product, quantity):
    error = increase_product_quantity(product, quantity)
    if error is not None:
        render_increase_product_quantity_screen(root, current_user, error)
        return

    render_products_screen(root, current_user)


def render_increase_product_quantity_screen(root, current_user, error=None):
    clear_screen(root)

    Label(root, text=f"Enter product name: ").grid(column=0, row=0, pady=25, padx=25)
    product_name = StringVar()
    Entry(root, textvariable=product_name).grid(column=1, row=0, pady=25, padx=25)

    Label(root, text=f"Enter quantity: ").grid(column=0, row=1, pady=25, padx=25)
    product_quantity = StringVar()
    Entry(root, textvariable=product_quantity).grid(column=1, row=1, pady=25, padx=25)

    Button(root, text=f"Increase product quantity", bg='green', fg='white',
           command=lambda: increase_quantity(root, current_user, product_name.get(), product_quantity.get())).\
        grid(column=1, row=2, pady=25, padx=25)

    Button(root, text=f"Back", bg='red', fg='yellow', command=lambda: render_products_screen(root, current_user)).\
        grid(column=0, row=2, pady=25, padx=25)

    if error is not None:
        Label(root, text=error, fg='red').grid(column=2, row=2, pady=25, padx=25)
