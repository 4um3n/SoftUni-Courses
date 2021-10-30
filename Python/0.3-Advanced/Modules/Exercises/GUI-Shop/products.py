import os
import json

current_path = os.getcwd()
products_file_path = os.path.join(current_path, 'DB', 'products.txt')
users_file_path = os.path.join(current_path, "DB", "users.txt")
image_files_dir_path = os.path.join(current_path, "DB", "Images")


def get_products_content(page_id, sign):
    products = []
    current_products = []
    with open(products_file_path, 'r') as file:
        for line in file.read().split('\n'):
            if line:
                product = json.loads(line)
                product = {k: os.path.join(image_files_dir_path, v) if k == "img_path" else v
                           for k, v in product.items()}

                if sign == '<' and product['quantity'] > 0:
                    continue
                elif sign == '>' and product['quantity'] <= 0:
                    continue

                current_products.append(product)
                if len(current_products) == 14:
                    products.append(current_products.copy())
                    current_products.clear()

        if current_products:
            products.append(current_products)

        if len(products) >= page_id + 1:
            return products[page_id]
        return []


def reduce_product_quantity(product_id):
    products = []
    with open(products_file_path, 'r+') as file:
        for line in [line for line in file.read().split('\n') if line]:
            line = json.loads(line)
            if line['id'] == product_id:
                if line['quantity'] <= 0:
                    return line['id']

                line['quantity'] -= line['doze'] if line['quantity'] >= line['doze'] else line['quantity']

            products.append(line)

        file.truncate(0)
        file.seek(0)
        for line in products:
            file.write(json.dumps(line))
            file.write(f"\n")


def add_product_to_user_products(current_user, product_id, now):
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
                user['sold_products'].append((product_id, now))

            file.write(json.dumps(user))
            file.write('\n')


def add_product_to_inventory(product):
    error = []
    product = {k: v.get() for k, v in product.items()}
    mapper = {
        "name": "product name",
        "taste": "product taste",
        "quantity": "product quantity",
        "img_path": "image path",
        "price": "product price",
        "unit": "selling unit",
        "doze": "selling doze",
    }

    for k, v in product.items():
        if not v:
            error.append(f"Enter {mapper[k]}!")
            continue

        if k == "img_path":
            if v not in os.listdir(image_files_dir_path):
                error.append(f'Image "{product[k]}" does not exist in ..DB/Images!')

        elif k == "quantity" or k == "price" or k == "doze":
            try:
                product[k] = float(v)
                if product[k] < 0:
                    raise ValueError
            except ValueError:
                error.append(f"{mapper[k]} must be a positive integer!")

        elif k == "unit":
            units = ['gr', 'kg', 'ml', 'count']

            if v not in units:
                error.append(f"Product unit must be one of: {', '.join(units)}")

    if not error:
        with open(products_file_path, 'r+') as file:
            next_id = len(file.read().split('\n'))
            product.update({"id": next_id})
            file.write(json.dumps(product))
            file.write("\n")

    return '\n'.join(error)


def increase_product_quantity(product_id, quantity):
    products = []
    is_found = False
    error = []
    if not product_id:
        error.append(f"Enter product name!")
    if not quantity:
        error.append(f"Enter product quantity!")

    if error:
        return '\n'.join(error)

    with open(products_file_path, 'r+') as file:
        for line in [line for line in file.read().split('\n') if line]:
            line = json.loads(line)
            if product_id == line['id']:
                is_found = True
                try:
                    quantity = int(quantity)
                    if quantity < 0:
                        raise ValueError
                    line['quantity'] += int(quantity)
                except ValueError:
                    error.append(f"Product quantity must be a positive integer!")
                    break

            products.append(line)

        if not is_found:
            error.append(f"Product not found!")

        if error:
            return '\n'.join(error)

        file.truncate(0)
        file.seek(0)
        for line in products:
            file.write(json.dumps(line))
            file.write('\n')
