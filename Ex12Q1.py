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
sub1=chicken.loc[chicken.feed.isin(['soybean']),:]
sub2=chicken.loc[chicken.feed.isin(['sunflower']),:]


