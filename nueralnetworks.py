import math

# Sigmoid function
def sigmoid(x): 
    return 1 / (1 + math.exp(-x))

# Simple neural network with 2 inputs, 1 output
def nn(x):
    w1, w2, b = 0.5, -0.5, 0
    return sigmoid(x[0]*w1 + x[1]*w2 + b)

# Test
inputs = [[0,0],[0,1],[1,0],[1,1]]
for i in inputs:
    print(f"Input: {i}, Output: {nn(i):.2f}")
