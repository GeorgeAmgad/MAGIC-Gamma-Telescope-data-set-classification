import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier, export_graphviz
import graphviz
from sklearn import tree
import os
import numpy as np
import sklearn

# to download these libraries
# open the terminal and type : pip install +library name
# example : pip install pandas
names = ["length", "width", "size", "conc", "conc1",
         "asym", "m3long", "m3trans", "alpha", "dist", "class"]

train = pd.read_csv('train.txt', names=names)
test = pd.read_csv('test.txt', names=names)

sns.pairplot(x_vars=["size"], y_vars=["alpha"], data=train, hue="class",
             palette=["green", "grey"], height=15)

plt.show()

array = train.values
X = array[:, 0:10]
Y = array[:, 10]


os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'


dt = DecisionTreeClassifier(min_samples_split=3, random_state=99)
dt.fit(X, Y)

dot_data = tree.export_graphviz(dt, out_file=None, class_names=True)
graph = graphviz.Source(dot_data)
graph.render("image", view=True)
