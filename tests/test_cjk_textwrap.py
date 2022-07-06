from cjk_textwrap import __version__, wrap


def test_non_cjk_textwrap():
    test_cases = {
        'Hello, world!': ['Hello, world!'],
        'Hello, world!\n': ['Hello, world!'],
        'What is your name? My name is carbenee!': ['What is your', 'name? My name is', 'carbenee!']
    }
    for k, v in test_cases.items():
        assert wrap(k, width=17, break_long_words=True, cjk_mode=False) == v


def test_chinese_textwrap():
    test_cases = {
        '我买了一件T恤，它的颜色是红色，它的价格是100元。':
        ['我买了一件', 'T恤，它的', '颜色是红色，', '它的价格是', '100元。'],
    }
    for k, v in test_cases.items():
        assert wrap(k, width=6, break_long_words=True) == v


def test_version():
    assert __version__ == '0.1.0'
