import json
import random


def change_vagon_id(path):
    with open(path) as f:
        data = json.load(f)

    for item in data['result']:
        # item['car_id'] = random.randint(1, 300)
        item['consignee_tgnl'] = str(random.randint(1, 3800))

    with open('file.json', 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':

    # в file_name записать имя файла, в котором нужно изменить id
    file_name = "file.json"
    file_path = "/Users/alisa/Desktop/logx_work_folder/work_py_files/work_scripts/" + file_name
    change_vagon_id(file_path)
