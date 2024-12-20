import requests

def calculate_and_print():
    """Запрашивает у пользователя ссылку, отправляет GET-запрос и выводит результат."""
    num1 = input("Введите число 1")
    num2 = input("Введите число 2")
    operation = input("weweweewerrrer")

    response = requests.get("http://127.0.0.1:5000/calculate/"+num1+"/"+num2+"/"+operation )

    if response.status_code == 200:
        result = response.json()['result']
        print(f"Результат: {result}")
    else:
        print(f"Ошибка: {response.text}")

if __name__ == "__main__":
    calculate_and_print()
