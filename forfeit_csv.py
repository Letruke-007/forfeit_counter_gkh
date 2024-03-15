import csv
import datetime
from datetime import date

csv.register_dialect('comma_no_quote', delimiter=',', quoting=csv.QUOTE_NONE, escapechar='\\')
csv.register_dialect('semicolon_quote_all', delimiter=';', quoting=csv.QUOTE_ALL)


def reader(file):
    with open(file, encoding='UTF-8') as f:
        reader_file = csv.reader(f, dialect='semicolon_quote_all')
        data = list(reader_file)
        header = data.pop(0)
        return data


def delete_data(file):
    with open(file, 'w') as f:
        writer_file = csv.writer(f, dialect='semicolon_quote_all')
        writer_file.writerow('')


def writer(file, row):
    with open(file, 'a', encoding='UTF-8-sig') as f:
        writer_file = csv.writer(f, dialect='semicolon_quote_all')
        writer_file.writerow(row)


def finder(file):
    finder_init = input('Введите текст для поиска в базе данных: ')
    counter = 0
    result_list = []
    for row in file:
        for i in row:
            if finder_init in i:
                counter += 1
                result_list.append(row)
    request = input(f'Найдено {counter} записей в реестре. Вывести их на печать (y/n)?: ')
    if request.lower() == 'y':
        for i in result_list:
            print(i)


def forfeit(file, name):
    counter = 0
    forfeit_result = 0

    for row in file:
        account_number = row[4]

        if counter == 0 and name == account_number:
            writer('files/result.csv', ['Расчет пени  ', '', '', '', '', '', '', ''])
            writer('files/result.csv', ['Лицевой счет:', row[4], '', '', '', '', '', '', ''])
            writer('files/result.csv', ['Адрес:       ', row[3], '', '', '', '', '', '', ''])
            writer('files/result.csv', ['Должник:     ', row[7], '', '', '', '', '', '', ''])
            counter += 1

        if name == account_number:
            debt = int(row[24])
            month = int(row[19][:2])
            if month // 10 < 1:
                month = int(month) % 10
            year = int(row[19][3:])
            first_date = date(year, month + 1, 11)

            interest_rate = 9.5
            null_forfeit_period_start = date(year, month, 11)
            low_forfeit_period_end = first_date + datetime.timedelta(60)

            difference = int(str(date.today() - first_date)[:3])

            if difference > 90:
                low_forfeit_period_amount = float('{:.2f}'.format((debt * (interest_rate / 100 / 300) * 60)))
                high_forfeit_period_amount = float(
                    '{:.2f}'.format((debt * (interest_rate / 100 / 130) * (difference - 90))))
                forfeit_result += (low_forfeit_period_amount + high_forfeit_period_amount)
            else:
                low_forfeit_period_amount = float(
                    '{:.2f}'.format((debt * (interest_rate / 100 / 300)) * (difference - 30)))
                high_forfeit_period_amount = 0
                forfeit_result += (low_forfeit_period_amount + high_forfeit_period_amount)

            writer('files/result.csv',
                   [f'Задолженность:', 'с', 'по', 'Дней', 'Ставка', 'Доля ставки',
                    'Формула', 'Пени'])
            writer('files/result.csv',
                   [debt, null_forfeit_period_start, first_date, 30, interest_rate, 0, f'{debt} * 30 * 9.5 * 0', 0])
            writer('files/result.csv',
                   [debt, first_date, low_forfeit_period_end, 60, interest_rate, '1 / 300',
                    f'{debt} * 60 * 9.5 * 1/300',
                    low_forfeit_period_amount])
            writer('files/result.csv',
                   [debt, low_forfeit_period_end, date.today(), (difference - 90), interest_rate, '1 / 130',
                    f'{debt} * {difference - 90} * 9.5 * 1/130', high_forfeit_period_amount])
            writer('files/result.csv',
                   ['', '', '', '', '', '', 'ИТОГО',
                    '{:.2f}'.format(high_forfeit_period_amount + low_forfeit_period_amount)])
    writer('files/result.csv',
           ['ВСЕГО долг:', {debt}, '', '', '', '', 'ВСЕГО, неустойка:', '{:.2f}'.format(forfeit_result)])


# finder(reader('files/reestr.csv'))
delete_data('files/result.csv')
forfeit(reader('files/reestr.csv'), '987654321')

