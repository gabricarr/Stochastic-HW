import numpy as np

# Ex G.4
# Define the transition matrix
P = np.array([
    [0, 0.1, 0.5, 0.4],   # Dorms (D)
    [0.6, 0, 0.1, 0.3],   # Gym (G)
    [0.5, 0.1, 0, 0.4],   # Library (L)
    [0.6, 0.2, 0.2, 0]    # Student Union (U)
])

print("Transition matrix P:")
print(P)


stationary = np.ones(4).T @ np.linalg.inv(np.eye(4) - P + np.ones((4, 4)))
print("Stationary distribution:")
print(stationary)




# Ex 2.27
import numpy as np
print("\n\nEx 2.27\n")


print("States from 0 to 5")
# Define the transition matrix
P = np.array([
    [0.0, 0.0, 0.0, 0.0, 0.0, 1],  # From state 0
    [0.5, 0.5, 0.0, 0.0, 0.0, 0.0],  # From state 1
    [0.0, 0.25, 0.75, 0.0, 0.0, 0.0],  # From state 2
    [0.0, 0.0, 0.2, 0.8, 0.0, 0.0],  # From state 3
    [0.0, 0.0, 0.0, 0.1, 0.9, 0.0],  # From state 4
    [0.0, 0.0, 0.0, 0.0, 0.05, 0.95]  # From state 5
])

print("Transition Matrix:")
print(P)

# Profits vector
f = np.array([-10000, 200, 500, 750, 900, 1000])


# Stationary distribution
stationary = np.ones(P.shape[0]).T @ np.linalg.inv(np.eye(P.shape[0]) - P + np.ones(P.shape))
print("Stationary distribution:")
print(stationary)

# Expected profit
expected_profit = stationary @ f
print("Expected profit:", expected_profit)


# 2 to 5
print("\n\nStates from 2 to 5")
# Define the transition matrix
P = np.array([
    [0.0, 0.0, 0.0, 1],  # From state 2
    [0.2, 0.8, 0.0, 0.0],  # From state 3
    [0.0, 0.1, 0.9, 0.0],  # From state 4
    [0.0, 0.0, 0.05, 0.95]  # From state 5
])

print("Transition Matrix:")
print(P)

# Profits vector
f = np.array([-7500, 750, 900, 1000])


# Stationary distribution
stationary = np.ones(P.shape[0]).T @ np.linalg.inv(np.eye(P.shape[0]) - P + np.ones(P.shape))
print("Stationary distribution:")
print(stationary)

# Expected profit
expected_profit = stationary @ f
print("Expected profit:", expected_profit)




# 3 to 5
print("\n\nStates from 3 to 5")
# Define the transition matrix
P = np.array([
    [0.0, 0.0, 1],  # From state 3
    [0.1, 0.9, 0.0],  # From state 4
    [0.0, 0.05, 0.95]  # From state 5
])

print("Transition Matrix:")
print(P)

# Profits vector
f = np.array([-6000, 900, 1000])


# Stationary distribution
stationary = np.ones(P.shape[0]).T @ np.linalg.inv(np.eye(P.shape[0]) - P + np.ones(P.shape))
print("Stationary distribution:")
print(stationary)

# Expected profit
expected_profit = stationary @ f
print("Expected profit:", expected_profit)




# 4 to 5
print("\n\nStates from 4 to 5")
# Define the transition matrix
P = np.array([
    [0.0, 1],  # From state 4
    [0.05, 0.95]  # From state 5
])

print("Transition Matrix:")
print(P)

# Profits vector
f = np.array([-5000, 1000])


# Stationary distribution
stationary = np.ones(P.shape[0]).T @ np.linalg.inv(np.eye(P.shape[0]) - P + np.ones(P.shape))
print("Stationary distribution:")
print(stationary)

# Expected profit
expected_profit = stationary @ f
print("Expected profit:", expected_profit)



























