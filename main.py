import math

def calculate_factorial(number):
    """
    Вычисляет факториал заданного числа.

    Args:
        number (int): Положительное целое число.

    Returns:
        int: Факториал числа.
    """
    if number < 0:
        raise ValueError("Факториал не определен для отрицательных чисел.")
    elif number == 0:
        return 1
    else:
        # Используем math.factorial для оптимизации работы с большими числами
        return math.factorial(number)

def main():
    """
    Основная функция программы, запрашивающая ввод, вычисляющая факториал
    и обрабатывающая ошибки.
    """
    while True:
        try:
            user_input = input("Пожалуйста, введите положительное целое число: ")
            num = int(user_input)

            if num < 0:
                print("Ошибка: Введите положительное целое число.")
            else:
                factorial_result = calculate_factorial(num)
                print(f"Факториал числа {num} равен: {factorial_result}")
                break  # Выходим из цикла, если ввод корректен и вычисление успешно
        except ValueError:
            print("Ошибка: Введенные данные не являются целым числом. Попробуйте еще раз.")
        except Exception as e:
            print(f"Произошла непредвиденная ошибка: {e}")

if __name__ == "__main__":
    main()
