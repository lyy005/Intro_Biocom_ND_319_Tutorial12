
# coding: utf-8

# # General description of "chickwts.txt" dataset.
# 
# 
# 
# ### Import packages and data

# In[20]:

import pandas as pd
import numpy as np
from scipy.stats import chi2
from scipy.optimize import minimize
from scipy.stats import norm
from plotnine import *

chickens=pd.read_table("chickwts.txt", delimiter=",")


# ### 1. Calculate mean weight of chickens based on feed source
# 
# #### create an empty dictionary for "means". Fill by using a for loop to loop through each type of chicken feed, and add the mean weight of chickens for each feed to the dictionary entry for that feed.

# In[21]:

means=dict()

for i in np.unique(chickens.feed):
    means[i]=np.mean(chickens[chickens.feed == i][["weight"]])[0]
    
means_df=pd.DataFrame(means, index =[0])
means_df


# ### 2. Generate a plot summarizing chicken weight data
# 
# #### use ggplot2 to create a boxplot of "chickwts.txt" data, plotting chicken **weight** on the y axis, grouped by chicken **feed**

# In[22]:

ggplot(chickens, aes(x="feed",y="weight")) + geom_boxplot() + theme_classic()


# ### 3. Null and alternative hyptheses for the difference in **chick weight** when fed **soybean feed** vs **sunflower feed**
# 
# #### *Null hypothesis: mean(sunflower)-mean(soybean) = 0*
# 
# #### *Alternative hypothesis: mean(sunflower)-mean(soybean) =/= 0*

# ### 4. Test Null and alternative hypotheses using chi-2 likelihood test
# 
# #### Create a data "sun_soy_chickens" containing only data of interest (chickens fed on soybean or sunflower feed). Add a column "Factor" to this new data frame, containing a 1 for chickens fed with sunflower feed, and a 0 for chickens fed with soybean feed.

# In[23]:

sun_soy_chickens=chickens[(chickens.feed == "sunflower") | (chickens.feed == "soybean")]

sun_soy_chickens["Factor"]=0
for i in range(0, len(sun_soy_chickens.feed)):
    if sun_soy_chickens.feed.iloc[i] == "sunflower":
        sun_soy_chickens.iloc[i,2]=1
    else:
        sun_soy_chickens.iloc[i,2]=0
        
sun_soy_chickens


# #### Define null and alternative hypothesis functions

# In[24]:

def nllalt(p,obs):
    B0=p[0]
    sigma=p[1]
    B1=p[2]
    
    expected=B0+B1*obs.Factor
    nll=-1*norm(expected,sigma).logpdf(obs.weight).sum()
    return nll
    
    
def nllnull(p,obs):
    B0=p[0]
    sigma=p[1]
    
    expected=B0
    nll=-1*norm(expected,sigma).logpdf(obs.weight).sum()
    return nll


# #### Make guess, use minimize function to find optimal coefficients for alternative and null hypothesis functions. T test to determine the significance of the factor (presence of sunflower seed) in determining the weight of chickens in this study

# In[25]:

guess=[1,1,1]

fit_alt=minimize(nllalt, guess, method="Nelder-Mead", options={'disp': True},args=sun_soy_chickens)
fit_null=minimize(nllnull, guess, method="Nelder-Mead", options={'disp': True},args=sun_soy_chickens)

D=2*(fit_null.fun-fit_alt.fun)
1-chi2.cdf(x=D, df=1)


# ### Interpreting the result of the likelihood ratio test
# 
# #### Since the P-value is \<0.05, there is a significant difference in chicken weights between chickens fed on sunflower and soybean feed.
