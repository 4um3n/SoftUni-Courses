import json
import os

current_path = os.getcwd()
products_file_path = os.path.join(current_path, 'DB', 'products.txt')
users_file_path = os.path.join(current_path, "DB", "users.txt")
image_files_dir_path = os.path.join(current_path, "DB", "Images")


def get_products_content():
    products = []
    with open(products_file_path, 'r') as file:
        for line in file.read().split('\n'):
            if line:
                product = json.loads(line)
                product = {k: os.path.join(image_files_dir_path, v) if k == "img_path" else v
                           for k, v in product.items()}
                products.append(product)

    return products


def reduce_product_quantity(product_id):
    products = []
    with open(products_file_path, 'r+') as file:
        for line in file.read().split('\n'):
            if line:
                line = json.loads(line)
                if line['id'] == product_id:
                    if line['quantity'] <= 0:
                        return line['id']

                    line['quantity'] -= 1

                products.append(line)

        file.truncate(0)
        file.seek(0)
        for line in products:
            file.write(json.dumps(line))
            file.write(f"\n")


def add_product_to_user_products(current_user, product_id):
    users = []
    with open(users_file_path, 'r+') as file:
        for line in file.read().split('\n'):
            if line:
                user = json.loads(line)
                users.append(user)

        file.truncate(0)
        file.seek(0)

        for user in users:
            if user['username'] == current_user:
                user['products'].append(product_id)

            file.write(json.dumps(user))
            file.write('\n')


def add_product_to_inventory(product):
    error = []
    product = {k: v.get() for k, v in product.items()}
    mapper = {"name": "name", "quantity": "quantity", "img_path": "image name"}
    for k, v in product.items():
        if not v:
            error.append(f"Enter {mapper[k]}!")
            continue

        if k == "img_path":
            if v not in os.listdir(image_files_dir_path):
                error.append(f'File "{product[k]}" does not exist!')

        elif k == "quantity":
            try:
                product[k] = int(v)
                if product[k] < 0:
                    raise ValueError
            except ValueError:
                error.append(f"Quantity must be a positive integer!")

    if not error:
        with open(products_file_path, 'r+') as file:
            next_id = len(file.read().split('\n'))
            product.update({"id": next_id})
            file.write(json.dumps(product))
            file.write("\n")

    return '\n'.join(error)


def get_current_user_products(current_user):
    products = get_products_content()
    current_user_products_ids = []
    current_user_products = {}
    with open(users_file_path, 'r') as file:
        for line in file.read().split('\n'):
            if line:
                line = json.loads(line)
                if line['username'] == current_user:
                    current_user_products_ids = line['products'].copy()

    for product_id in current_user_products_ids:
        if product_id not in current_user_products:
            current_user_products[product_id] = {"quantity": 0, "name": "", "img_path": ""}

        current_user_products[product_id]['quantity'] += 1

    for product_id in current_user_products_ids:
        for product in products:
            if product_id == product['id']:
                current_user_products[product_id]['name'] = product['name']
                current_user_products[product_id]['img_path'] = product['img_path']

    return current_user_products


def increase_product_quantity(product, quantity):
    products = []
    is_found = False
    error = []
    if not product:
        error.append(f"Enter product name!")
    if not quantity:
        error.append(f"Enter quantity!")

    if error:
        return '\n'.join(error)

    with open(products_file_path, 'r+') as file:
        for line in file.read().split('\n'):
            if line:
                line = json.loads(line)
                if product == line['name']:
                    is_found = True
                    try:
                        quantity = int(quantity)
                        if quantity < 0:
                            raise ValueError
                        line['quantity'] += int(quantity)
                    except ValueError:
                        error.append(f"Quantity must be a positive integer!")
                        break

                products.append(line)

        if not is_found:
            error.append(f"Product not found in the inventory!")

        if error:
            return '\n'.join(error)

        file.truncate(0)
        file.seek(0)
        for line in products:
            file.write(json.dumps(line))
            file.write('\n')
