from twttr import shorten

def test_shorten():
    assert shorten('Twitter') == 'Twttr'
    assert shorten('H3LL0, w0rld') == 'H3LL0, w0rld'
    assert shorten('amarjeet') == 'mrjt'
    assert shorten('RASENGAN') == 'RSNGN'