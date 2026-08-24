
# Функция, которую мы тестируем
def is_even(number):
    """Возвращает True, если число чётное"""
    return number % 2 == 0


# Тест 1: проверяем чётные числа
def test_is_even_with_even_number():
    assert is_even(2) == True
    assert is_even(4) == True
    assert is_even(0) == True


# Тест 2: проверяем нечётные числа
def test_is_even_with_odd_number():
    assert is_even(1) == False
    assert is_even(3) == False
    assert is_even(7) == False