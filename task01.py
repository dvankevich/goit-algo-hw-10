import pulp

# Ініціалізація моделі
model = pulp.LpProblem("Maximize Profit", pulp.LpMaximize)

# Визначення змінних
lemonade = pulp.LpVariable("Лимонад", lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable("Фруктовий сік", lowBound=0, cat='Integer')

# Цільова функція: максимізувати загальну кількість вироблених продуктів "Лимонад" та "Фруктовий сік"
model += lemonade + fruit_juice, "Загальна кількість продуктів"

# Обмеження на ресурси
'''
1. "Лимонад" виготовляється з "Води", "Цукру" та "Лимонного соку".
2. "Фруктовий сік" виготовляється з "Фруктового пюре" та "Води".
3. Обмеження ресурсів: 100 од. "Води", 50 од. "Цукру", 30 од. "Лимонного соку" та 40 од. "Фруктового пюре".
4. Виробництво одиниці "Лимонаду" вимагає 2 од. "Води", 1 од. "Цукру" та 1 од. "Лимонного соку".
5. Виробництво одиниці "Фруктового соку" вимагає 2 од. "Фруктового пюре" та 1 од. "Води".
'''
model += 2 * lemonade + 1 * fruit_juice <= 100, "Вода"
model += 1 * lemonade <= 50, "Цукор"
model += 1 * lemonade <= 30, "Лимонний сік"
model += 2 * fruit_juice + 1 * lemonade <= 40, "Фруктове пюре"

# Розв'язання моделі
model.solve()

# Вивід результатів
print(f"Status: {pulp.LpStatus[model.status]}")
print(f"Виробляти лимонадів: {lemonade.varValue}")
print(f"Виробляти фруктового соку: {fruit_juice.varValue}")
print(f"Загальна кількість продуктів: {lemonade.varValue + fruit_juice.varValue}")