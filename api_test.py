from requests import get


# Задание 1
response = get("https://jsonplaceholder.typicode.com/posts")
posts = response.json()
first_five_posts = posts[:5]
print("--- Первые 5 постов --- \n")
for index, post in enumerate(first_five_posts, start=1):
    print(f"Пост №{index}")
    print(f"Заголовок: {post['title']}")
    print(f"Текст: {post['body']}")
    print("-" * 30 + "\n")
