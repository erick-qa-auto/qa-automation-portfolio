from thermostat import count_overheating, temps

def test_count_overheating_temps():
    assert count_overheating(temps, 15) == 2

def test_count_overheating_normal():
    assert count_overheating([10, 12, 14], 15) == 0

def test_count_overheating_alarm():
    assert count_overheating([20, 30, 40], 15) == 3

def test_count_overheating_bonduary_limit():
    assert count_overheating([14], 15) == 0
    assert count_overheating([16], 15) == 1
    assert count_overheating([15], 15) == 1