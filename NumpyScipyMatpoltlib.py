#!/usr/bin/env python
# coding: utf-8

# In[18]:


import numpy as np
import scipy as sp
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy.misc
import scipy.integrate

def f(x):
    return x**3 - 300*np.sin(x) - 6
def df(x):
    return sp.misc.derivative(f, x)
@np.vectorize
def F(x):
    return sp.integrate.quad(f, 0, x)[0]
X = np.linspace(-10, 10, 200) # Hier wird der Vektor erzeugt, der im Folgenden verwendet wird
Y = f(X)
Y1 = df(X)
Y2 = F(X)
plt.plot(X, Y, linewidth=2, label="f")
plt.plot(X, Y1, linewidth=2, linestyle="dashed", label="f'")
plt.plot(X, Y2, linewidth=2, linestyle="dotted", label="F")
plt.legend()
plt.show()


# In[20]:


X2 = np.linspace(0, 2*np.pi, 200)
Y2 = np.sin(X2)
plt.plot(X2, Y2)
plt.show()


# In[ ]:




