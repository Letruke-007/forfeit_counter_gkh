import pandas as pd

# import csv
import datetime
# from datetime import date
#
# csv.register_dialect('comma_no_quote',  delimiter=',', quoting=csv.QUOTE_NONE, escapechar='\\')
# csv.register_dialect('semicolon_quote_all',  delimiter=';', quoting=csv.QUOTE_ALL)
#
# def reader(file):
#     with open(file, encoding='UTF-8') as f:
#         reader_file = csv.reader(f, dialect='semicolon_quote_all')
#         reestr = list(reader_file)
#         header = reestr.pop(0)
#         return reestr
#
# def writer(file, row):
#     with open(file, 'a') as f:
#         writer = csv.writer(f, dialect='semicolon_quote_all')
#         writer.writerow(row)
#
# def finder(file):
#     finder_init = input('Введите текст для поиска в базе данных: ')
#     counter = 0
#     result_list = []
#     for row in file:
#         for i in row:
#             if finder_init in i:
#                 counter += 1
#                 result_list.append(row)
#     request = input(f'Найдено {counter} записей в реестре. Вывести их на печать (y/n)?: ')
#     if request.lower() == 'y':
#         for i in result_list:
#             print(i)
#
#
# def forfeit(file, debtors):
#     count_id = file[0][4]
#     print(count_id)
#     counter = 0
#     forfeit_total = 0
#     fieldnames = []
#     for name in debtors:
#         for row in file:
#             if name == row[7]:
#                 debt = int(row[24])
#                 month = int(row[19][:2])
#                 if month // 10 < 1:
#                     month = int(month) % 10
#                 year = int(row[19][3:])
#                 first_date = date(year, month + 1, 11)
#
#                 if row[4] != count_id:
#                     counter = 0
#                     count_id = row[4]
#
#                 if counter == 0:
#                     writer('files/result.csv', ['Расчет пени за коммунальные услуги (ст. 155 ЖК РФ)'])
#                     writer('files/result.csv', [f'Номер лицевого счета: {count_id}'])
#                     writer('files/result.csv', [f'Адрес:                {row[3]}'])
#                     writer('files/result.csv', [f'Должник:              {row[7]}'])
#                     counter += 1
#
#                 if row[4] == count_id:
#                     counter += 1
#                     interest_rate = {date.today(): 9.5}
#                     low_forfeit_period_end = first_date + datetime.timedelta(60)
#                     for key, val in interest_rate.items():
#                         difference = int(str(key - first_date)[:3])
#                         if difference > 90:
#                             low_forfeit_period_amount = float('{:.2f}'.format((debt * (val / 100 / 300) * 60)))
#                             high_forfeit_period_amount = float('{:.2f}'.format((debt * (val / 100 / 130) * (difference - 90))))
#                         else:
#                             low_forfeit_period_amount = float('{:.2f}'.format((debt * (val / 100 / 300)) * (difference - 30)))
#                             high_forfeit_period_amount = 0
#
#                     writer('files/result.csv', [['Задолженность'], ['с'], ['по'], ['Дней'], ['Ставка'], ['Доля ставки'], ['Сумма неустойки, руб.']])
#                     writer('files/result.csv', [*[debt], *[first_date], *[low_forfeit_period_end], *[60], *[9.5], *[1/300], *[low_forfeit_period_amount + high_forfeit_period_amount]])
#
#
#
# debtors_list = []
# for i in (reader('files/reestr.csv')):
#     if i[7] not in debtors_list:
#         debtors_list.append(i[7])
#
# # finder(reader('files/reestr.csv'))
#
# forfeit(reader('files/reestr.csv'), debtors_list)


reader = pd.read_csv('C:/Users/Anton/PycharmProjects/pythonProject12/files/reestr.csv', sep=';')
dates = []

reader = [reader]
print(reader)


def convert_date(val):
    new_val = int(val.replace('.', ''))
    print(new_val)

