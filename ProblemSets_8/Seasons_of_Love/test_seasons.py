from seasons import convert_time

def test_convert():
    assert convert_time('2001-06-07') == "Eleven million, seven hundred thousand minutes"
    assert convert_time('2020-06-01') == "One million, seven hundred fifteen thousand forty minutes"