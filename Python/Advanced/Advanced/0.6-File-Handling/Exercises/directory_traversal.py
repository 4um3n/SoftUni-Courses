import os


def create_report_file_of_given_dir(dir_path: str):
    try:
        files = [f for f in os.listdir(dir_path) if os.path.isfile(f)]
    except FileNotFoundError:
        print(f"Enter a valid path!")
        return

    report_data = {}
    for file_name in files:
        file_extension = file_name.split(".")[-1]
        if file_extension not in report_data:
            report_data[file_extension] = []

        report_data[file_extension].append(file_name)

    report_file_path = os.path.join(os.getcwd(), "report.txt")
    with open(report_file_path, "w") as file:
        for extension in sorted(report_data):
            file.write(f".{extension}\n")
            files = [f"- - - {f}" for f in sorted(report_data[extension])]
            file.write('\n'.join(files))


create_report_file_of_given_dir(input())
