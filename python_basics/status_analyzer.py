def analyzer_status(code):
    if code == 200:
        return "ok"
    elif code == 201:
        return "created"
    elif code == 400:
        return "bad request"
    elif code == 404:
        return "not found"
    elif code == 429:
        return "limit requests"
    elif 400 <= code <= 499:
        return "ошибка клиента" 
    elif 500 <= code <= 599:
        return "ошибка сервера"
    else:
        return "неизвестная ошибка"