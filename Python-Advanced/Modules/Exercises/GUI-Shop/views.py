from datetime import datetime
from authentication import *
from products import *
from canvas import *

root = create_app()


def render_main_screen():
    clear_screen(root)

    login_button = Button(root, text='Login', width=18, bd=0)
    login_button.configure(font=1, command=lambda: render_login_screen())
    login_button.configure(activebackground='maroon4', activeforeground='snow2', bg='orchid4', fg='white')
    login_button.grid(row=0, column=0, ipady=3, padx=2)

    register_button = Button(root, text='Register')
    register_button.configure(font=1, command=lambda: render_register_screen(), width=18, bd=0)
    register_button.configure(activebackground='maroon4', activeforeground='snow2', bg='orchid4', fg='white')
    register_button.grid(row=0, column=2, ipady=3, padx=2)


def render_register_screen(error=None):
    clear_screen(root)

    Label(root, text=f"Enter username:", bg='gray10', fg='snow2', font=2).grid(column=0, row=0)
    username = StringVar()
    username_entry = Entry(root, textvariable=username)
    username_entry.configure(bg='gray10', fg='snow2', font=0, bd=0)
    username_entry.grid(row=0, column=1, ipady=3, padx=2, pady=2)

    Label(root, text=f"Enter password", bg='gray10', fg='snow2', font=2).grid(column=0, row=1)
    password = StringVar()
    password_entry = Entry(root, textvariable=password)
    password_entry.configure(bg='gray10', fg='snow2', font=1, bd=0)
    password_entry.grid(row=1, column=1, ipady=3, padx=2, pady=2)

    user = {
        'username': username,
        'password': password,
    }

    register_button = Button(root, text=f"Register")
    register_button.configure(font=1, command=lambda: register(user), width=18, bd=0)
    register_button.configure(activebackground='purple4', activeforeground='snow2', bg='purple3', fg='white')
    register_button.grid(row=5, column=0, ipady=3, padx=2,  pady=4)

    back_button = Button(root, text=f"Back")
    back_button.configure(font=1, command=lambda: render_main_screen(), width=18, bd=0)
    back_button.configure(activebackground='brown4', activeforeground='snow2', bg='brown3', fg='white')
    back_button.grid(row=5, column=1, ipady=3, padx=2,  pady=4, sticky=W+E)

    if error is not None:
        Label(root, text=f"{error}", bg='gray10', fg='IndianRed2', font=1).grid(row=0, column=2, rowspan=4, padx=5)


def render_login_screen(error=None):
    clear_screen(root)

    Label(root, text=f"Enter username: ", bg='gray10', fg='snow2', font=2).grid(column=0, row=0)
    username = StringVar()
    username_entry = Entry(root, textvariable=username)
    username_entry.configure(bg='gray10', fg='snow2', font=1, bd=0)
    username_entry.grid(row=0, column=1, ipady=3, pady=2)

    Label(root, text=f"Enter password: ", font=1, bg='gray10', fg='snow2').grid(row=1, column=0)
    password = StringVar()
    password_entry = Entry(root, textvariable=password)
    password_entry.configure(bg='gray10', fg='snow2', font=1, show='*', bd=0)
    password_entry.grid(row=1, column=1, ipady=3, pady=2)

    login_button = Button(root, text='Login')
    login_button.configure(activebackground='maroon4', activeforeground='snow2', bg='orchid4', fg='white')
    login_button.configure(font=1, command=lambda: login(username.get(), password.get()), width=18, bd=0)
    login_button.grid(row=2, column=0, ipady=3, padx=2, pady=4)

    back_button = Button(root, text='Back')
    back_button.configure(font=1, command=lambda: render_main_screen(), width=18, bd=0)
    back_button.configure(activebackground='brown4', activeforeground='snow2', bg='brown3', fg='white')
    back_button.grid(row=2, column=1, ipady=3, padx=2, pady=4, sticky=W+E)

    if error is not None:
        Label(root, text=f"{error}", bg='gray10', fg='IndianRed2', font=1).grid(column=3, row=2)


