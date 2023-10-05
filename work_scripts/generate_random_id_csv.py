import csv
import uuid
import random

def change_id_csv(path):
    with open(path) as f:
        reader = csv.reader(f)
        content_list = list(reader)
        # Меняем значение в первом столбце с номером заявки
        # content_list[1][0] = id + 1
        # content_list[2][0] = id + 2
        i=1
        while i < len(content_list):
            content_list[i][0] = str(uuid.uuid4())
            prefixes = ["RAS", "ZZS", "ABS", "SRS", "ALS", "WMS"]
            content_list[i][1] = random.choice(prefixes) + str(random.randint(1, 9999999))
            i=i+1
        
        

    # Перезаписываем файл с новыми номерами
    with open(path, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(content_list)

if __name__ == '__main__':

    # в file_name записать имя файла, в котором нужно изменить id
    file_name = "test_1.csv"
    file_path = "/home/alisapokormlyak/Desktop/logX work folder/work_py_files/" + file_name
    change_id_csv(file_path)
