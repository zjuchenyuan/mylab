# encoding:utf-8
# # {{{ http://code.activestate.com/recipes/414200/ (r1)
#!/usr/bin/env python
# Author:      Flávio Codeço Coelho
# License:     GPL

from math import *
# from RandomArray import *
from matplotlib.pylab import *

def sdnorm(z):
    """
    Standard normal pdf (Probability Density Function)
    """
    return exp(-z * z / 2.) / sqrt(2 * pi)

n = 10000
alpha = 1
x = 100.
vec = []
vec.append(x)
res = []
innov = uniform(-alpha, alpha, n)  # random innovation, uniform proposal distribution
for i in xrange(1, n):
    can = x + innov[i]  # candidate
    aprob = min([1., sdnorm(can) / sdnorm(x)])  # acceptance probability
    u = uniform(0, 1)
    if u < aprob:
        x = can
        vec.append(x)
    res.append(x)

print float(len(vec)) / n
# plotting the results:
# theoretical curve
x = arange(-3, 3, .1)
y = sdnorm(x)
subplot(211)
title('Metropolis-Hastings')
plot(vec)
subplot(212)

hist(vec, bins=30, normed=1)
plot(x, y, 'ro')
ylabel('Frequency')
xlabel('x')
legend(('PDF', 'Samples'))
show()
# # end of http://code.activestate.com/recipes/414200/ }}}
