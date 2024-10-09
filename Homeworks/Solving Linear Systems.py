# Exaples of solving linear Sistems


# 1) Solving a big linear system using Gaussian elimination
from sympy import Matrix

# Define the augmented matrix [A|B]
augmented_matrix = Matrix([ 
    [2, 3, -4, 5, 6, 10],
    [1, -2, 3, -4, 5, 20],
    [3, 1, 2, 4, -1, 15],
    [2, -3, 4, 1, 5, 25],
    [4, 2, 3, -1, 2, 30]
])

# Perform row reduction
row_reduced_matrix, _ = augmented_matrix.rref()

print(row_reduced_matrix)             # The solution is in the last column of the row reduced matrix






# 2) Solving a big linear system using Gaussian elimination and variables
from sympy import Matrix, symbols

# Define the variable p
p = symbols('p')

# Define the augmented matrix [A|B] with p included
augmented_matrix = Matrix([ 
    [2, 3, -4, 5, p, 10],
    [1, -2, 3, -4, 5, 20],
    [3, 1, 2, 4, -1, 15],
    [2, -3, 4, 1, p, 25],
    [4, 2, 3, -1, 2, 30]
])

# Perform row reduction
row_reduced_matrix, _ = augmented_matrix.rref()

print(row_reduced_matrix)  # The solution will include expressions involving p





# 3) Solving a small system symbolically
from sympy import Matrix, solve_linear_system, symbols

x, y = symbols('x, y')
A = Matrix(((-2/3, 1/4, 0), 
            (2/3, -1/4, 0)))                # Augmented matrix
solution = solve_linear_system(A, x, y)
print(solution)                         # The system has infinitely many solutions





# 4) Solving a small system numerically 
from sympy import Matrix

# Define the augmented matrix [A|B]
augmented_matrix = Matrix([
    [-2/3, 1/4, 0],
    [2/3, -1/4, 0]
])

# Perform row reduction
row_reduced_matrix, _ = augmented_matrix.rref()

print(row_reduced_matrix)     # Oss: the output in this case is a vector that encodes the 
                              #  infinite solution of the system!




# 5) Solving a linea equation numerically
# eq: q = 1/5 * (q^0 + q^1 + q^2 + q^3 + q^4)
from sympy import symbols, Eq, solve

# Define the variable
q = symbols('q')

# Define the equation
equation = Eq(q, (1/5) * (q**0 + q**1 + q**2 + q**3 + q**4))

# Solve the equation
solution = solve(equation, q)

solution