def render_menu_screen(current_seller, error=None):
    clear_screen(root)

    sell_button = Button(root, text='Sell product')
    sell_button.configure(
        font=1, command=lambda: render_products_screen(current_seller, command_type='sell'), width=18, bd=0)
    sell_button.configure(activebackground='maroon4', activeforeground='snow2', bg='orchid4', fg='white')
    sell_button.grid(row=0, column=0, ipady=3, padx=2)

    increase_button = Button(root, text='Increase quantity')
    increase_button.configure(
        font=1, command=lambda: render_products_screen(current_seller, command_type='increase'), width=18, bd=0)
    increase_button.configure(activebackground='maroon4', activeforeground='snow2', bg='orchid4', fg='white')
    increase_button.grid(row=0, column=1, ipady=3, padx=2)

    add_button = Button(root, text='Add product')
    add_button.configure(font=1, command=lambda: render_add_product_screen(current_seller), width=18, bd=0)
    add_button.configure(activebackground='maroon4', activeforeground='snow2', bg='orchid4', fg='white')
    add_button.grid(row=0, column=2, ipady=3, padx=2)

    back_button = Button(root, text='Back')
    back_button.configure(font=1, command=lambda: render_login_screen(), width=18, bd=0)
    back_button.configure(activebackground='brown4', activeforeground='snow2', bg='brown3', fg='white')
    back_button.grid(row=0, column=3, ipady=3, padx=2)

    if error is not None:
        Label(root, text=f"{error}", font=2, bg='gray10', fg='IndianRed2').grid(row=1, column=0, pady=4)


def render_add_product_screen(current_seller, error=None):
    clear_screen(root)

    Label(root, text=f"Enter product name", bg='grey10', fg='snow2', font=1).grid(row=0, column=0)
    product_name = StringVar()
    product_name_entry = Entry(root, textvariable=product_name)
    product_name_entry.configure(bg='gray10', fg='snow2', font=1, bd=0)
    product_name_entry.grid(row=0, column=1, ipady=3, pady=2)

    Label(root, text=f"Enter product taste", bg='grey10', fg='snow2', font=1).grid(row=1, column=0)
    product_taste = StringVar()
    product_taste_entry = Entry(root, textvariable=product_taste)
    product_taste_entry.configure(bg='gray10', fg='snow2', font=1, bd=0)
    product_taste_entry.grid(row=1, column=1, ipady=3, pady=2)

    Label(root, text=f'Enter selling unit: "gr, kg, ml or count"', bg='grey10', fg='snow2', font=1).\
        grid(row=2, column=0)
    unit = StringVar()
    unit_entry = Entry(root, textvariable=unit)
    unit_entry.configure(bg='gray10', fg='snow2', font=1, bd=0)
    unit_entry.grid(row=2, column=1, ipady=3, pady=2)

    Label(root, text=f"Enter selling doze in selling unit", bg='grey10', fg='snow2', font=1).\
        grid(row=3, column=0)
    doze = StringVar()
    doze_entry = Entry(root, textvariable=doze)
    doze_entry.configure(bg='gray10', fg='snow2', font=1, bd=0)
    doze_entry.grid(row=3, column=1, ipady=3, pady=2)

    Label(root, text=f"Enter product quantity in selling unit", bg='grey10', fg='snow2', font=1).grid(row=4, column=0)
    product_quantity = StringVar()
    product_quantity_entry = Entry(root, textvariable=product_quantity)
    product_quantity_entry.configure(bg='gray10', fg='snow2', font=1, bd=0)
    product_quantity_entry.grid(row=4, column=1, ipady=3, pady=2)

    Label(root, text=f"Enter product price for a doze", bg='grey10', fg='snow2', font=1).grid(row=5, column=0)
    product_price = StringVar()
    product_price_entry = Entry(root, textvariable=product_price)
    product_price_entry.configure(bg='gray10', fg='snow2', font=1, bd=0)
    product_price_entry.grid(row=5, column=1, ipady=3, pady=2)

    Label(root, text=f'Enter image name with the extension: ', bg='grey10', fg='snow2', font=1).\
        grid(row=6, column=0, padx=5)
    img_path = StringVar()
    img_path_entry = Entry(root, textvariable=img_path)
    img_path_entry.configure(bg='gray10', fg='snow2', font=1, bd=0)
    img_path_entry.grid(row=6, column=1, ipady=3, pady=2)
    Label(root, text=f'Example: "image-name.jpeg"', bg='grey10', fg='snow2', font=1).grid(row=6, column=2, padx=5)

    product = {
        "name": product_name,
        "taste": product_taste,
        "quantity": product_quantity,
        "price": product_price,
        "unit": unit,
        "doze": doze,
        "img_path": img_path,
    }

    back_button = Button(root, text=f"Back")
    back_button.configure(font=1, command=lambda: render_menu_screen(current_seller), width=18, bd=0)
    back_button.configure(activebackground='brown4', activeforeground='snow2', bg='brown3', fg='white')
    back_button.grid(row=7, column=0, ipady=3, padx=2, pady=4)

    add_product_button = Button(root, text=f"Add product")
    add_product_button.configure(font=1, command=lambda: add_product(product, current_seller), width=18, bd=0)
    add_product_button.configure(activebackground='LightPink3', activeforeground='black', bg='LightPink2', fg='black')
    add_product_button.grid(row=7, column=1, ipady=3, padx=2, pady=4)

    Label(root, text=f"The image must be in:\n"
                     f"/Current-Folder/DB/Images", bg='grey10', fg='Indianred2', font=1).\
        grid(row=7, column=2, pady=5)

    if error is not None:
        Label(root, text=error, bg='grey10', fg='IndianRed2', font=1).grid(row=8, column=1, pady=25)


