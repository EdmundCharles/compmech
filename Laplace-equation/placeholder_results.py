import numpy as np
import pandas as pd
from Solver import SRM

# ==============================================================================
# PARAMETERS, BOUNDARY CONDITIONS (BC) AND INITIAL CONDITIONS (IC)
# ==============================================================================
h = 0.1
l = 1
m = 1

nx = int(l/h) + 1
ny = int(m/h) + 1

phi_0 = lambda x: 10*x*(1-x) 
phi_m = lambda x: 20
psi_0 = lambda y: 20*y**2
psi_l = lambda y: 20*y

omegas = np.arange(0.1,2,0.1)
eps = 0.01


res = SRM(phi_0,phi_m,psi_0,psi_l,l,m,nx,ny,eps,omega = 1)

u = res[2]
iters = []
for w in omegas:
    k  = SRM(phi_0,phi_m,psi_0,psi_l,l,m,nx,ny,eps,omega = w)[-1]
    iters.append(k)
pd.DataFrame(u).to_clipboard(excel=True, index=False, header=False)
print("1/2: Решение скопировано")
print("     В Excel Cmd+V.")

input(
    "\npress enter to continue"
)

pd.DataFrame([iters]).to_clipboard(excel=True, index=False, header=False,)
print("2/2: Количество итераций скопировано")
print("     В Excel нажми Cmd+V")