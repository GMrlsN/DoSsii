import pandas as pd
from google.colab import drive
import matplotlib.pyplot as plt
drive.mount('/content/drive')

!ls "/content/drive/My Drive/Colab Notebooks"

import numpy as np
from matplotlib import colors
import seaborn as sb
plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.native_bayes import GaussianNB
from sklearn.feature_selection import SelectKBest

dataframe = pd.read_csv(r"/content/drive/My Drive/Colab Notebooks/iris.csv")
dataframe.head(10)

print(dataframe.groupby('species').size())
dataframe.drop(['comprar'], axis=1).hist()
plt.show()
#-------------------------
dataframe['gastos']=(dataframe['gastos_comunes']+dataframe['gastos_otros']+dataframe['pago_coche'])
dataframe['financiar']=dataframe['vivienda']-dataframe['ahorros']
dataframe.drop(['gastos_comunes','gastos_otros','pago_coche','vivienda','ahorros'], axis=1).hist(10)
#-------------------------
reduced = dataframe.drop(['gastos_comunes','gastos_otros','pago_coche'], axis=1)
reduced.describe()
#-------------------------

x=dataframe.drop(['comprar'], axis=1) #entrada
y=dataframe['comprar'] # salida
#-------------------------

best=SelectKBest(k=5)
x_new=best.fit_transform(x,y)
x_new.shape
selected = best.get_support(indices=True)
print(x.columns[selected])

#-------------------------

used_features =x.columns[selected]

colormap = plt.cm.viridis
plt.figure(figsize=(12,12))
plt.title('pearson correlation of features', y=1.05, size=15)
sb.heatmap(dataframe[used_features].astype(float).corr(),linewidths=0.1,vmax=1.0, square=True, cmap=colormap, linecolor='white', annot=True)
