import numpy as np
import pandas as pd
from Solver import explicit, implicit

# Начальные и краевые условия
phi = lambda x: 2 * x * (x + 0.2) + 0.4
psi_0 = lambda t: 2 * t + 0.4
psi_l = lambda t: 1.36

l = 0.6
t_star = 0.01

# Сетка преподавателя: 11 точек по x (шаг 0.06) и 11 точек по t (шаг 0.001)
nh = 11
nt = 11

# Прямой расчет без интерполяции
res_exp = explicit(phi, psi_0, psi_l, t_star, l, nt, nh)
res_imp = implicit(phi, psi_0, psi_l, t_star, l, nt, nh)

# Забираем матрицу T, если функция возвращает кортеж (x, t, T)
T_explicit = res_exp[2] if isinstance(res_exp, tuple) else res_exp
T_implicit = res_imp[2] if isinstance(res_imp, tuple) else res_imp

# 1. Буфер для явной схемы
pd.DataFrame(T_explicit).to_clipboard(excel=True, index=False, header=False)
print("1/2: Таблица ЯВНОЙ схемы скопирована в буфер.")
print("     Встань в Excel на ячейку D4 и нажми Cmd+V (Ctrl+V).")

# 2. Пауза перед вторым шагом
input(
    "\nКак вставишь первую таблицу, нажми Enter здесь для копирования неявной..."
)

# 3. Буфер для неявной схемы
pd.DataFrame(T_implicit).to_clipboard(excel=True, index=False, header=False)
print("2/2: Таблица НЕЯВНОЙ схемы скопирована в буфер.")
print("     Встань в Excel на ячейку D18 и нажми Cmd+V (Ctrl+V).")