def render_products_screen(current_seller, command_type, error_id=None, page_id=0):
    clear_screen(root)

    if command_type == 'sell':
        products = get_products_content(page_id, '>')
        button_text = f'Sell'
    else:
        products = get_products_content(page_id, '<')
        button_text = f'Increase'

    r, c = 3, 0
    if not products and page_id <= 0:
        render_menu_screen(current_seller, error=f"There is no products in the inventory!")
        return
    elif not products:
        render_products_screen(current_seller, command_type, page_id=page_id - 1)
        return

    for product in products:
        product_id = product.get('id')
        product_name = product.get('name')
        product_img_path = product.get('img_path')
        product_count = product.get('quantity')
        product_unit = product.get('unit')
        product_price = product.get('price')
        now = datetime.now().strftime("%d/%h/%y - %H:%M:%S")
        img = get_image(root, product_img_path)

        Label(root, text=f"{product_name}", bg='grey10', fg='snow2', font=1).grid(row=r-3, column=c, pady=2)

        Label(root, text=f"{product_price:.2f} lv.", bg='grey10', fg='snow2', font=1).grid(row=r-2, column=c, pady=2)

        Label(root, text=f"{product_count} {product_unit}.", bg='grey10', fg='snow2', font=1).\
            grid(row=r-1, column=c, pady=2)

        img.grid(row=r, column=c, padx=14)

        button = Button(root, text=button_text)
        button.configure(command=get_command(command_type, current_seller, page_id, product_id, now))
        button.configure(font=1, bd=0)
        button.configure(bg='LightPink2', fg='black', activebackground='LightPink3', activeforeground='black')
        button.grid(row=r+1, column=c, ipady=3, pady=20)

        if product_id == error_id:
            Label(root, text=f"Not enough quantity!", bg='gray10', fg='IndianRed2', font=1).\
                grid(column=c, row=r+2, pady=25)

        c += 1
        if c % 7 == 0:
            r += 6
            c = 0

    c = 0
    if page_id > 0:
        prev_page_button = Button(root, text=f"<- Previous page ", font=1, width=18, bd=0)
        prev_page_button.configure(command=lambda: render_products_screen(current_seller, command_type, page_id=page_id - 1))
        prev_page_button.configure(activebackground='LightPink3', activeforeground='black', bg='LightPink2', fg='black')
        prev_page_button.grid(row=r + 3, column=c, ipady=3, padx=2, pady=4)
        c += 1

    back_button = Button(root, text=f"Back")
    back_button.configure(font=1, command=lambda: render_menu_screen(current_seller), width=18, bd=0)
    back_button.configure(activebackground='brown4', activeforeground='snow2', bg='brown3', fg='white')
    back_button.grid(row=r+3, column=c, ipady=3, padx=2, pady=4)

    next_page_button = Button(root, text=f"Next page ->", width=18, bd=0)
    next_page_button.configure(font=1, command=lambda: render_products_screen(current_seller, command_type, page_id=page_id + 1))
    next_page_button.configure(activebackground='LightPink3', activeforeground='black', bg='LightPink2', fg='black')
    next_page_button.grid(row=r + 3, column=c+1, ipady=3, padx=2, pady=4)


