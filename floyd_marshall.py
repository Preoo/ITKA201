# Floyd and Mashall method in code

from math import inf

D = [[0, 12, 38, 28],
    [inf, 0, 8, inf],
    [inf, 20, 0, 6],
    [25, 30, inf, 0]]

n = len(D[0])
for k in range(n):
    # generate pairs with generator comprehension
    for i, j in ((i, j) for i in range(n) for j in range(n)):
        D[i][j] = min(D[i][j], D[i][k] + D[k][j])

for row in D:
    print(row)

# Output (prettified by hand):
# [ 0, 12, 20, 26]
# [39,  0,  8, 14]
# [31, 20,  0,  6]
# [25, 30, 38,  0]