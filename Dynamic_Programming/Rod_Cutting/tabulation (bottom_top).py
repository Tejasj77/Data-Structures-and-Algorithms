import numpy as np

price = [2,5,7,8]
n = 5

# Make an initial grid of all zeros
T = np.zeros((len(price), n + 1))
print(T)
for i in range(0, len(price)):
    for j in range(0, n + 1):

        # First column => 0 length of rod => 0 profit
        if j == 0:
            continue

        # First row => T[i-1,j] doesn't exist so just pick the second value
        elif i == 0:
            T[i, j] = price[i] + T[i, j - i - 1]

        # where j <= i => T[i, j-i-1] doesn't exist so just pick the first value
        elif (j-i-1)<0:
            T[i, j] = T[i - 1, j]

        # using the whole expression
        else:
            T[i, j] = max(T[i - 1, j], (price[i] + T[i, j - i - 1]))

print(T)
# Answer in the extreme bottom right cell
print("Maximum profit is", T[len(price) - 1, n])

