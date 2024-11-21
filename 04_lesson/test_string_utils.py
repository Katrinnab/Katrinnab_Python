import pytest
from stringutils import StringUtils

string_utils = StringUtils()


@pytest.mark.parametrize('string, result', [('skypro', 'Skypro'),
                                            ('hello, World', 'Hello, World'),
                                            ('   ', '   '),
                                            ('123skypro', '123skypro')])
def test_cap(string, result):
    string_utils = StringUtils()
    res = string_utils.capitalize(string)
    assert res == result


@pytest.mark.parametrize('string, result', [(' skypro', 'skypro'),
                                            ('_skypro', '_skypro'),
                                            ('s kypro', 's kypro'),
                                            ('   1234   ', '1234   '),
                                            ('   ', '')])
def test_trim(string, result):
    string_utils = StringUtils()
    res = string_utils.trim(string)
    assert res == result


@pytest.mark.parametrize('string, delimeter, result',
                         [('Я иду спать', ' ', ['Я', 'иду', 'спать']),
                             ('1234', ' ', ['1234']),
                             ('1:2:3:4', ':', ['1', '2', '3', '4']),
                             ('23456', '', ['23456'])])
def test_to_list(string, delimeter, result):
    string_utils = StringUtils()
    res = string_utils.to_list(string, delimeter)
    assert res == result


@pytest.mark.parametrize('string, symbol, result', [('skypro', '$', False),
                         ('Skypro', 's', False), ('Skypro', 'S', True),
                         ('   ', 'j', True)])
def test_contains(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.contains(string, symbol)
    assert res == result


@pytest.mark.parametrize('string, symbol, result', [(' Skypro', ' ', 'Skypro'),
                                                    (' ', ' ', ''),
                                                    ('', '', ''),
                                                    ('', 'jfyj', '')])
def test_del_symbol(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.delete_symbol(string, symbol)
    assert res == result


@pytest.mark.parametrize('string, symbol, result', [('12gdjg', '1', True),
                                                    (' fjfyj', ' ', True),
                                                    ('', '', True),
                                                    ('stop', '', True),
                                                    ('start', 't', False)])
def test_starts_with(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.starts_with(string, symbol)
    assert res == result


@pytest.mark.parametrize('string, symbol, result', [('12345', '5', True),
                                                    ('@#%$', '$', True),
                                                    (' ', ' ', True),
                                                    ('', '', True),
                                                    ('test ', 't', True)])
def test_end_with(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.end_with(string, symbol)
    assert res == result


@pytest.mark.parametrize('string, result', [('Star', False), ('', True),
                                            (' ', True), ('___', False),
                                            ('   _', False), (None, True)])
def test_is_empty(string, result):
    string_utils = StringUtils()
    res = string_utils.is_empty(string)
    assert res == result


@pytest.mark.parametrize('lst, joiner, result', [([1, 2, 3, 4, 5],
                                                  ',', '1,2,3,4,5'),
                                                 ([], ' ', ''),
                                                 (['a', 'b', 'c', 'd'],
                                                  ' ', 'a b c d'),
                                                 ([None, '', ''], None, ''),
                                                 (['Pro', 'Sky'],
                                                  '-', 'Pro-Sky')])
def test_list_to_string(lst, joiner, result):
    string_utils = StringUtils()
    res = string_utils.list_to_string(lst, joiner)
    assert res == result
