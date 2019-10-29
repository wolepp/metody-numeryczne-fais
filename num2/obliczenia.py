import math
import numpy as np

A = np.array([[64.054,-8.021,-39.907,-15.991,-7.994],
    [-8.021,1.267,4.989,1.957,0.87],
    [-39.907,4.989,25.199,9.935,4.966],
    [-15.991,1.957,9.935,4.225,1.996],
    [-7.994,0.87,4.966,1.996,1.242]])

x1 = np.array([0.23,1.12,0.32,0.4,0.72])
x2 = np.array([0.2218,1.121,0.3251,0.4021,0.721])
x3 = np.array([0.231,1.122,0.318,0.438,0.714])
x4 = np.array([0.238,1.1343,0.3218,0.4443,0.7261])

y1 = np.linalg.solve(A, x1)
y2 = np.linalg.solve(A, x2)
y3 = np.linalg.solve(A, x3)
y4 = np.linalg.solve(A, x4)

W1 = np.linalg.norm(y1-y2) / np.linalg.norm(x1-x2)
W2 = np.linalg.norm(y3-y4) / np.linalg.norm(x3-x4)

print('y1:', y1)
print('y2:', y2)
print('y3:', y3)
print('y4:', y4)

print('w1:', W1)
print('w2:', W2)
print('różnica:', W1 - W2)
