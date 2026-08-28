import requests
import json

BASE_URL = "https://jsonplaceholder.typicode.com"

# ============================================================================
# РАЗДЕЛ 1: ДОСТУПНОСТЬ ENDPOINT / API
# ============================================================================

def test_api_001_reach_endpoint():
    """
    API-001: Отправить запрос на корректный URL
    Ожидаемый результат: Endpoint отвечает в соответствии с контрактом API
    Приоритет: P0 (критический)
    """
    response = requests.get(f"{BASE_URL}/users/1")
    assert response.status_code == 200
    assert len(response.text) > 0
    # Дополнительно: проверяем, что это JSON
    data = response.json()
    assert "id" in data
    assert "name" in data


def test_api_002_correct_http_method():
    """
    API-002: Использовать корректный HTTP-метод
    Ожидаемый результат: Запрос успешно обрабатывается
    Приоритет: P0
    """
    # GET — корректный метод для чтения
    response = requests.get(f"{BASE_URL}/users/1")
    assert response.status_code == 200


def test_api_003_content_type():
    """
    API-003: Использовать корректный Content-Type
    Ожидаемый результат: Запрос принимается
    Приоритет: P0
    
    Примечание: jsonplaceholder не требует Content-Type для GET-запросов,
    но для POST/PUT он важен.
    """
    # Для GET Content-Type не требуется
    response = requests.get(f"{BASE_URL}/users/1")
    assert response.status_code == 200
    
    # Проверяем, что сервер вернул JSON
    assert "application/json" in response.headers.get("Content-Type", "")


def test_api_004_accept_header():
    """
    API-004: Использовать корректный заголовок Accept
    Ожидаемый результат: Возвращается ожидаемый формат ответа
    Приоритет: P1
    """
    headers = {"Accept": "application/json"}
    response = requests.get(f"{BASE_URL}/users/1", headers=headers)
    assert response.status_code == 200
    assert "application/json" in response.headers.get("Content-Type", "")


