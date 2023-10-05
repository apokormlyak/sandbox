import json


def add_delivery_type(path):
    with open(path) as f:
        data = json.load(f)

    for item in data['applications']:
        item['due_date'] = 1693885975

    with open('file.json', 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':

    file_name = "file.json"
    file_path = "/home/alisapokormlyak/Desktop/logX work folder/work_py_files/" + file_name
    add_delivery_type(file_path)