def render_increase_screen(product_id, current_seller, error=None):
    clear_screen(root)

    Label(root, text=f"Enter product quantity: ", font=1, bg='gray10', fg='snow2').grid(row=0, column=0, padx=4)
    product_quantity = StringVar()
    product_quantity_entry = Entry(root, textvariable=product_quantity)
    product_quantity_entry.configure(bg='gray10', fg='snow2', font=1, bd=0)
    product_quantity_entry.grid(row=0, column=1, ipady=3, pady=2)

    back_button = Button(root, text=f"Back")
    back_button.configure(font=1, command=lambda: render_products_screen(current_seller, 'increase'), width=18, bd=0)
    back_button.configure(activebackground='brown4', activeforeground='snow2', bg='brown3', fg='white')
    back_button.grid(row=1, column=0, ipady=3, padx=2, pady=4)

    increase_button = Button(root, text='Increase', font=1)
    increase_button.configure(command=lambda: increase_product(product_id, product_quantity.get(), current_seller))
    increase_button.configure(activebackground='LightPink3', activeforeground='black', bg='LightPink2', fg='black')
    increase_button.grid(row=1, column=1, ipady=3, padx=2, pady=4)

    if error is not None:
        Label(root, text=error, bg='grey10', fg='snow2', font=1).grid(row=2, column=0, pady=2)


'''Helpers'''


def get_command(command_type, current_seller, page_id, product_id, now):
    if command_type == 'sell':
        return lambda pd_id=product_id, nw=now: reduce_product(current_seller, pd_id, nw, page_id)
    return lambda pd_id=product_id: render_increase_screen(pd_id, current_seller)


def register(user):
    error = register_validator(**user)
    if error:
        render_register_screen(error)
        return

    render_login_screen(root)


def login(username, password):
    if login_validator(username, password):
        render_menu_screen(username)
        return

    render_login_screen(error='Wrong username or password!')


def add_product(product, current_seller):
    error = add_product_to_inventory(product)
    if not error:
        render_add_product_screen(current_seller)
        return

    render_add_product_screen(current_seller, error)


def reduce_product(current_seller, product_id, now, page_id):
    error_id = reduce_product_quantity(product_id)
    if error_id:
        render_products_screen(current_seller, 'sell', error_id=error_id, page_id=page_id)
        return

    add_product_to_user_products(current_seller, product_id, now)
    render_products_screen(current_seller, 'sell')


def increase_product(product_id, product_quantity, current_seller):
    error = increase_product_quantity(product_id, product_quantity)
    if error:
        render_increase_screen(product_id, current_seller, error)
        return

    render_products_screen(current_seller, 'increase')
