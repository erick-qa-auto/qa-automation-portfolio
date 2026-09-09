from cart_calculator import get_total_price

def test_total_price():
    assert get_total_price([1500, 2000, 500, 3000]) == 7000

def test_total_price_with_zero():
    assert get_total_price([100, 0, 200]) == 300

def test_total_price_empty():
    assert get_total_price([]) == 0