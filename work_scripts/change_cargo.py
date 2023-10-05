import json
import random
import numpy


def change_cargo(path):
    with open(path) as f:
        data = json.load(f)

    for item in data['applications']:
        item['cargo'] = {
                "cargo_items":
                [
                    {
                        "id": "6e73a796-da29-460f-ab54-d45b8d386fba",
                        "name": "Катушка якоря 5ТХ.524.346-02 (БИЛТ.685421.014-02) 245х200х13,3 0,274кг ВС650",
                        "price": 10000.0,
                        "skmtr": "3391523026",
                        "unit_id": 1,
                        "place_id": "5ed5bfe4-9eff-4df1-946f-91a9bdaeb649",
                        "quantity": 1.0
                    },
                    {
                        "id": "54d6671a-7f20-4e9a-9e28-09d7114d7c5a",
                        "name": "Катушка якоря 5ТХ.524.346-01 (БИЛТ.685421.014-01) 237х230х13,3 0,273кг ВС650",
                        "price": 30000.0,
                        "skmtr": "3391523025",
                        "unit_id": 1,
                        "place_id": "5ed5bfe4-9eff-4df1-946f-91a9bdaeb649",
                        "quantity": 1.0
                    }
                ],
                "cargo_places":
                [
                    {
                        "id": "c4cfe6d5-376c-43a3-9de9-a792599cc88f",
                        "width": 0.3,
                        "height": 0.3,
                        "length": 0.3,
                        "volume": 0.3,
                        "weight": 0.3,
                        "quantity": 1
                    }
                ],
                "max_dimensions":
                {
                    "width": 1.1,
                    "height": 1.1,
                    "length": random.choice(numpy.arange(0.1, 1, 0.5))
                }
            }

    with open('file.json', 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def add_package_type(path):
    with open(path) as f:
        data = json.load(f)

        for item in data['applications']:
            for cargo_place in item['cargo']['cargo_places']:
                cargo_place["package_type_id"] = random.randint(1, 4)

    with open('file.json', 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':

    file_name = "file.json"
    file_path = "/Users/alisa/Desktop/logx_work_folder/work_py_files/" + file_name
    change_cargo(file_path)
    #add_package_type(file_path)

