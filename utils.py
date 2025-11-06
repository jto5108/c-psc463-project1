import numpy as np


def corr_distance(a, b):
a, b = a - np.mean(a), b - np.mean(b)
return 1 - np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def dtw_distance(a, b):
n, m = len(a), len(b)
D = np.full((n+1, m+1), np.inf)
D[0, 0] = 0
for i in range(1, n+1):
for j in range(1, m+1):
cost = (a[i-1] - b[j-1])**2
D[i, j] = cost + min(D[i-1, j], D[i, j-1], D[i-1, j-1])
return np.sqrt(D[n, m])
