def data_type_print(data_type, data):
    if data_type == "int":
        return int(data) * 2
    elif data_type == "real":
        return f"{float(data) * 1.5:.2f}"
    return f"${data}$"


d_type, d = input(), input()
print(data_type_print(d_type, d))
