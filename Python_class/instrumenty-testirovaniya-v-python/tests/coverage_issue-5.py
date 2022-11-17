from what_is_year_now import what_is_year_now
from unittest.mock import patch
import io


def test_ymd():
    with patch('what_is_year_now.urllib.request.urlopen',
               return_value=io.StringIO('{"currentDateTime": "2022-11-13T19:59Z"}')) as get_date:
        assert what_is_year_now() == 2022


def test_dmy():
    with patch('what_is_year_now.urllib.request.urlopen',
               return_value=io.StringIO('{"currentDateTime": "13.11.2022T19:59Z"}')) as get_date:
        assert what_is_year_now() == 2022


def test_value_error():
    with patch('what_is_year_now.urllib.request.urlopen',
               return_value=io.StringIO('{"currentDateTime": "13@11@2022T19:59Z"}')) as get_date:
        try:
            what_is_year_now()
        except ValueError:
            pass
