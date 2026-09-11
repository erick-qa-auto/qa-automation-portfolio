from analyze_defects import get_analyze_defects

def test_positive_analyze_defects():
    assert get_analyze_defects([2, 5, 1, 12, 8, 3, 20]) == (2, 51)
    