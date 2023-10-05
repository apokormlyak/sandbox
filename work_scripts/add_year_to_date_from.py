import json
import os
from datetime import datetime

#def add_year(path):
 #   for root, dirs, files in os.walk(path):
  #      for file in files:
   #         if(file.endswith('.json')):
    #            with open(os.path.join(root, file), 'r') as f:
     #               data = json.load(f)

      #          for item in data['applications']:
       #             for waypoint in item['waypoints']:
        #                date = datetime.fromtimestamp(waypoint['date_from'])
         #               new_date = date.replace(year = date.year + 2)
          #              waypoint['date_from'] = new_date.timestamp()
           #             with open(os.path.join(root, file), 'w') as f:
            #                json.dump(data, f, ensure_ascii=False, indent=4)


def add_year(path):
    with open(path) as f:
         data = json.load(f)

         for item in data['applications']:
             for waypoint in item['waypoints']:
                date = datetime.fromtimestamp(waypoint['date_from'])
                new_date = date.replace(year = date.year + 2)
                waypoint['date_from'] = new_date.timestamp()

    with open('file.json', 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':

    file_name = "file.json"
    file_path = "/home/alisapokormlyak/Desktop/logX work folder/work_py_files/" + file_name
    add_year(file_path)
