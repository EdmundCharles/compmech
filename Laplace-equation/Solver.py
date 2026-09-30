import numpy as np

def SRM(phi_0,phi_m,psi_0,psi_l,l,m,nx,ny,eps,omega = 1, max_iter = 10000):
    if eps <= 0:
        raise ValueError("eps has to be a positive number")
    if omega <= 0 or omega >= 2:
        raise ValueError("0< omega < 2 not satisfied - terminating the process")
    #INIT and BC
    x = np.linspace(0,l,nx)
    y = np.linspace(0,m,ny)

    u = np.zeros((nx,ny))

    u[:,0] = phi_0(x)
    u[:,-1] = phi_m(x)
    u[0,:] = psi_0(y)
    u[-1,:] = psi_l(y)

    #Successive relaxations
    err = 2*eps
    k = 0
    while err > eps and k < max_iter:
        k += 1
        err  = 0
        for i in range(1,nx-1):
            for j in range(1,ny-1):

                u_old = u[i,j]

                u_tilde = 0.25*(u[i+1,j] + u[i-1,j] + u[i,j+1] + u[i,j-1])

                u[i,j] = u[i,j] + omega*(u_tilde - u[i,j])

                diff = abs(u[i,j] - u_old)

                if diff > err: 
                    err = diff

    return  x , y , u , k


