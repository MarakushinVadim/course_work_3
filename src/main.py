from src.utils import get_date, get_description, get_card_info, get_sum, get_sorted_operation_list
# Импортируем необходимые функции

# Создаем переменную список словарей
sorted_operation_list = get_sorted_operation_list()

# Запускаем тело цикла
for operation in range(5):
    print(f'''{get_date(sorted_operation_list[operation])} {get_description(sorted_operation_list[operation])}
{get_card_info(sorted_operation_list[operation])}
{get_sum(sorted_operation_list[operation])}
''')
    print()
# Наслаждаемся результатом
