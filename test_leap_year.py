#условие високосного года
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

#test 1 граничное значение
def test_is_leap_year_boundary ():
    assert is_leap_year(2024) == True
    assert is_leap_year(2023) == False

#test 2 негативный тест
def test_is_leap_year_negativ ():
    assert is_leap_year(1900) == False
    assert is_leap_year(0) == True
    assert is_leap_year(578824234235235234234235425342) == False

#test 3 позитивный тест классом эквивалентности
def test_is_leap_year_positive ():
    assert is_leap_year(1999) == False
    assert is_leap_year(2004) == True
    assert is_leap_year(3026) == False
    assert is_leap_year(2026) == False
    assert is_leap_year(2028) == True
    
