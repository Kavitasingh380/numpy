
# =============================================================================
# 9. Plotting a distribution with seaborn
# =============================================================================
# import matplotlib.pyplot as plt       # matplotlib does the actual drawing

# import seaborn as sns                 # seaborn = easier, nicer statistical plots on top of matplotlib
# sns.displot([0, 1, 2, 3, 4, 5], kind="kde")   # kde = smooth curve showing how the values are spread
# plt.show()                            # open the plot window

#normal Distribution(Gaussian)

# from numpy import random
# arr = random.normal(loc=1,scale=2,size=(2,3))
# # print(arr)


# sns.displot(random.normal(loc=50,scale=5, size=1000),kind= "kde")
# plt.show()


#binomial distribution
# from numpy import random
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.displot(random.binomial(n=100,p=0.5,size=1000),kde=False)
# plt.show()



# poisson distribution
# from numpy import random
# import matplotlib.pyplot as plt 
# import seaborn as sns
# sns.displot(random.poisson(lam=2,size=1000),kde=False)
# plt.show()

# difference between Normal and poisson

# from numpy import random
# import matplotlib.pyplot as plt 
# import seaborn as sns

# # kdeplot draws only the smooth curve, and both curves go on the same axes so they can be compared
# sns.kdeplot(random.normal(loc=50,scale=7,size=1000), label='Normal')
# sns.kdeplot(random.poisson(lam=50,size=1000), label='Poisson')
# plt.legend()                          # show the 'Normal' / 'Poisson' labels
# plt.show()



#uniform distribution

# from numpy import random
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.kdeplot(random.uniform(size=1000))
# plt.show()


#logistic distribution

# from numpy import random
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.kdeplot(random.logistic(size=1000))
# plt.show()


#chi square distribution 
# from numpy import random 
# arr = random.chisquare(df=2,size=(2,3))
# print(arr)
# import matplotlib.pyplot as plt 
# import seaborn as sns
# sns.kdeplot(random.chisquare(df=1,size=1000))
# plt.show()

#pareto distribution 
# from numpy import random 
# arr = random.pareto(a=2,size=(2,3))
# print(arr)
# import matplotlib.pyplot as plt 
# import seaborn as sns
# sns.kdeplot(random.pareto(a=5,size=1000))
# plt.show()


#zipf distribution 
# from numpy import random
# arr = random.zipf(a=2,size=(2,3))
# print(arr)
# import matplotlib.pyplot as plt 
# import seaborn as sns
# sns.kdeplot(random.zipf(a=2,size=1000))
# plt.show()

