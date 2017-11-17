import pandas
from plotnine import *

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