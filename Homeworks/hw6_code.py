import numpy as np

# Ex F.2    (Sucker's Bet)
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
A_idx = [4]

for i in A_idx:       # Skip the 4th element (THH, Alan's choice)
    # Indices for the submatrix
    r_indices = [i]
    q_indices = [x for x in [0, 1, 2, 3, 4, 5, 6, 7] if x != i]

    # Extract the submatrix
    Q = p_matrix[np.ix_(q_indices, q_indices)]
    R = p_matrix[np.ix_(q_indices, r_indices)]

    w = np.linalg.inv(np.eye(7) - Q) @ np.ones(7)

    # print(Q)
    # print(R)
    # print(H)
    print(f"{w}")   # +1 becouse if we start from Brian's choice we already won (w = 0)



