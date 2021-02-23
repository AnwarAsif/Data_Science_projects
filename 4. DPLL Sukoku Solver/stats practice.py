import  numpy as np
import random
import matplotlib.pyplot as plt
from scipy.stats import norm
import timeit
import scipy.stats as stats
import statsmodels.api as sm 
import pandas as pd
import math

'''
One population hypothesis testing 

RQ: In previous years 52% of the parents that the electronics and the social media are the cause of their teenager's 
lack of sleep. Do more parents today believe that their teenagers' lack of sleep is caused by social media and and
electronics. 

Population: Parents of the teanagers
Parameter of interest: p (percentage)
Null hypothesis, H0: p = 0.52
Alternative hypothesis, H1: P > 0.52
total parents, n = 1018 
percentage for this year is, p_hat = 0.56

'''
n = 1018
p_null = 0.52
p_hat = 0.56
result = sm.stats.proportions_ztest(p_hat * n, n, p_null)
print(result)
## (2.571067795759113, 0.010138547731721065) 

'''
Difference in population proportion

Is there a significant difference between population proportions of parents of black children and parents of 
hispanic children who are reported that their children had some swiming lesson?

Population: all parents of black children, all parents of hispanic children 
Parameter of interest: p1 - p2, where p1 = black, p2 = hispanic 
Null hypothsis, H0: p1 - p2 = 0 
Alternative, H1: p1 - p2 ≠ 0
'''

n1 = 247
p1 = .37

n2 = 308
p2 = .39

population1 = np.random.binomial(1,p1,n1)
population2 = np.random.binomial(1,p2,n2)

result = stats.ttest_ind(population1, population2)

print(population1.sum())
print(result)


'''
One population Mean 
RQ: is the average cartwheel distance (in inches) for adults more than 80 inches?

population: all adults 
Parameter of Interest: µ, population mean cartwheel distance.
Null hypothesis, H0: µ = 80
Alternat hypothesis, H1: µ > 80

n  = 25
𝜎 = 15.06 

'''

df = pd.DataFrame(np.random.uniform(60, 100, 25 ), columns=["CWDistance"])

x1 = df['CWDistance']
n = len(df['CWDistance'])
mean = df['CWDistance'].mean()
sd = df['CWDistance'].std()
print(n, mean, sd)
value = 80.

test = sm.stats.ztest(x1, alternative='larger', value=value)
print(test)


'''
RQ: Considering adults in the NHANES data, do meales have a significantly higher mean body mass index than females?

Population: Adults in the NHANES data. 
Parameter of Interest: µ1 & µ2, body mass index of male and female
Null Hypothesis, H0: µ1 - µ2 = 0 
Alternative Hypothesis: HA: µ1 ≠ µ2
Given, 
n1 = 2976 female
µ1 = 29.94
sd1 = 7.75

n2 = 2759
µ2 = 28.78
sd2 = 6.26

µ1 - µ2 = 1.16 

test = sn.stats.ztest(x1,x2)

'''


'''
Two-Sample T-Test
A two sample t test investigates wheather the means of two independent data samples different from one another. In a two-sample test, the null hypothesis is that the mean of both gorups are the same. Un
'''

np.random.seed(12)
ages1 = stats.poisson.rvs(size=30, mu=33, loc=18)
ages2 = stats.poisson.rvs(size=20, mu=33, loc=18)

test = stats.ttest_ind(ages1, ages2, equal_var=False)
print(test)

'''
Paired T-test
The basic two sample t-test is desinged for testing differences between independet groups. in some caes, you might be interested in testing different between sampels of the same gorup at diffenet poin in time. 
'''

np.random.seed(11)
dpll = stats.norm.rvs(scale=30, loc=250, size=100)
dpll2 = dpll + stats.norm.rvs(scale=5, loc=-1.25, size=100)

df = pd.DataFrame({"dpll": dpll,
                   'dpll2': dpll2,
                   'change': dpll-dpll2})

#print(df.describe())

print(stats.shapiro(df['dpll']))
print(stats.shapiro(df['dpll2']))
test = stats.ttest_rel(df['dpll'], df['dpll2'])
print(test)

# l = np.random.randint(0,100,1000)

# mean_values = []
# for x in range(10000):
#     m = random.choices(l, k=30)
#     mean_values.append(np.mean(m))
    
# print(np.mean(mean_values))

# plt.plot(mean_values)
# plt.show()


# sizes = [10, 100, 500, 1000, 10000]
# # generate samples of different sizes and calculate their means
# means = [np.mean(5 * np.random.randn(size) + 50) for size in sizes]
# print(means)
# # plot sample mean error vs sample size
# plt.scatter(sizes, np.array(means)-50)
# plt.show()
    