from src.utils import get_date, get_description, get_card_info, get_sum
def test_get_date():
    assert get_date('2020-10-19') == '19.10.2020'