import random
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Визначення функції
def f(x):
    return x ** 2

def is_inside(x, y, func):
    """Перевіряє, чи знаходиться точка (x, y) всередині "сірої зони"."""
    return y <= func(x)

def monte_carlo_simulation(a, b, num_experiments, func):
    """Виконує серію експериментів методом Монте-Карло."""
    average_area = 0
    maxf = max(func(x) for x in np.linspace(a, b, 100))
    print("maxf", maxf)

    for _ in range(num_experiments):
        points = [(random.uniform(a, b), random.uniform(0, maxf)) for _ in range(15000)]
        inside_points = [point for point in points if is_inside(point[0], point[1], func)]

        M = len(inside_points)
        N = len(points)
        area = (M / N) * ((b - a) * maxf)
        average_area += area

    average_area /= num_experiments
    return average_area

a = 0.5
b = 2
num_experiments = 100

# Виклик функцій
result, error = spi.quad(f, a, b)
average_area = monte_carlo_simulation(a, b, num_experiments, f)

print("Інтеграл: ", result, error)
print(f"Середня площа за {num_experiments} експериментів: {average_area}")