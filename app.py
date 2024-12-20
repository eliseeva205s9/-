from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate/<num1>/<num2>/<operation>')
def calculate(num1, num2, operation):
    """
    Обрабатывает GET-запрос с данными для вычисления.

    Args:
        num1 (str): Первое число.
        num2 (str): Второе число.
        operation (str): Операция ("add", "subtract", "multiply", "divide").

    Returns:
        JSON-ответ с результатом вычисления или ошибкой.
    """
    try:
        num1 = float(num1)
        num2 = float(num2)

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                return jsonify({'error': 'Деление на ноль недопустимо'}), 400
            result = num1 / num2
        else:
            return jsonify({'error': 'Неверная операция'}), 400

        return jsonify({'result': result})

    except ValueError as e:
        return jsonify({'error': f'Некорректный ввод данных: {e}'}), 400

if __name__ == '__main__':
    app.run(debug=True)
