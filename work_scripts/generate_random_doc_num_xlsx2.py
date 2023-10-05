import csv
import uuid
import random
import xlsxwriter
import pandas as pd


def change_docnum_xslx(path):
    df = pd.read_excel(path)
    print(df)
    df['Номер документа']=df['Номер документа'].apply(lambda x: create_new_doc_number())
    df['Вес, тонн']=df['Вес, тонн'].apply(lambda x: create_new_weight())
    df.to_excel(path, index=False, sheet_name = 'Данные')


def create_new_doc_number() -> str:
    return "MPO" + str(random.randint(1, 9999999))

def create_new_weight() -> float:
    return random.random()*20

if __name__ == '__main__':
    # в file_name записать имя файла, в котором нужно изменить id
    file_name = "template123 (1).xlsx"
    file_path = "/home/alisapokormlyak/Desktop/logX work folder/work_py_files/" + file_name
    change_docnum_xslx(file_path)
