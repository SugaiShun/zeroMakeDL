
# def AND(x1,x2):
#     w1, w2, theta = 0.5, 0.5, 0.7
#     tmp = x1 * w1 + x2 * w2
#     if tmp <= theta:
#         return 0
#     else:
#         return 1

# print(AND(0,0))
# print(AND(1,0))
# print(AND(0,1))
# print(AND(1,1))

import numpy as np

# x = np.array([0,1])
# w = np.array([0.5,0.5])
# b = -0.7

# print(w*x)
# print(np.sum(w*x))
# print(np.sum(w*x)+b)

def AND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.7
    tmp = np.sum(x*w) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def NAND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([-0.5,-0.5])
    b = 0.7
    tmp = np.sum(x*w) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def OR(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.2
    tmp = np.sum(x*w) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def XOR(x1,x2):
    s1 = NAND(x1,x2)
    s2 = OR(x1,x2)
    y = AND(s1,s2)
    return y

def step_function(x):
    return np.array(x>0,dtype=np.int)

def sigmoid(x):
    return 1 / (1+np.exp(-x))

import matplotlib.pylab as plt

x = np.arange(-10.0,10.0,0.1)
# y = step_function(x)
y = sigmoid(x)
plt.plot(x,y)
plt.ylim(-0.1,1.1)
plt.show()
