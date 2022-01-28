import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

plt.ion()

# assuming that there are 200 different stickers to collect
allstickers = pd.DataFrame({'all_stickers':np.arange(1, 201).astype(int)})

mc_runs = 500           # number of iterations for the monte carlo
nr_packages_dist = []
runtime_dist = []

for i in range(mc_runs):
    
    exit_condition = False
    packages = []    
    cntr = 0

    while exit_condition == False:   
        packages.append(allstickers.sample(5))        
        bought_packages = pd.concat(packages)
        nr_missing_stickers = len(allstickers) - len(pd.unique(bought_packages['all_stickers'])) 
        cntr += 1
        if nr_missing_stickers == 0: # we break if we have collected all stickers
            exit_condition = True
            
    printstr = f'run {i} out of {mc_runs}'
    print(printstr)
    nr_packages_dist.append(cntr)

avg_buys = np.round(np.mean(nr_packages_dist)).astype(int)


# plot the histogram and empirical cumulative distribution using seaborn
plt.figure()
plt.subplot(2,1,1)
plt.title('Probability to collect all stickers vs. bought packages')
sns.distplot(nr_packages_dist)
plt.xlabel('Number of bought packages')
plt.ylabel('PDF')
plt.xlim(0, 510)
plt.legend([f'Data; average: {avg_buys}'])
plt.subplot(2,1,2)
kwargs = {'cumulative': True}
sns.distplot(nr_packages_dist, hist_kws = kwargs, kde_kws = kwargs)
plt.xlabel('Number of bought packages')
plt.ylabel('CDF')
plt.tight_layout()
plt.xlim(0, 510)
