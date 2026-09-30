import numpy as np
import matplotlib.pyplot as plt
from Solver import SRM

#Prolem statement
h = 0.1
l = 1
m = 1

nx = int(l/h) + 1
ny = int(m/h) + 1

phi_0 = lambda x: 10*x*(1-x) 
phi_m = lambda x: 20
psi_0 = lambda y: 20*y**2
psi_l = lambda y: 20*y

eps = 0.01
# Discretization of the relaxation parameter omega in (0, 2)
omegas = np.round(np.arange(0.1, 2.0, 0.05), 2)

# ==============================================================================
# 2. NUMERICAL CONVERGENCE ANALYSIS: k(omega)
# ==============================================================================
iterations = []

for w in omegas:
    _, _, _, k = SRM(phi_0, phi_m, psi_0, psi_l, l, m, nx, ny, eps, omega=w)
    iterations.append(k)

iterations = np.array(iterations)

# Minimum iteration count and empirical optimal omega
opt_idx = np.argmin(iterations)
omega_opt = omegas[opt_idx]
k_min = iterations[opt_idx]

# Theoretical optimal omega for Dirichlet problem on a square mesh:
# omega_opt = 2 / (1 + sin(pi * h / l))
omega_th = 2.0 / (1.0 + np.sin(np.pi * h / l))

# Solution computed at optimal omega
x, y, u, _ = SRM(
    phi_0, phi_m, psi_0, psi_l, l, m, nx, ny, eps, omega=omega_opt
)

# ==============================================================================
# 3. FIGURE 1: CONVERGENCE RATE vs. RELAXATION FACTOR
# ==============================================================================
fig_conv, ax_conv = plt.subplots(figsize=(8, 5), dpi=100)

ax_conv.plot(
    omegas,
    iterations,
    color="#08519c",
    linewidth=1.8,
    marker="o",
    markersize=4.0,
    label="SR iterations",
)

# Baseline: classical Gauss–Seidel method (omega = 1.0)
k_seidel = iterations[np.where(omegas == 1.0)[0][0]]
ax_conv.scatter(
    [1.0],
    [k_seidel],
    color="#238b45",
    s=70,
    zorder=5,
    label=rf"Gauss–Seidel ($\omega = 1.0$, $k = {k_seidel}$)",
)

# Numerical minimum
ax_conv.scatter(
    [omega_opt],
    [k_min],
    color="#cb181d",
    s=85,
    zorder=5,
    label=rf"Numerical optimum ($\omega = {omega_opt:.2f}$, $k = {k_min}$)",
)

# # Theoretical estimate reference line
# ax_conv.axvline(
#     omega_th,
#     color="#737373",
#     linestyle="--",
#     linewidth=1.2,
#     alpha=0.9,
#     label=rf"Theoretical bound ($\omega \approx {omega_th:.2f}$)",
# )

ax_conv.set_title(
    r"Convergence of the SR Method ($\varepsilon = 10^{-2}$)",
    fontsize=12,
    fontweight="semibold",
    pad=10,
)
ax_conv.set_xlabel(r"$\omega$", fontsize=12)
ax_conv.set_ylabel(r"$k$", fontsize=12)
ax_conv.grid(True, linestyle=":", linewidth=0.6, alpha=0.7)
ax_conv.legend(fontsize=9, loc="upper right", frameon=True, framealpha=0.95)
ax_conv.set_xlim(0.05, 1.95)
ax_conv.tick_params(direction="out", labelsize=10)

plt.tight_layout()

# ==============================================================================
# 4. FIGURE 2: 3D EQUILIBRIUM SURFACE u(x, y)
# ==============================================================================
X, Y = np.meshgrid(x, y, indexing="ij")

fig_surf = plt.figure(figsize=(9, 6.5), dpi=100)
ax_surf = fig_surf.add_subplot(111, projection="3d")

surf = ax_surf.plot_surface(
    X,
    Y,
    u,
    cmap="plasma",
    edgecolor="#252525",
    linewidth=0.25,
    alpha=0.95,
    rstride=1,
    cstride=1,
)

ax_surf.set_title(
    rf"Numerical Solution $u(x, y)$ ($\Delta u = 0$, $\omega = {omega_opt:.2f}$)",
    fontsize=12,
    fontweight="semibold",
    pad=14,
)
ax_surf.set_xlabel(r"$x$", fontsize=11, labelpad=6)
ax_surf.set_ylabel(r"$y$", fontsize=11, labelpad=6)
ax_surf.set_zlabel(r"$u(x, y)$", fontsize=11, labelpad=6)

ax_surf.view_init(elev=26, azim=-128)
ax_surf.tick_params(labelsize=9)

cbar = fig_surf.colorbar(surf, ax=ax_surf, shrink=0.55, aspect=14, pad=0.08)
cbar.set_label(r"$u(x, y)$", fontsize=11)
cbar.ax.tick_params(labelsize=9)

plt.tight_layout()
plt.show()