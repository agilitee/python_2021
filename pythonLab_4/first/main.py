from sympy import symbols, Matrix
import sympy

r, m, l, x = symbols('r, m, l, x')

a = Matrix.zeros(9)
b = Matrix.eye(9)

a[0, 3] = a[1, 4] = a[2, 5] = -1 / r
a[3, 0] = -(l + 2 * m)
a[4, 1] = a[5, 2] = -m
a[6, 0] = a[8, 0] = -l

determinant = sympy.det(a - x * b)
eigvals = sympy.solve(determinant, x)
print(eigvals)
