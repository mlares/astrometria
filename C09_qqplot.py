import numpy as np
import statsmodels.api as sm
import pylab
import stats

#test = np.random.normal(0,1, 1000)
#test = np.random.uniform(0,1, 1000)


test = np.random.weibull(1, 1000)

sm.qqplot(test, line='45')
pylab.show()

