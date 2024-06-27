import pytest
from lesson_4 import StringUtils

#Тесты функции capitilize 
#Позитивные
@pytest.mark.positive_test
@pytest.mark.parametrize("str1, result",
[("тест", "Тест"),
 ("test", "Test"),
 ("skypro test", "Skypro test"),
 ("04 апреля 2023","04 апреля 2023"),
 ("%@#%#*&%","%@#%#*&%")])
def test_capitilize_positive(str1, result):
    utils = StringUtils()
    res = utils.capitilize(str1)
    assert res == result

#Негативые
@pytest.mark.negative_test
@pytest.mark.parametrize("str1, result",
[("",""),
 (" "," "),
 ("123","123"),
 ("Test", "Test")])
def test_capitilize_negative(str1, result):
    utils = StringUtils()
    res = utils.capitilize(str1)
    assert res == result

#Тесты функции trim
#Позитивные
@pytest.mark.positive_test
@pytest.mark.parametrize("str1, result",
[(" тест", "тест"),
 ("  test", "test"),
 (" 132", "132"),
 ("  04 апреля 2023","04 апреля 2023"),
 ("  $@#!$^&", "$@#!$^&")])
def test_trim_positive(str1, result):
    utils = StringUtils()
    res = utils.trim(str1)
    assert res == result

#Негативые
@pytest.mark.negative_test
@pytest.mark.parametrize("str1",
[(123),
 (None)])
def test_trim_negative_no_string(str1):
    utils = StringUtils()
    with pytest.raises(AttributeError):
        utils.trim(str1)

@pytest.mark.negative_test
@pytest.mark.parametrize("str1, result",
[("",""),
 (" ",""),
 ("123","123"),
 ("Test", "Test")])
def test_trim_negative(str1, result):
    utils = StringUtils()
    res = utils.trim(str1)
    assert res == result

#Тесты функции to_list
#Позитивные
@pytest.mark.positive_test
@pytest.mark.parametrize("str1, result",
[("т,е,с,т", ["т","е","с","т"]),
 ("t,e,s,t", ["t","e","s","t"]),
 ("s,k,y, ,p,r,o,1", ["s","k","y"," ","p","r","o","1"]),
 ("1,2,3", ["1","2","3"])])
def test_to_list_positive_default(str1, result):
    utils = StringUtils()
    res = utils.to_list(str1)
    assert res == result

#Негативые
@pytest.mark.negative_test
@pytest.mark.parametrize("str1",
[(1,2,3),
 (None,None)])
def test_to_list_negative_no_string(str1):
    utils = StringUtils()
    with pytest.raises(AttributeError):
        utils.to_list(str1)


#Тесты функции to_list
#Позитивные
@pytest.mark.positive_test
@pytest.mark.parametrize("str1, src, result",
[('Тест', 'е', True),
 ("123", "2", True),
 ("04 апреля 2023", "а", True)])
def test_contains_positive(str1, src, result):
    utils = StringUtils()
    res = utils.contains(str1, src)
    assert res == result 

#Негативные
@pytest.mark.negative_test
@pytest.mark.parametrize("str1, src, result",
[("", "", ""),
 (" ", " ", " "),
 (None, None, "")])
def test_contains_negative(str1, src, result):
    utils = StringUtils()
    res = utils.contains(str1, src)
    assert res == result
