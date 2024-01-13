import json
from datetime import datetime

with open('operations.json') as file:
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

operation_list = sorted(
    operation_list,
    key=lambda x: datetime.strptime(x['date'], '%Y-%m-%d %H:%M:%S'), reverse=False
)
print(operation_list)