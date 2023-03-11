import numpy as np
from scipy.stats import norm, uniform

def jitter(n, s):
    n_noise = norm(0, s)
    n = n_noise.rvs(n)
    return n


def line(n, b, s=None):
    if s==None:
        s = 0.05
    x = np.linspace(-1, 1, n)
    y = ((x) + b) + jitter(n, s)

    return x, y


def circle(n, r, s=None):

    if n % 2 == 0:
        m = int(n/2)
    else:
        m = np.floor(n)

    if s==None:
        s = 0.05
    x = np.linspace(-r, r, m)
    y1 = np.sqrt(r-(x)**2) + jitter(m,s)
    y2 = -np.sqrt(r-(x)**2) + jitter(m,s)

    x = np.hstack((x,x))
    y = np.hstack((y1,y2))

    return x, y


def parabola(n, a, s=None):

    if s== None:
        s = 0.05
    x = np.linspace(-1, 1, n)
    y = (a*(x)**2) -1 + jitter(n, s)

    return x, y

