import json
from datetime import datetime


def get_sorted_operation_list():
    with open('/home/vadim/PycharmProjects/course_work_3/src/operations.json') as file:
        operation_dict = json.load(file)
        five_operation = {}
        operation_list = []
        iteration = 0
        for operation in operation_dict:
            while len(five_operation) < 5:
                if operation['state'] == 'EXECUTED':
                    iteration += 1
                    five_operation[iteration] = operation
                    break
    for operation in five_operation:
        operation_list.append(five_operation[operation])

    sorted_operation_list = sorted(
        operation_list,
        key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse=True
    )
    return sorted_operation_list

def get_date(dict):
    dict["date"]
    year = dict['date'][0:4]
    month = dict['date'][5:7]
    day = dict['date'][8:10]
    return f'{str(day)}.{str(month)}.{str(year)}'


def get_description(dict):
    return dict['description']


def get_card_info(dict):
    if 'from' in dict:
        card_name = dict['from'][:-17]
        card_num = dict['from'][-16:]
        acc_num = dict['to']
        return (f'{card_name} {card_num[0:4]} {card_num[4:6]}** **** {card_num[12:]} -> {acc_num[0:4]} **{acc_num[-4:]}')
    return (f'''Нет информации о номере карты -> {dict['to'][0:4]} **{dict['to'][-4:]}''')

def get_sum(dict):
    return f'''{dict['operationAmount']['amount']} {dict['operationAmount']['currency']['name']}'''

