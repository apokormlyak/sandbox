import json
import random


def change_id(path):
    with open(path) as f:
        data = json.load(f)

    for item in data['applications']:
        prefixes = ["RAS", "ZZS", "ABS", "SRS", "ALS", "WMS"]
        item['id'] = random.randint(1, 99999999)
        item["document_number"] = random.choice(prefixes) + str(random.randint(1, 9999999))

    with open('file.json', 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':

    # в file_name записать имя файла, в котором нужно изменить id
    file_name = "file.json"
    file_path = "/Users/alisa/Desktop/logx_work_folder/work_py_files/" + file_name
    change_id(file_path)
