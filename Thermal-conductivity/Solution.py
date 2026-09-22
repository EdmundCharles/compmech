import numpy as np
from Solver import explicit, implicit
import matplotlib.pyplot as plt
#Parameters, BC and IC
# phi = lambda x: 2*x*(x + 0.2) + 0.4
phi = lambda x: 0.5*np.sin(10*x)
psi_0 = lambda t: 2*t + 0.4
psi_l = lambda t: 1.36

l = 0.6
t_star = 0.01
h = 0.01
dt = 0.3*h**2
nt = round(t_star/dt) + 1
nh = round(l/h) + 1
#Solution
x_explicit,t_explicit,T_explicit = explicit(phi,psi_0,psi_l,t_star,l,nt, nh)
x_implicit,t_implicit,T_implicit = implicit(phi,psi_0,psi_l,t_star,l,nt, nh)

#Plots
# ==============================================================================
# PLOT CONFIGURATION SETTINGS
# ==============================================================================
PLOT_CONFIG = {
    # Figure properties
    "fig_size": (10, 7),
    "dpi": 100,
    "view_elev": 25,  # Elevation angle
    "view_azim": -120,  # Azimuth angle
    # Font sizes
    "title_size": 14,
    "label_size": 12,
    "tick_size": 10,
    "colorbar_label_size": 11,
    # Surface style
    "alpha": 0.9,
    "edge_color": "black",
    "line_width": 0.1,
    "rstride": 1,  # Coordinate step size for mesh wireframe
    "cstride": 1,  # Time step size for mesh wireframe
    # Explicit scheme aesthetics
    "explicit_cmap": "viridis",
    "explicit_title": "Explicit Scheme",
    # Implicit scheme aesthetics
    "implicit_cmap": "coolwarm",
    "implicit_title": "Implicit Scheme",
    # Axis labels (English)
    "label_x": "Coordinate, $x$ [m]",
    "label_t": "Time, $t$ [s]",
    "label_T": "Temperature, $T(x, t)$",
}

# ==============================================================================
# 1. EXPLICIT SCHEME 3D SURFACE PLOT
# ==============================================================================
X_exp, TIME_exp = np.meshgrid(x_explicit, t_explicit)

fig_exp = plt.figure(figsize=PLOT_CONFIG["fig_size"], dpi=PLOT_CONFIG["dpi"])
ax_exp = fig_exp.add_subplot(111, projection="3d")

surf_exp = ax_exp.plot_surface(
    X_exp,
    TIME_exp,
    T_explicit,
    cmap=PLOT_CONFIG["explicit_cmap"],
    edgecolor=PLOT_CONFIG["edge_color"],
    linewidth=PLOT_CONFIG["line_width"],
    alpha=PLOT_CONFIG["alpha"],
    rstride=PLOT_CONFIG["rstride"],
    cstride=PLOT_CONFIG["cstride"],
)

ax_exp.set_title(
    PLOT_CONFIG["explicit_title"],
    fontsize=PLOT_CONFIG["title_size"],
    pad=15,
    fontweight="bold",
)
ax_exp.set_xlabel(
    PLOT_CONFIG["label_x"], fontsize=PLOT_CONFIG["label_size"], labelpad=10
)
ax_exp.set_ylabel(
    PLOT_CONFIG["label_t"], fontsize=PLOT_CONFIG["label_size"], labelpad=10
)
ax_exp.set_zlabel(
    PLOT_CONFIG["label_T"], fontsize=PLOT_CONFIG["label_size"], labelpad=10
)

ax_exp.tick_params(axis="both", which="major", labelsize=PLOT_CONFIG["tick_size"])
ax_exp.view_init(elev=PLOT_CONFIG["view_elev"], azim=PLOT_CONFIG["view_azim"])

cbar_exp = fig_exp.colorbar(
    surf_exp, ax=ax_exp, shrink=0.55, aspect=12, pad=0.1
)
cbar_exp.set_label(
    PLOT_CONFIG["label_T"], fontsize=PLOT_CONFIG["colorbar_label_size"]
)
cbar_exp.ax.tick_params(labelsize=PLOT_CONFIG["tick_size"])

plt.tight_layout()

# ==============================================================================
# 2. IMPLICIT SCHEME 3D SURFACE PLOT
# ==============================================================================
X_imp, TIME_imp = np.meshgrid(x_implicit, t_implicit)

fig_imp = plt.figure(figsize=PLOT_CONFIG["fig_size"], dpi=PLOT_CONFIG["dpi"])
ax_imp = fig_imp.add_subplot(111, projection="3d")

surf_imp = ax_imp.plot_surface(
    X_imp,
    TIME_imp,
    T_implicit,
    cmap=PLOT_CONFIG["implicit_cmap"],
    edgecolor=PLOT_CONFIG["edge_color"],
    linewidth=PLOT_CONFIG["line_width"],
    alpha=PLOT_CONFIG["alpha"],
    rstride=PLOT_CONFIG["rstride"],
    cstride=PLOT_CONFIG["cstride"],
)

ax_imp.set_title(
    PLOT_CONFIG["implicit_title"],
    fontsize=PLOT_CONFIG["title_size"],
    pad=15,
    fontweight="bold",
)
ax_imp.set_xlabel(
    PLOT_CONFIG["label_x"], fontsize=PLOT_CONFIG["label_size"], labelpad=10
)
ax_imp.set_ylabel(
    PLOT_CONFIG["label_t"], fontsize=PLOT_CONFIG["label_size"], labelpad=10
)
ax_imp.set_zlabel(
    PLOT_CONFIG["label_T"], fontsize=PLOT_CONFIG["label_size"], labelpad=10
)

ax_imp.tick_params(axis="both", which="major", labelsize=PLOT_CONFIG["tick_size"])
ax_imp.view_init(elev=PLOT_CONFIG["view_elev"], azim=PLOT_CONFIG["view_azim"])

cbar_imp = fig_imp.colorbar(
    surf_imp, ax=ax_imp, shrink=0.55, aspect=12, pad=0.1
)
cbar_imp.set_label(
    PLOT_CONFIG["label_T"], fontsize=PLOT_CONFIG["colorbar_label_size"]
)
cbar_imp.ax.tick_params(labelsize=PLOT_CONFIG["tick_size"])

plt.tight_layout()
plt.show()