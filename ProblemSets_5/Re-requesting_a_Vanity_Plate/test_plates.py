from plates import is_valid

def test_is_valid():
    assert is_valid('CS50')
    assert not is_valid('CS05')
    assert not is_valid('longvanityplates')
    assert not is_valid('70')
    assert not is_valid('GS3WAR')
    assert not is_valid('GG.AI5')