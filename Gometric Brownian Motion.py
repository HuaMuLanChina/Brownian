'''https://blog.csdn.net/IT__LS/article/details/78555072
    插值法
'''

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10,10))

T = 2
mu = 0.1
sigma = 0.04
S0 = 20
dt = 0.01
N = round(T/dt)
t = np.linspace(0, T, N)

W = np.random.standard_normal(size = N)
W = np.cumsum(W)*np.sqrt(dt)

X = (mu-0.5*sigma**2)*t + sigma*W

S = S0*np.exp(X)


plt.plot(t,S,lw=2)
plt.xlabel("Timt t", fontsize=16)
plt.ylabel("S", fontsize=16)
plt.title("Gometric Brownian Motion (Simulation)", fontsize=18)
plt.show()