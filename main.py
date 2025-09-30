import requests
token = "ВАШ_ТОКЕН"
url = "https://api.github.com/user/repos"
headers = {"Authorization": f"token {token}"}
data = {"name": "lopassss", "description": "Password manager CLI", "private": False}
response = requests.post(url, headers=headers, json=data)
print("Репозиторій створено!" if response.status_code == 201 else "Помилка!")
