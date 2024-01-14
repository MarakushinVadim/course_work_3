from src.utils import get_date, get_description, get_card_info, get_sum
from src.main import sorted_operation_list

def test_get_date():
    assert get_date(sorted_operation_list[0]) == '26.08.2019'

def test_get_description():
    assert get_description(sorted_operation_list[0]) == 'Перевод организации'
    assert get_description(sorted_operation_list[2]) == 'Перевод со счета на счет'
    assert get_description(sorted_operation_list[4]) == 'Открытие вклада'

def test_get_card_info():
    assert get_card_info(sorted_operation_list[0]) == 'Maestro 1596 83** **** 5199 -> Счет **9589'
    assert get_card_info(sorted_operation_list[4]) == 'Нет информации о номере карты -> Счет **2431'

def test_get_sum():
    assert get_sum(sorted_operation_list[0]) == '31957.58 руб.'