from parking_fee import parking_cost

def test_parking_cost_normal():
    result = parking_cost(15)
    assert result == 50



def test_parking_cost_zerro():
    result = parking_cost(0)
    assert result == None

def test_parking_cost_bonduary():
    result = parking_cost(1)
    assert result == 50