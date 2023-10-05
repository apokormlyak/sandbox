import csv
import uuid
import random
import xlsxwriter
import pandas as pd

def change_docnum_xslx(path):
    xl_file = pd.ExcelFile(file_name)
    df = pd.read_excel(path, sheet_name="Данные", usecols = ['Номер документа'])
    i=1
    print(df)
    while i < len(df):
        df[i] = new_doc_number()
        print(df[i])
        i+=1

def new_doc_number():
    return "MPO" + str(random.randint(1,9999999))

        
       
        

if __name__ == '__main__':

    # в file_name записать имя файла, в котором нужно изменить id
    file_name = "2XLSX_template.xlsx"
    file_path = "/home/alisapokormlyak/Desktop/logX work folder/work_py_files/" + file_name
    change_docnum_xslx(file_path)
