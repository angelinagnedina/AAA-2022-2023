from what_is_year_now import what_is_year_now
from unittest.mock import patch


def test_ymd():
    with patch('what_is_year_now.urllib.request') as get_date:
        get_date.return_value.urlopen = lambda x: ''
        with patch("what_is_year_now.json.load") as load_data:
            load_data.return_value = {'currentDateTime': '2022-11-13T19:59Z'}
            assert what_is_year_now() == 2022


def test_dmy():
    with patch('what_is_year_now.urllib.request') as get_date:
        get_date.return_value.urlopen = lambda x: ''
        with patch("what_is_year_now.json.load") as load_data:
            load_data.return_value = {'currentDateTime': '13.11.2022T19:59Z'}
            assert what_is_year_now() == 2022


def test_value_error():
    with patch('what_is_year_now.urllib.request') as get_date:
        get_date.return_value.urlopen = lambda x: ''
        with patch("what_is_year_now.json.load") as load_data:
            load_data.return_value = {'currentDateTime': '13@11@2022T19:59Z'}
            try:
                what_is_year_now()
            except ValueError:
                pass
