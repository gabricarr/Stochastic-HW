


# ex 1.3
from sympy import symbols, Eq, solve

# Define the variable
q = symbols('q')

# Define the equation
equation = Eq(q, (1/5) * (q**0 + q**1 + q**2 + q**3 + q**4))

# Solve the equation
solution = solve(equation, q)

print(solution)




















