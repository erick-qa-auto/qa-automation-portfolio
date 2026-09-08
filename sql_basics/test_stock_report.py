from stock_report import count_brand, brands

def test_carel_count():
    assert count_brand("Carel") == 2

def test_danfoss_count():
    assert count_brand("Danfoss") == 2

def test_unox_count():
    assert count_brand("Unox") == 1

def test_unknown_brand():
    assert count_brand("Bosch") == 0

def test_total_items():
    assert len(brands) == 6
