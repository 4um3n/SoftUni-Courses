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
                product = {k: os.path.join(current_path, v) if k == "img_path" else v for k, v in product.items()}
                products.append(product)

    return products


def reduce_product_quantity(products, product_id):
    for i in range(len(products)):
        if products[i]['id'] == product_id:
            if products[i]['quantity'] <= 0:
                return products[i]['id']

            products[i]['quantity'] -= 1
            with open(products_file_path, 'r+') as file:
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
            product[k] = os.path.join(image_files_dir_path, v)
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


def increase_product_quantity():
    pass
