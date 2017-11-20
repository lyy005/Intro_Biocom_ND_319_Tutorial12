import numpy
import pandas
import plotnine
from plotnine import *
from scipy.optimize import minimize 
from scipy.stats import norm

chicken=pandas.read_csv("chickwts.txt", sep=",")
chicken.shape
ggplot(chicken,aes(x="feed",y="weight"))+geom_dotplot(binaxis="y",stackdir="center", stackratio=0.5, dotsize=0.2)+theme_classic()

#subset data into different data frames 
sub1=chicken.loc[chicken.feed.isin(['soybean','sunflower']),:]

#Make new data frame with 'group' column (your x=0 or x=1)
#var2=pandas.DataFrame({'y':var1.col2name, 'x':})
sub1frame=pandas.DataFrame({'y':sub1.feed,'x':0})

#Designate 'treatment' group as x=1
#var2.loc[var1.col1name=='name of treatment group', 'x']=1
sub1frame.loc[sub1.weight=='sunflower','x']=1


