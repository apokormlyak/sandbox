import pytest
import logging
# from helpers.application import Application
import json
from pathlib import Path

LOGGER = logging.getLogger(__name__)


def get_diff_in_results():

    p1 = Path("графики до очистки/31102023 charts")
    p2 = Path("графики после очистки 30_30_90/31102023 charts3")
    for file1 in p1.rglob("*"):
        for file2 in p2.rglob("*"):
            if file1.name == file2.name:
                print(file1.name + ' vs ' + file2.name + '\n')
                # file1 = 'графики до очистки/09-10_day charts/09-10-day_sent_combinations_profit.json'
                # file2 = 'графики после очистки 30_30_90/09-10_day charts3/09-10_day_sent_combinations_profit3.json'
                with open(file1, 'r') as file1:
                    data_f1 = json.load(file1)

                with open(file2, 'r') as file2:
                    data_f2 = json.load(file2)

                diffs = {i: data_f1[i] for i in data_f1 if i in data_f2 and data_f1[i] != data_f2[i]}
                if len(diffs):
                    for key, value in diffs.items():
                        print(f'{key}: {value} \n -> \n  {key}: {data_f2[key]}')
            else:
                continue


# class Test_get_chrt_data:
#     app = Application()
#
#     app.login()
#
#     def test_Apps_ordinary_cost(self):
#         LOGGER.info("Дерагем ручку графика")
#         charts_data = self.app.actions.get_charts(type='cost').json()
#         with open("31102023ordinary_cost.json", "w") as f:
#             json.dump(charts_data, f, indent=4)
#
#     def test_Apps_classification(self):
#         LOGGER.info("Дерагем ручку графика")
#         charts_data = self.app.actions.get_charts(type='classification').json()
#         with open("31102023apps_classification.json", "w") as f:
#             json.dump(charts_data, f, indent=4)
#
#     def test_Sent_combinations_profit(self):
#         LOGGER.info("Дерагем ручку графика")
#         charts_data = self.app.actions.get_charts(type='profit').json()
#         with open("31102023sent_combinations_profit.json", "w") as f:
#             json.dump(charts_data, f, indent=4)
#
#     def test_Rejected_combinations_by_reason(self):
#         LOGGER.info("Дерагем ручку графика")
#         charts_data = self.app.actions.get_charts(type='reject_reason').json()
#         with open("31102023rejected_combinations_by_reason.json", "w") as f:
#             json.dump(charts_data, f, indent=4)
#
#     def test_Combinations_in_work_share(self):
#         LOGGER.info("Дерагем ручку графика")
#         charts_data = self.app.actions.get_charts(type='share').json()
#         with open("31102023combinations_in_work_share.json", "w") as f:
#             json.dump(charts_data, f, indent=4)
#
#     def test_Combinations_in_work_status(self):
#         LOGGER.info("Дерагем ручку графика")
#         charts_data = self.app.actions.get_charts(type='status').json()
#         with open("31102023combinations_in_work_status.json", "w") as f:
#             json.dump(charts_data, f, indent=4)
#
#     def test_Rejected_approved_by_route_type(self):
#         LOGGER.info("Дерагем ручку графика")
#         charts_data = self.app.actions.get_charts(type='reject_route').json()
#         with open("31102023rejected_approved_by_route_type.json", "w") as f:
#             json.dump(charts_data, f, indent=4)
#
#     def test_average_count_hourly(self):
#         LOGGER.info("Дерагем ручку графика")
#         charts_data = self.app.actions.get_charts(type='average_count_hourly').json()
#         with open("31102023average_count_hourly.json", "w") as f:
#             json.dump(charts_data, f, indent=4)
#
#     def test_apps_average_count(self):
#         LOGGER.info("Дерагем ручку графика")
#         charts_data = self.app.actions.get_charts(type='apps_average_count').json()
#         with open("31102023apps_average_count.json", "w") as f:
#             json.dump(charts_data, f, indent=4)


if __name__ == '__main__':
    get_diff_in_results()
