import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi
import random

# Визначення функції
def f(x):
    #return x ** 2
    return np.sin(x) + np.cos(x) + 2

def is_inside(x, y, func):
    """Перевіряє, чи знаходиться точка (x, y) всередині "сірої зони"."""
    return y <= func(x)

def monte_carlo_simulation(a, b, num_experiments, func):
    """Виконує серію експериментів методом Монте-Карло."""
    average_area = 0
    maxf = max(func(x) for x in np.linspace(a, b, 100))
    #print("maxf", maxf)

    for _ in range(num_experiments):
        points = [(random.uniform(a, b), random.uniform(0, maxf)) for _ in range(15000)]
        inside_points = [point for point in points if is_inside(point[0], point[1], func)]

        M = len(inside_points)
        N = len(points)
        area = (M / N) * ((b - a) * maxf)
        average_area += area

    average_area /= num_experiments
    return average_area

a = 0.5  # Нижня межа
b = 6.25  # Верхня межа
# Кількість експериментів
num_experiments = 100

# Створення діапазону значень для x
x = np.linspace(-0.5, 7.5, 400)
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
ax.set_title('Графік інтегрування f(x) від ' + str(a) + ' до ' + str(b))
plt.grid()
print("Для продовження закрийте графік")
plt.show()

result, error = spi.quad(f, a, b)

print("Інтеграл: ", result, error)

average_area = monte_carlo_simulation(a, b, num_experiments, f)
print(f"Середня площа за {num_experiments} експериментів: {average_area}")