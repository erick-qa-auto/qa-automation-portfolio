'функция которая тестируется'
def is_adult(age):
    return age >= 18

'тест 1: проверим что точно взрослый'
def test_is_adult_with_adult_edge ():
    assert is_adult(19) == True
    assert is_adult(25) == True
    assert is_adult(40) == True

'тест 2: проверим что точно ребёнок'
def test_is_adult_with_child_age ():
    assert is_adult(16) == False
    assert is_adult(10) == False
    assert is_adult(8) == False

'тест 3: граничное значение'
def test_is_adult_boundary ():
    assert is_adult(18) == True
    assert is_adult(17) == False
    