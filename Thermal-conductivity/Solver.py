import numpy as np
###################################################
def explicit(phi, psi_0, psi_l, t_star, l, nt, nh):
    #Initial and boundary conditions application
    h = l/(nh - 1)
    dt = t_star/(nt - 1)
    curant = dt/h**2
    if curant > 0.5:
        print("Warning the explicit scheme might be unstable, consider choosing dt/h^2 < 0.5")
    T = np.zeros([nt,nh])

    t = np.linspace(0, t_star, nt)
    x = np.linspace(0,l,nh)

    T_init = phi(x)
    T_l = psi_0(t)
    T_r = psi_l(t)

    T[0] = T_init
    T[:,0] = T_l
    T[:,nh - 1] = T_r
    #Solution 
    for k in range(0,nt - 1):
        for i in range(1,nh - 1):
            T[k+1,i] = dt/h**2*(T[k,i-1]-2*T[k,i] + T[k,i+1]) + T[k,i]

    return x,t,T



###################################################
def implicit(phi, psi_0, psi_l, t_star, l, nt, nh):
    h = l / (nh - 1)
    dt = t_star / (nt - 1)

    t = np.linspace(0, t_star, nt)
    x = np.linspace(0, l, nh)


    a = -1.0 / h**2
    c = -1.0 / h**2
    b = (h**2 + 2 * dt) / (dt * h**2)


    deltas = np.zeros(nh)
    den = np.zeros(nh)


    deltas[0] = 0.0

    for i in range(1, nh - 1):
        den[i] = b + a * deltas[i - 1]
        deltas[i] = -c / den[i]


    T = np.zeros((nt, nh))
    T[0, :] = phi(x)

    lambdas = np.zeros(nh)


    for k in range(1, nt):
        t_curr = t[k]

        lambdas[0] = psi_0(t_curr)

        for i in range(1, nh - 1):
            f_i = T[k - 1, i] / dt
            lambdas[i] = (f_i - a * lambdas[i - 1]) / den[i]

        T[k, -1] = psi_l(t_curr)

        for i in range(nh - 2, -1, -1):
            T[k, i] = deltas[i] * T[k, i + 1] + lambdas[i]

    return x,t,T





# def implicit(phi, psi_0, psi_l, t_star, l, nt, nh):
#         h = l/(nh - 1)
#         dt = t_star/(nt - 1)

#         t = np.linspace(0, t_star, nt)
#         x = np.linspace(0,l,nh)
        
#         A , C, B, F = np.zeros(nh), np.zeros(nh), np.zeros(nh), np.zeros(nh)
#         #A, B, C are independent relative to time frame
#         #i = 0
#         B[0] = 1
#         #i = nh
#         B[-1] = 1

#         #i = 1, ... , nh - 1
#         A[1:nh] = -1/h**2
#         C[1:nh] = -1/h**2
#         B[1:nh] = (h**2 + 2*dt)/(dt*h**2)

#         T = np.zeros([nt,nh])
#         T[0] = phi(x)
#         ###SOLVE THE SYSTEM###
        
#         ##Forward
#         deltas = np.zeros(nh)
#         lambdas = np.zeros(nh)
#         # i = 0
#         deltas[0] = C[0]/B[0]
#         lambdas[0] = F[0]/B[0]
#         for i in range(1,nh):
#             den = B[i] + A[i]* deltas[i-1]
#             deltas[i] = - C[i] / den
#         for k in range(1,nt):
#             F[0] = psi_0(k*dt)
#             F[-1] = psi_l(k*dt)
#             F[1:nh] = T[1:nh,k]/dt
#             # i = 1, …, n - 1
#             for i in range(1,nh):
#                 lambdas[i] = (F[i] - A[i] * lambdas[i-1]) / den
#             # i = n
#             lambdas[-1] = 0

#             #Backward
#             T = np.zeros(n+1)
#             T[-1] = lambdas[-1]
#             for i in range(n - 1, -1, -1):
#                 T[i] = deltas[i]*T[i+1] + lambdas[i]
            
#         return T