import sympy as sym
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

# sympy
f = sym.symbols('f', cls=sym.Function)
x = sym.symbols('x')
eq = sym.Eq(f(x).diff(x, 1) + 2 * f(x), 0)
solution = sym.dsolve(eq, f(x), ics={f(0): sym.sqrt(2)})
print(solution)

x_arr = np.arange(0, 10, 0.1)
y_sympy = list(float(solution.args[1].subs(x, i)) for i in x_arr)
print(y_sympy)


# scipy
def dy_dt(y, t):
    return -y * 2


y0 = np.sqrt(2)
y_scipy = odeint(dy_dt, y0, x_arr)
y_scipy = np.array(y_scipy).flatten()

# plot
fig, axs = plt.subplots(2)
fig.set_figheight(8)
plt.subplots_adjust(hspace=0.5)
axs[0].plot(x_arr, y_sympy, '-', color='pink', label='Sympy')
axs[0].plot(x_arr, y_scipy, '--', color='c', label='Scipy')
axs[0].grid()
axs[0].legend()
axs[0].set_title('Решения sympy и scipy')
axs[1].plot(x_arr, abs(y_scipy - y_sympy), color='b')
axs[1].grid()
axs[1].set_title('Разность двух решений')
plt.savefig('plot.png')
