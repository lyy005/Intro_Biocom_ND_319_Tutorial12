import numpy
import pandas
import plotnine
from plotnine import *

chicken=pandas.read_csv("chickwts.txt", sep=",")
chicken.shape
ggplot(chicken,aes(x="feed",y="weight"))+geom_dotplot(binaxis="y",stackdir="center", stackratio=0.5, dotsize=0.2)+theme_classic()