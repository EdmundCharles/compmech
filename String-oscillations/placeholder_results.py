import numpy as np
import pandas as pd
from Solver import explicit, implicit

# ==============================================================================
# PARAMETERS, BOUNDARY CONDITIONS (BC) AND INITIAL CONDITIONS (IC)
# ==============================================================================
phi_0 = lambda x: (1.0 - x) * np.cos(np.pi * x / 2.0)
phi_1 = lambda x: 2.0 * x + 1.0

psi_0 = lambda t: 2.0 * t + 1.0
psi_l = lambda t: np.zeros_like(t)

l = 1.0
t_star = 0.5
h = 0.1
dt = 0.05

nt = round(t_star / dt) + 1
nh = round(l / h) + 1


res_exp = explicit(phi_0, phi_1, psi_0, psi_l, t_star, l, nt, nh)
res_imp = implicit(phi_0, phi_1, psi_0, psi_l, t_star, l, nt, nh)

u_explicit = res_exp[2] if isinstance(res_exp, tuple) else res_exp
u_implicit = res_imp[2] if isinstance(res_imp, tuple) else res_imp

pd.DataFrame(u_explicit).to_clipboard(excel=True, index=False, header=False)
print("1/2: Таблица ЯВНОЙ схемы (струна) скопирована в буфер.")
print("     Встань в Excel на ячейку D4 и нажми Cmd+V (Ctrl+V).")

input(
    "\nКак вставишь первую таблицу, нажми Enter здесь для копирования неявной..."
)

pd.DataFrame(u_implicit).to_clipboard(excel=True, index=False, header=False)
print("2/2: Таблица НЕЯВНОЙ схемы (струна) скопирована в буфер.")
print("     Встань в Excel на ячейку D18 и нажми Cmd+V (Ctrl+V).")