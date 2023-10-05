import json
import random


def filter_apps(path):
    with open(path) as f:
        data = json.load(f)
        print(len(data['applications']))

        filtered_apps = list(filter(lambda app: app['document_number'][0:3] not in ['ALS', 'WMS'],
                                    data['applications']))

        data['applications'] = filtered_apps
        print(len(data['applications']))

    with open('file.json', 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def get_uniq_applications(path):
    with open(path) as f:
        data = json.load(f)
        print(len(data['applications']))

        appls_by_num = {a['document_number']: a for a in data['applications']}
        data['applications'] = list(appls_by_num.values())
        print(len(data["applications"]))

#Пример, как это работает: словарь словарей по ключу
        apps = [{'document_number': 1, 'value': 33},
                {'document_number': 1, 'value': 33},
                {'document_number': 2, 'value': 33},
                {'document_number': 2, 'value': 33},
                {'document_number': 3, 'value': 33},
                {'document_number': 3, 'value': 33},
                {'document_number': 4, 'value': 33},
                {'document_number': 5, 'value': 33},

                ]
        print(apps)
        appls_by_num = {a['document_number']: a for a in apps}
        uniq_apps = list(appls_by_num)
        print(uniq_apps)

    with open('file.json', 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':

    file_name = "file.json"
    file_path = "/home/alisapokormlyak/Desktop/logX work folder/work_py_files/" + file_name
    get_uniq_applications(file_path)
