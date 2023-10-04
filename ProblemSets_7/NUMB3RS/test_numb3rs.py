from numb3rs import validate

def test_validate():
    assert validate('255.255.255.255')
    assert validate('1.2.3.255')
    assert validate('2.2.2.2')
    assert validate('128.1.245.12')
    assert not validate('255.255.')
    assert not validate('dog')
    assert not validate('275')
    assert not validate('1.2.285.512')