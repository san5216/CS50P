import pytest
from seasons import main, date_difference


def test_date_difference():
    with pytest.raises(SystemExit):
        assert date_difference("1982/01*09")


