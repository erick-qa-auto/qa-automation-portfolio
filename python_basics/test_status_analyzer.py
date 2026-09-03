from status_analyzer import analyzer_status

def test_status_200():
    assert analyzer_status(200) == "ok"

def test_status_201():
    assert analyzer_status(201) == "created"

def test_status_400():
    assert analyzer_status(400) == "bad request"

def test_status_404():
    assert analyzer_status(404) == "not found"

def test_status_429():
    assert analyzer_status(429) == "limit requests"

def test_status_400_to_499():
    for code in [401, 403, 418, 499]:
        assert analyzer_status(code) == "ошибка клиента"


def test_boundary_499_500():
    assert analyzer_status(499) == "ошибка клиента"
    assert analyzer_status(500) == "ошибка сервера"

def test_boundary_400():
    assert analyzer_status(399) == "неизвестная ошибка"
    assert analyzer_status(400) == "bad request"

def test_status_500_to_599():
    for code in [501, 503, 520, 555, 599]:
        assert analyzer_status(code) == "ошибка сервера"

def test_boundary_599_600():
    assert analyzer_status(599) == "ошибка сервера"
    assert analyzer_status(600) == "неизвестная ошибка"