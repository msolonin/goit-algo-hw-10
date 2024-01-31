# -*- coding: utf-8 -*-
"""
Завдання 2. Обчислення визначеного інтеграла.
Ваше друге завдання полягає в обчисленні значення інтеграла функції методом Монте-Карло.
Виконаємо побудову графіка.
"""
import scipy.integrate as spi
import matplotlib.pyplot as plt
import numpy as np
import random

a = 0  # Нижня межа
b = 2  # Верхня межа


# Визначення функції та межі інтегрування
def f(x):
    return x ** 2


def build_graph():
    # Створення діапазону значень для x
    x = np.linspace(-0.5, 2.5, 400)
    y = f(x)

    # Створення графіка
    fig, ax = plt.subplots()

    # Малювання функції
    ax.plot(x, y, 'r', linewidth=2)

    # Заповнення області під кривою
    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)

    # Налаштування графіка
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')

    # Додавання меж інтегрування та назви графіка
    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')
    ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
    plt.grid()
    plt.show()


def monte_carlo_simulation(func, a, b, num_samples):
    total = 0
    for _ in range(num_samples):
        x = random.uniform(a, b)
        total += func(x)
    average = total / num_samples
    integral = (b - a) * average
    return integral


if __name__ == '__main__':
    # Обчислення інтеграла
    result, error = spi.quad(f, a, b)
    print(f"Інтеграл: {result}")
    # Виконання симуляції
    average_area = monte_carlo_simulation(f, a, b, 1000000)
    print(f"Інтеграл методом Монте-Карло: {average_area}")
    # Створення графіка:
    build_graph()
