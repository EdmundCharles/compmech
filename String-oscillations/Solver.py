import numpy as np

import numpy as np


def explicit(phi_0, phi_1, psi_0, psi_l, t_star, l, nt, nh, a=1.0):
    h = l / (nh - 1)
    dt = t_star / (nt - 1)

    courant = a * dt / h
    if courant > 1.0:
        print("Warning the explicit scheme might be unstable, consider choosing a*dt/h <= 1")

    t = np.linspace(0, t_star, nt)
    x = np.linspace(0, l, nh)

    PHI_0 = phi_0(x)
    PHI_1 = phi_1(x)
    PSI_0 = psi_0(t)
    PSI_l = psi_l(t)

    u = np.zeros([nt, nh])

    u[0] = PHI_0
    u[:, 0] = PSI_0
    u[:, -1] = PSI_l

    coeff = (a * dt / h) ** 2

    u[1, 1:-1] = (PHI_0[1:-1] + PHI_1[1:-1] * dt + 0.5 * coeff * (PHI_0[:-2] - 2 * PHI_0[1:-1] + PHI_0[2:]))

    for k in range(1, nt - 1):
        u[k + 1, 1:-1] = (2 * u[k, 1:-1] - u[k - 1, 1:-1] + coeff * (u[k, :-2] - 2 * u[k, 1:-1] + u[k, 2:]))

    return x, t, u

def implicit(phi_0, phi_1, psi_0, psi_l, t_star, l, nt, nh, a=1.0):
    h = l / (nh - 1)
    dt = t_star / (nt - 1)

    t = np.linspace(0, t_star, nt)
    x = np.linspace(0, l, nh)

    PHI_0 = phi_0(x)
    PHI_1 = phi_1(x)
    PSI_0 = psi_0(t)
    PSI_l = psi_l(t)

    u = np.zeros([nt, nh])

    u[0] = PHI_0
    u[:, 0] = PSI_0
    u[:, -1] = PSI_l

    coeff = (a * dt / h) ** 2

    u[1, 1:-1] = (PHI_0[1:-1] + PHI_1[1:-1] * dt + 0.5 * coeff * (PHI_0[:-2] - 2 * PHI_0[1:-1] + PHI_0[2:]))

    #Construct the systlem
    a_coef = -1/h**2
    c_coef = -1/h**2
    b_coef = (2*a**2*dt**2 + h**2)/(h**2*a**2*dt**2)

    deltas = np.zeros(nh)
    den = np.zeros(nh)


    deltas[0] = 0.0

    for i in range(1, nh - 1):
        den[i] = b_coef + a_coef * deltas[i - 1]
        deltas[i] = -c_coef / den[i]

    lambdas = np.zeros(nh)
    a2_dt2 = (a**2*dt**2)
    for k in range(1, nt - 1):
        t_next = t[k+1]

        lambdas[0] = psi_0(t_next)

        
        for i in range(1, nh - 1):
            f_i = (2*u[k,i] - u[k-1,i])/ a2_dt2
            lambdas[i] = (f_i - a_coef * lambdas[i - 1]) / den[i]


        for i in range(nh - 2, -1, -1):
            u[k+1, i] = deltas[i] * u[k+1, i + 1] + lambdas[i]

    return x,t,u
