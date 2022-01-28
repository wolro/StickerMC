import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

plt.ion()

# assuming that there are 200 different stickers to collect
allstickers = pd.DataFrame({'all_stickers':np.arange(1, 201).astype(int)})

mc_runs = 500
dist_missing_stickers = []

for i in range(mc_runs):
    packages = []
    number_draws = 100 # how many packages do we buy?

    for i in range(number_draws):
        packages.append(allstickers.sample(5))        
    bought_packages = pd.concat(packages)

    nr_missing_stickers = len(allstickers) - len(pd.unique(bought_packages['all_stickers'])) 
    dist_missing_stickers.append(nr_missing_stickers) 

# plot the distribution of missing stickers    
sns.distplot(dist_missing_stickers)
plt.ylabel('Fraction of runs')
plt.xlabel('Missing stickers')
plt.title(f'{mc_runs} runs, {number_draws} bought packages')