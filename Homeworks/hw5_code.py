import numpy as np

# Ex E.4    (Sucker's Bet)
print("Ex E.4")

# Create a 8x8 matrix filled with zeros
p_matrix = np.zeros((8, 8))

# Build transition probabilities
for n in range(8):
    j = 2*n % 8
    j_1 = (2*n + 1) % 8
    i = n

    p_matrix[i, j] = 0.5
    p_matrix[i, j_1] = 0.5

print(p_matrix)


# Calculating the probabilities
S = ['HHH', 'HHT', 'HTH', 'HTT', 'THH', 'THT', 'TTH', 'TTT']

for i in [0, 1, 2, 3, 5, 6, 7]:       # Skip the 4th element (THH, Alan's choice)
    # Indices for the submatrix
    r_indices = [4, i]
    q_indices = [x for x in [0, 1, 2, 3, 5, 6, 7] if x != i]

    # Extract the submatrix
    Q = p_matrix[np.ix_(q_indices, q_indices)]
    R = p_matrix[np.ix_(q_indices, r_indices)]

    H = np.linalg.inv(np.eye(6) - Q) @ R

    # print(Q)
    # print(R)
    # print(H)
    print(f"P(Brian chooses {S[i]}): {(np.sum(H[:,1]) + 1) / 8}")   # +1 becouse if we start from Brian's choice we already won




####################################################################################################
# Ex E.1   (Earnhest's Urn)
print("\n\n\nEx E.1")

# Create a 11x11 matrix filled with zeros
N = 5                                  # Number of balls
p_matrix = np.zeros((N+1, N+1))
for i in range(p_matrix.shape[0]):
    for j in range(p_matrix.shape[1]):
        if j == i-1:
            p_matrix[i, j] = i/N 
        elif j == i+1:
            p_matrix[i, j] = 1 - i/N

print(p_matrix)



for i in [1, 2, 3, 4, 5,]:
    print(f"P^{i}:")
    print(np.linalg.matrix_power(p_matrix, i))
    print("\n\n")



P3 = np.linalg.matrix_power(p_matrix, 3)

print(f"P^3 column mean:")
print(P3.mean(axis=0))
print("\n\n")





####################################################################################################
# Ex E.2
import scipy.stats as stats

# Values of binomial distribution
# Parameters
n = 5
p = 0.5

# Create a binomial distribution object
binom_dist = stats.binom(n, p)

# Calculate the PMF for all possible values (0 to n)
x = np.arange(0, n + 1)
pmf_values = binom_dist.pmf(x)

# Print the PMF values
for k, pmf in zip(x, pmf_values):
    print(f"P(X = {k}) = {pmf:.4f}")


# Calculate Probability that X_3 = j
u = pmf_values
Prob = u.T @ P3

print("\nDistribution of X_3 given binomial initial conditions:")
print(Prob)