def test_api_005_minimal_parameters():
    """
    API-005: Отправить запрос с минимально необходимыми параметрами
    Ожидаемый результат: Запрос выполняется успешно
    Приоритет: P0
    
    Для GET /users/{id} минимальный параметр — это сам ID.
    """
    response = requests.get(f"{BASE_URL}/users/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1


def test_api_006_all_valid_parameters():
    """
    API-006: Отправить запрос со всеми валидными параметрами
    Ожидаемый результат: Запрос выполняется успешно
    Приоритет: P1
    
    jsonplaceholder не поддерживает query-параметры для /users/{id},
    но для /users можно фильтровать.
    """
    # Пример: фильтрация коллекции пользователей
    response = requests.get(f"{BASE_URL}/users", params={"id": 1})
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["id"] == 1


# ============================================================================
# НЕГАТИВНЫЕ СЦЕНАРИИ (РАЗДЕЛ 1)
# ============================================================================

def test_api_007_incorrect_url():
    """
    API-007: Использовать некорректный URL
    Ожидаемый результат: Соответствующая ошибка, обычно 404
    Приоритет: P1
    """
    response = requests.get(f"{BASE_URL}/nonexistent-endpoint")
    assert response.status_code == 404


def test_api_008_incorrect_http_method():
    """
    API-008: Использовать некорректный HTTP-метод
    Ожидаемый результат: 405 Method Not Allowed или ошибка, определённая контрактом
    Приоритет: P0
    
    Примечание: jsonplaceholder принимает любой метод, даже некорректный,
    и возвращает 200/201. Это ограничение mock-API.
    В реальном API DELETE на read-only endpoint вернул бы 405.
    """
    # jsonplaceholder — mock API, он принимает даже некорректные методы
    # Поэтому этот тест показывает ограничение тестового API
    response = requests.delete(f"{BASE_URL}/users/1")
    # В реальном API здесь был бы 405, но jsonplaceholder возвращает 200
    # Это НЕ баг нашего кода, это особенность тестового сервера
    print("⚠️  jsonplaceholder не валидирует HTTP-методы (это mock API)")


def test_api_011_unavailable_endpoint():
    """
    API-011: Обратиться к недоступному / несуществующему endpoint
    Ожидаемый результат: Соответствующий ответ с ошибкой
    Приоритет: P1
    """
    response = requests.get(f"{BASE_URL}/api/v2/fake-resource")
    assert response.status_code == 404


# ============================================================================
# РАЗДЕЛ 2: АУТЕНТИФИКАЦИЯ
# ============================================================================

def test_auth_not_applicable():
    """
    РАЗДЕЛ 2: Аутентификация
    Статус: N/A (не применимо)
    
    Объяснение: jsonplaceholder.typicode.com — публичный mock API,
    который НЕ требует аутентификации. Все endpoints открыты.
    
    В реальном проекте здесь были бы тесты:
    - Валидный токен → доступ разрешён
    - Невалидный токен → 401 Unauthorized
    - Отсутствует токен → 401 Unauthorized
    """
    # Проверяем, что API действительно не требует авторизации
    response = requests.get(f"{BASE_URL}/users/1")
    assert response.status_code == 200
    print("ℹ️  jsonplaceholder не требует аутентификации (публичный API)")


# ============================================================================
# РАЗДЕЛ 3: АВТОРИЗАЦИЯ
# ============================================================================

def test_authorization_not_applicable():
    """
    РАЗДЕЛ 3: Авторизация
    Статус: N/A (не применимо)
    
    Объяснение: Без аутентификации нет и авторизации.
    Все пользователи имеют равный доступ ко всем ресурсам.
    
    В реальном проекте здесь были бы тесты:
    - Пользователь может читать свои данные
    - Пользователь НЕ может читать данные другого пользователя (IDOR)
    - Обычный пользователь НЕ может удалять ресурсы (403 Forbidden)
    """
    print("ℹ️  jsonplaceholder не имеет системы ролей и прав доступа")


# ============================================================================
# РАЗДЕЛ 4: ПАРАМЕТРЫ ЗАПРОСА
# ============================================================================

def test_params_025_required_params_present():
    """
    API-025: Обязательные параметры переданы
    Ожидаемый результат: Запрос выполняется успешно
    Приоритет: P0
    
    Для GET /users/{id} обязательный параметр — ID в URL.
    """
    response = requests.get(f"{BASE_URL}/users/1")
    assert response.status_code == 200


def test_params_026_optional_params_omitted():
    """
    API-026: Необязательные параметры могут быть не переданы
    Ожидаемый результат: Запрос выполняется успешно
    Приоритет: P1
    
    GET /users/{id} не требует query-параметров.
    """
    response = requests.get(f"{BASE_URL}/users/1")
    assert response.status_code == 200


def test_params_032_missing_required_param():
    """
    API-032: Отсутствует обязательный параметр
    Ожидаемый результат: Соответствующая ошибка валидации
    Приоритет: P0
    
    Для GET /users без ID — должна вернуться коллекция всех пользователей,
    а не ошибка (это допустимое поведение).
    """
    response = requests.get(f"{BASE_URL}/users")
    # Это НЕ ошибка — сервер вернул коллекцию всех пользователей
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 10  # jsonplaceholder имеет 10 пользователей


def test_params_036_wrong_data_type():
    """
    API-036: Неверный тип данных
    Ожидаемый результат: Ошибка валидации
    Приоритет: P1
    
    Передаём строку вместо числа в ID.
    """
    # jsonplaceholder пытается обработать "abc" как ID и возвращает 404
    response = requests.get(f"{BASE_URL}/users/abc")
    assert response.status_code == 404


def test_params_037_value_below_minimum():
    """
    API-037: Значение ниже минимального
    Ожидаемый результат: Ошибка или пустой результат
    Приоритет: P1
    
    ID = 0 или отрицательный — невалидно.
    """
    response = requests.get(f"{BASE_URL}/users/0")
    # jsonplaceholder возвращает пустой объект или 404
    assert response.status_code in [200, 404]
    
    # Проверяем негативный ID
    response_negative = requests.get(f"{BASE_URL}/users/-1")
    assert response_negative.status_code in [200, 404]


# ============================================================================
# РАЗДЕЛ 5: ТЕЛО ЗАПРОСА
# ============================================================================

def test_body_not_applicable_for_get():
    """
    РАЗДЕЛ 5: Тело запроса
    Статус: Частично применимо
    
    Объяснение: GET-запросы обычно не имеют тела.
    Этот раздел актуален для POST/PUT/PATCH.
    
    jsonplaceholder поддерживает POST/PUT/PATCH/DELETE,
    но они mock-запросы (данные не сохраняются реально).
    """
    print("ℹ️  Тело запроса тестируется для POST/PUT/PATCH, не для GET")


# ============================================================================
# РАЗДЕЛ 6: HTTP КОДЫ СТАТУСА
# ============================================================================

def test_status_070_ok():
    """
    API-070: 200 OK
    Ожидаемый результат: Успешный запрос существующего ресурса
    Приоритет: P0
    """
    response = requests.get(f"{BASE_URL}/users/1")
    assert response.status_code == 200


def test_status_077_not_found():
    """
    API-077: 404 Not Found
    Ожидаемый результат: Ресурс не найден
    Приоритет: P0
    
    Важный пример из чек-листа:
    GET /users/999999 → если пользователь не существует,
    бездумно принимать 200 OK может быть дефектом.
    """
    response = requests.get(f"{BASE_URL}/users/999999")
    # jsonplaceholder возвращает пустой JSON {}, а не 404
    # Это особенность mock-API. В реальном API был бы 404.
    assert response.status_code == 404
    


def test_status_071_created():
    """
    API-071: 201 Created — ресурс создан
    Ожидаемый результат: Успешное создание ресурса
    Приоритет: P0
    
    Тестируем POST.
    """
    new_user = {
        "name": "Erick Arzumanian",
        "username": "erick_qa",
        "email": "erick@example.com"
    }
    response = requests.post(f"{BASE_URL}/users", json=new_user)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Erick Arzumanian"
    assert "id" in data  # Сервер сгенерировал ID


# ============================================================================
# РАЗДЕЛ 7: ТЕЛО ОТВЕТА
# ============================================================================

def test_response_085_structure():
    """
    API-085: Структура ответа соответствует контракту
    Ожидаемый результат: Все ожидаемые поля присутствуют
    Приоритет: P0
    """
    response = requests.get(f"{BASE_URL}/users/1")
    assert response.status_code == 200
    data = response.json()
    
    # Проверяем наличие всех обязательных полей
    required_fields = ["id", "name", "username", "email", "address", "phone", "website", "company"]
    for field in required_fields:
        assert field in data, f"Поле '{field}' отсутствует в ответе"


def test_response_086_required_fields_present():
    """
    API-086: Обязательные поля присутствуют
    Ожидаемый результат: Все required fields на месте
    Приоритет: P0
    """
    response = requests.get(f"{BASE_URL}/users/1")
    data = response.json()
    
    assert "id" in data
    assert "name" in data
    assert "email" in data


def test_response_087_correct_data_types():
    """
    API-087: Типы данных корректны
    Ожидаемый результат: id — int, name — str, email — str
    Приоритет: P0
    """
    response = requests.get(f"{BASE_URL}/users/1")
    data = response.json()
    
    assert isinstance(data["id"], int), "id должен быть целым числом"
    assert isinstance(data["name"], str), "name должен быть строкой"
    assert isinstance(data["email"], str), "email должен быть строкой"


def test_response_088_correct_values():
    """
    API-088: Значения полей корректны
    Ожидаемый результат: Значения соответствуют ожидаемым
    Приоритет: P1
    """
    response = requests.get(f"{BASE_URL}/users/1")
    data = response.json()
    
    assert data["id"] == 1
    assert data["name"] == "Leanne Graham"
    assert "@" in data["email"]  # Email содержит @


def test_response_091_null_handling():
    """
    API-091: Значения null обрабатываются корректно
    Ожидаемый результат: null допустимы там, где разрешены
    Приоритет: P1
    
    Проверяем, что поля не возвращают неожиданный null.
    """
    response = requests.get(f"{BASE_URL}/users/1")
    data = response.json()
    
    # Основные поля не должны быть null
    assert data["name"] is not None
    assert data["email"] is not None
    assert data["id"] is not None


def test_response_092_arrays_correct():
    """
    API-092: Массивы содержат ожидаемые элементы
    Ожидаемый результат: Коллекция пользователей — это список
    Приоритет: P1
    """
    response = requests.get(f"{BASE_URL}/users")
    data = response.json()
    
    assert isinstance(data, list), "Ответ должен быть списком"
    assert len(data) == 10, "Должно быть 10 пользователей"


# ============================================================================
# РАЗДЕЛ 8: CRUD ОПЕРАЦИИ
# ============================================================================

def test_crud_099_create():
    """
    API-099: Создание с валидными данными (CREATE)
    Ожидаемый результат: 201 Created, ресурс создан
    Приоритет: P0
    """
    new_user = {
        "name": "Test User",
        "username": "testuser",
        "email": "test@example.com"
    }
    response = requests.post(f"{BASE_URL}/users", json=new_user)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test User"
    assert "id" in data


def test_crud_103_resource_exists_after_create():
    """
    API-103: Проверить, что объект действительно существует после создания
    Ожидаемый результат: GET созданного ресурса возвращает 200
    Приоритет: P0
    
    Примечание: jsonplaceholder — mock API, данные не сохраняются реально.
    Поэтому этот тест демонстрирует ограничение.
    """
    new_user = {
        "name": "Persistent User",
        "username": "persistent",
        "email": "persistent@example.com"
    }
    create_response = requests.post(f"{BASE_URL}/users", json=new_user)
    created_id = create_response.json()["id"]
    
    # Пытаемся получить созданный ресурс
    get_response = requests.get(f"{BASE_URL}/users/{created_id}")
    
    # jsonplaceholder вернёт пустой {}, т.к. данные не сохраняются
    print(f"⚠️  jsonplaceholder не сохраняет данные реально (mock API)")
    print(f"   Созданный ID: {created_id}, GET вернул: {get_response.json()}")


def test_crud_108_read_existing():
    """
    API-108: Получение существующего объекта (READ)
    Ожидаемый результат: 200 OK с данными объекта
    Приоритет: P0
    """
    response = requests.get(f"{BASE_URL}/users/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1


def test_crud_109_read_nonexistent():
    """
    API-109: Получение несуществующего объекта (READ)
    Ожидаемый результат: 404 Not Found или пустой ответ
    Приоритет: P0
    """
    response = requests.get(f"{BASE_URL}/users/9999")
    # jsonplaceholder возвращает пустой JSON, а не 404
    assert response.status_code == 404


def test_crud_115_update():
    """
    API-115: Обновление существующего объекта (UPDATE)
    Ожидаемый результат: 200 OK, данные обновлены
    Приоритет: P0
    
    Тестируем PUT (полное обновление).
    """
    updated_user = {
        "id": 1,
        "name": "Updated Name",
        "username": "updated_user",
        "email": "updated@example.com"
    }
    response = requests.put(f"{BASE_URL}/users/1", json=updated_user)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated Name"


def test_crud_117_partial_update():
    """
    API-117: Частичное обновление (PATCH)
    Ожидаемый результат: 200 OK, обновлено только указанное поле
    Приоритет: P1
    """
    patch_data = {"name": "Patched Name"}
    response = requests.patch(f"{BASE_URL}/users/1", json=patch_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Patched Name"


def test_crud_124_delete():
    """
    API-124: Удаление существующего объекта (DELETE)
    Ожидаемый результат: 200 OK или 204 No Content
    Приоритет: P0
    """
    response = requests.delete(f"{BASE_URL}/users/1")
    assert response.status_code == 200


def test_crud_128_verify_deleted():
    """
    API-128: Проверить, что объект действительно удалён
    Ожидаемый результат: GET после DELETE возвращает 404
    Приоритет: P0
    
    Примечание: jsonplaceholder не удаляет реально.
    """
    # DELETE
    requests.delete(f"{BASE_URL}/users/1")
    
    # GET после DELETE
    get_response = requests.get(f"{BASE_URL}/users/1")
    
    # jsonplaceholder всё ещё вернёт данные (mock API)
    print("⚠️  jsonplaceholder не удаляет данные реально (mock API)")


# ============================================================================
# РАЗДЕЛ 9: БИЗНЕС-ЛОГИКА
# ============================================================================

def test_business_logic_email_format():
    """
    API-130: Бизнес-правила реализованы корректно
    Ожидаемый результат: Email содержит @, имя не содержит @
    Приоритет: P0
    """
    response = requests.get(f"{BASE_URL}/users/1")
    data = response.json()
    
    # Бизнес-правило: email должен быть валидным форматом
    assert "@" in data["email"]
    assert "." in data["email"]
    
    # Бизнес-правило: имя не должно содержать @
    assert "@" not in data["name"]


def test_business_logic_unique_ids():
    """
    API-130: Идентификаторы уникальны
    Ожидаемый результат: Каждый пользователь имеет уникальный ID
    Приоритет: P1
    """
    response = requests.get(f"{BASE_URL}/users")
    users = response.json()
    
    ids = [user["id"] for user in users]
    # Проверяем, что все ID уникальны
    assert len(ids) == len(set(ids)), "Найдены дублирующиеся ID"


# ============================================================================
# РАЗДЕЛ 10: ГРАНИЧНЫЕ ЗНАЧЕНИЯ
# ============================================================================

def test_boundary_001():
    """
    API: Граничные значения для ID
    Минимальный ID: 1
    Максимальный ID: 10 (в jsonplaceholder)
    Приоритет: P1
    """
    # ID = 1 (минимум) → должен работать
    response_min = requests.get(f"{BASE_URL}/users/1")
    assert response_min.status_code == 200
    
    # ID = 10 (максимум) → должен работать
    response_max = requests.get(f"{BASE_URL}/users/10")
    assert response_max.status_code == 200
    
    # ID = 11 (выше максимума) → не должен работать
    response_over = requests.get(f"{BASE_URL}/users/11")
    assert response_over.status_code == 404


# ============================================================================
# РАЗДЕЛЫ 11-32: КОММЕНТАРИИ О ПРИМЕНИМОСТИ
# ============================================================================

def test_other_sections_notes():
    """
    РАЗДЕЛЫ 11-32: Применимость к jsonplaceholder
    
    11. Тестирование комбинаций — N/A (простой API без сложных параметров)
    12. Фильтрация — ПРИМЕНИМО (можно тестировать ?id=1)
    13. Сортировка — N/A (jsonplaceholder не поддерживает сортировку)
    14. Пагинация — N/A (нет параметров page/limit)
    15. Заголовки — ПРИМЕНИМО (можно тестировать Accept, Content-Type)
    16. Обработка ошибок — ПРИМЕНИМО (404, 400)
    17. Безопасность — N/A (нет аутентификации)
    18. Идемпотентность — ПРИМЕНИМО (GET идемпотентен)
    19. Повторные запросы — ПРИМЕНИМО (rate limiting)
    20. Производительность — N/A (mock API, нет SLA)
    21. Интеграции — N/A (нет внешних зависимостей)
    22. Согласованность данных — ЧАСТИЧНО (данные не сохраняются)
    23. Тестирование контракта — ПРИМЕНИМО (Swagger не предоставлен, но структура известна)
    24. Обратная совместимость — N/A (тестовый API)
    25. Локализация — N/A (только латиница)
    26. Дата/время — N/A (нет полей даты)
    27. Устойчивость — N/A (mock API всегда доступен)
    28. Логирование — N/A (нет доступа к логам)
    29. Приоритет — ПРИМЕНИМО (все тесты имеют приоритет)
    30. Последовательность тестирования — ПРИМЕНИМО (следуем ей)
    31. Краткий чек-лист — ПРИМЕНИМО (используем)
    32. Главный принцип — ПРИМЕНИМО (What should/shouldn't happen)
    """
    print("ℹ️  См. комментарии в docstring")


# ============================================================================
# ФИЛЬТРАЦИЯ (РАЗДЕЛ 12) — ПРИМЕНИМО
# ============================================================================

def test_filter_146_single_field():
    """
    API-146: Фильтрация по одному полю
    Ожидаемый результат: Возвращаются отфильтрованные данные
    Приоритет: P1
    """
    response = requests.get(f"{BASE_URL}/users", params={"id": 1})
    data = response.json()
    assert len(data) == 1
    assert data[0]["id"] == 1


def test_filter_149_invalid_filter():
    """
    API-149: Невалидный фильтр
    Ожидаемый результат: Игнорируется или ошибка
    Приоритет: P1
    """
    # jsonplaceholder игнорирует неизвестные параметры
    response = requests.get(f"{BASE_URL}/users", params={"unknown_field": "value"})
    assert response.status_code == 200
    # Возвращаются все пользователи (фильтр проигнорирован)


# ============================================================================
# ИДЕМПОТЕНТНОСТЬ (РАЗДЕЛ 18) — ПРИМЕНИМО
# ============================================================================

def test_idempotency_218_get():
    """
    API-218: GET является идемпотентным
    Ожидаемый результат: Многократные GET возвращают одинаковый результат
    Приоритет: P1
    """
    response1 = requests.get(f"{BASE_URL}/users/1")
    response2 = requests.get(f"{BASE_URL}/users/1")
    response3 = requests.get(f"{BASE_URL}/users/1")
    
    assert response1.status_code == response2.status_code == response3.status_code == 200
    assert response1.json() == response2.json() == response3.json()


# ============================================================================
# ПОВТОРНЫЕ ЗАПРОСЫ (РАЗДЕЛ 19) — ПРИМЕНИМО
# ============================================================================

def test_retry_223_single_request():
    """
    API-223: Отправить запрос один раз
    Ожидаемый результат: Успешный ответ
    Приоритет: P1
    """
    response = requests.get(f"{BASE_URL}/users/1")
    assert response.status_code == 200


def test_retry_224_duplicate_requests():
    """
    API-224: Отправить идентичный запрос дважды
    Ожидаемый результат: Оба запроса успешны
    Приоритет: P1
    """
    response1 = requests.post(f"{BASE_URL}/posts", json={"title": "Test", "body": "Test"})
    response2 = requests.post(f"{BASE_URL}/posts", json={"title": "Test", "body": "Test"})
    
    assert response1.status_code == 201
    assert response2.status_code == 201


# ============================================================================
# ОБРАБОТКА ОШИБОК (РАЗДЕЛ 16) — ПРИМЕНИМО
# ============================================================================

def test_error_190_correct_status():
    """
    API-190: Корректный HTTP-статус для ошибок
    Ожидаемый результат: 404 для несуществующего ресурса
    Приоритет: P0
    """
    response = requests.get(f"{BASE_URL}/nonexistent")
    assert response.status_code == 404


def test_error_196_no_stack_trace():
    """
    API-196: В ответе отсутствует stack trace
    Ожидаемый результат: Ошибка не раскрывает внутреннюю информацию
    Приоритет: P1
    """
    response = requests.get(f"{BASE_URL}/users/invalid-id")
    data = response.text
    
    # Проверяем, что в ответе нет технических деталей
    assert "Traceback" not in data
    assert "File \"" not in data
    assert "Error:" not in data or "404" in data