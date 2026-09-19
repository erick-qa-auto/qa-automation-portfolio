import requests

def test_mock_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    user = {"title": "Erick", "body": "My first post", "userId": 5}
    response = requests.post(url, json=user)
    print(f"status: {response.status_code}")
    print(f"all response: {response.json()}")
    post_id = response.json()["id"]
    check_url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    check_response = requests.get(check_url)
    print(f"get status: {check_response.status_code}")
    r_post = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    print(f"realpost status: {r_post.status_code}")
    get_title = r_post.json()["title"]
    print(f"title: {get_title}")

    '''status: 201 — POST создал пост
       get status: 404 — «созданный» пост не найден (улика мока)
       realpost status: 200 — реальный пост жив
       title: sunt aut facere... — длинный английский заголовок реального поста'''