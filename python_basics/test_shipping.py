from shipping import calculate_shipping_cost


# test 1 positive situations weight
def test_shipping_normal_weight():
    result = calculate_shipping_cost(0.5, 10)
    assert result == 8.0
    result = calculate_shipping_cost(2.5, 10)
    assert result == 11.0
    result = calculate_shipping_cost(15, 10)
    assert result == 16.0
    result = calculate_shipping_cost(30, 10)
    assert result == 26.0

# test 2 positive situation weight with express
def test_shipping_normal_weight_express():
    result = calculate_shipping_cost(0.5, 10, True)
    assert result == 12.0
    result = calculate_shipping_cost(2.5, 10, True)
    assert result == 16.5
    result = calculate_shipping_cost(15, 10, True)
    assert result == 24.0
    result = calculate_shipping_cost(30, 10, True)
    assert result == 39.0

# test 3 boundary shipping weight
def test_shipping_boundary_normal_weight():
    result = calculate_shipping_cost(1, 10)
    assert result == 8.0
    result = calculate_shipping_cost(5, 50)
    assert result == 15.0
    result = calculate_shipping_cost(20, 100)
    assert result == 25.0
    result = calculate_shipping_cost(21, 200)
    assert result == 45.0

# test 4 negative situations weight & distance
def test_shipping_weight_distance():
    result = calculate_shipping_cost(0, 0)
    assert result == None
    result = calculate_shipping_cost(-1, -1, True)
    assert result == None
    result = calculate_shipping_cost(5, 0)
    assert result == None
    result = calculate_shipping_cost(0, 10)
    assert result == None