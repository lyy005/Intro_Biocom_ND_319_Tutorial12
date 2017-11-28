import numpy
import pandas
from plotnine import *

#read data
data=pandas.read_csv("chickwts.txt",sep=",",header=0)

#produce barplot
barplot=ggplot(data)+theme_classic()+xlab("feed")+ylab("weight")
barplot+geom_bar(aes(x="factor(feed)",y="weight"),stat="summary",fun_y=numpy.mean)