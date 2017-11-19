import numpy
import pandas
from plotnine import *
from scipy.optimize import minimize
from scipy.stats import norm

weights=pandas.read_csv("chickwts.txt", header=0, sep=",")

horsebean=weights.loc[weights.feed.isin(['horsebean']),:]
linseed=weights.loc[weights.feed.isin(['linseed']),:]
soybean=weights.loc[weights.feed.isin(['soybean']),:]
sunflower=weights.loc[weights.feed.isin(['sunflower']),:]
meatmeal=weights.loc[weights.feed.isin(['meatmeal']),:]
casein=weights.loc[weights.feed.isin(['casein']),:]

g=ggplot(horsebean,aes(x='feed',y='weight'))+geom_point()+theme_classic()
g=g+geom_point(linseed, aes(x='feed',y='weight'))+theme_classic()
g=g+geom_point(soybean, aes(x='feed',y='weight'))+theme_classic()
g=g+geom_point(sunflower, aes(x='feed',y='weight'))+theme_classic()
g=g+geom_point(meatmeal, aes(x='feed',y='weight'))+theme_classic()
g=g+geom_point(casein, aes(x='feed',y='weight'))+theme_classic()

frames=[soybean,sunflower]

df=pd.concat(frames)
df.replace(['soybean','sunflower'],[0,1],inplace=True)

def null(p,obs):
    B0=p[0]
    sigma=p[1]
    expected=B0
    nll=-1*norm(expected,sigma).logpdf(obs.weight).sum()
    return nll

def alt(p,obs):
    B0=p[0]
    B1=p[1]
    sigma=p[2]
    expected=B0+B1*obs.feed
    nll=-1*norm(expected,sigma).logpdf(obs.weight).sum()

initVals=numpy.array([1,1,1])

fitNull=minimize(null,initVals,method="Nelder-Mead",options={'disp':True},args=df)
fitAlt=minimize(alt,initVals,method="Nelder-Mead",options={'disp':True},args=df)

print(fitNull.x)
print(fitAlt.x)
########################
#null hypothesis likelihood equation
def null(p,obs):
    B0=p[0]
    sigma=p[1]
    expected=B0
    nll=-1*norm(expected,sigma).logpdf(obs.weight).sum()
    return nll

#Alternative hypothesis likelihood equation
def alt(p,obs):
    B0=p[0]
    B1=p[1]
    sigma=p[2]
    expected=B0+B1*obs.feed
    nll=-1*norm(expected,sigma).logpdf(obs.weight).sum()
    return nll

#estimaitng parameters by minimizing the nll 
initialVals1=numpy.array([1,1,1])

fitNull=minimize(null,initialVals1, method="Nelder-Mead",options={'disp': True}, args=df)
fitAlt=minimize(alt,initialVals1, method="Nelder-Mead",options={'disp': True}, args=df)

print(fitNull.x)
print(fitAlt.x)

from scipy.stats import chi2
D=(2*(fitNull.fun-fitAlt.fun))
chi2feed=(1-chi2.cdf(x=D,df=1))
print(chi2feed)
