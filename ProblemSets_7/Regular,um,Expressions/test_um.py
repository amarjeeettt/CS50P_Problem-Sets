from um import count

def test_count():
    assert count('I\'m ummm fine') == 0
    assert count('Um...can you repeat that?') == 1
    assert count('uM, helL0') == 1