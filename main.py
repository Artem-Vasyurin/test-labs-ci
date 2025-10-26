class Calculator:
    """Простой класс калькулятора с базовыми операциями."""

    def add(self, a, b):
        """Сложение двух чисел."""
        return a + b

    def subtract(self, a, b):
        """Вычитание второго числа из первого."""
        return a - b

    def multiply(self, a, b):
        """Умножение двух чисел."""
        return a * b

    def divide(self, a, b):
        """Деление первого числа на второе."""
        if b == 0:
            raise ValueError("Деление на ноль невозможно")
        return a / b

    def is_prime_number(self, n):
        """Проверка, является ли число простым."""
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
