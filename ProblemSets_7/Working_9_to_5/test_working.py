from working import convert
import pytest

def test_convert():
    assert convert("10:00 AM to 11:30 AM") == "10:00 to 11:30"
    assert convert("12:30 PM to 01:00 PM") == "12:30 to 13:00"
    assert convert("11:59 PM to 12:00 AM") == "23:59 to 00:00"

    with pytest.raises(ValueError):
        convert(" to ")
    with pytest.raises(ValueError):
        convert("0 AM to 0 PM")
    with pytest.raises(ValueError):
        convert("10:00AM 11:30AM")
    with pytest.raises(ValueError):
        convert("13:65 AM to 11:70")