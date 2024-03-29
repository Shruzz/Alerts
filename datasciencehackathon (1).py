# -*- coding: utf-8 -*-
"""DataScienceHackathon.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14IdPFyf7mMjBmZADuOAldep4kA1dlzwk
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

d1=pd.read_csv(r"/content/iraste_nxt_cas.csv")
d2=pd.read_csv(r"/content/iraste_nxt_casdms.csv")

d1

d2

df=pd.concat([d1,d2],ignore_index=True)

df

df.shape

df.info()

df.isnull().sum()

df=df.fillna(method='ffill')

df.isnull().sum()

df.duplicated().sum()

df=df.drop_duplicates()

df.duplicated().sum()

df.describe()

df.describe(include="all")

df.skew()

"""If skewness is negative, the distribution is skewed to the left (longer tail on the left side).
If skewness is positive, the distribution is skewed to the right (longer tail on the right side).
If skewness is close to zero, the distribution is approximately symmetric.

"""

df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'])
df.drop(['Date', 'Time'], axis=1, inplace=True)

plt.hist(df['Speed'], bins=10, color='skyblue', edgecolor='black')
plt.xlabel('Speed')
plt.ylabel('Frequency')
plt.title('Speed Distribution')
plt.show()

df.hist(layout=(1,6), figsize=(18,3))
plt.show()

sns.boxenplot(data=df, x='Speed')
plt.show()

plt.figure(figsize=(10,7))
sns.scatterplot(y=df['DateTime'], x=df['Speed'])
plt.show()

from statsmodels.tsa.seasonal import seasonal_decompose
df.set_index('DateTime', inplace=True)
decomposition = seasonal_decompose(df['Speed'], model='additive', period=1)

plt.figure(figsize=(10, 8))

plt.subplot(4, 1, 1)
plt.plot(df['Speed'], label='Original', color='blue')
plt.legend(loc='upper left')

plt.subplot(4, 1, 2)
plt.plot(decomposition.trend, label='Trend', color='red')
plt.legend(loc='upper left')

plt.subplot(4, 1, 3)
plt.plot(decomposition.seasonal, label='Seasonal', color='green')
plt.legend(loc='upper left')

plt.subplot(4, 1, 4)
plt.plot(decomposition.resid, label='Residual', color='purple')
plt.legend(loc='upper left')

plt.tight_layout()
plt.show()

df

sns.heatmap(df.corr(),annot=True)

sns.scatterplot(data=df,x='Long',y='Vehicle')

plt.figure(figsize=(15,3))
sns.scatterplot(data=df, x='Alert', y='Speed', hue='Vehicle')
plt.show()

"""(i) Forward Collision Warning - FCW,

(ii) Pedestrian Collision Warning - PCW,


(iii) Headway Monitoring and Warning - HMW, and

(iv) Lane Departure Warning - LDW.

(i) Forward Collision Warning - FCW,

(ii) Pedestrian Collision Warning - PCW,

(iii) Headway Monitoring and Warning - HMW, and

(iv) Lane Departure Warning - LDW.
"""

sns.scatterplot(data=df,x='Alert',y='Vehicle')

#exploring categorical values
df['Alert'].value_counts()

plt.figure(figsize=(15,3))
sns.barplot(x=df['Alert'].value_counts().index,
            y=df['Alert'].value_counts().values)
plt.show()

plt.figure(figsize=(10,7))
plt.pie(x=df['Alert'].value_counts().values,
        labels=df['Alert'].value_counts().index,
        autopct='%2.2f%%')
plt.show()

pd.crosstab(index=df['Alert'], columns=df['Vehicle'])

grid = sns.FacetGrid(data=df, col='Alert', height=4, aspect=1, sharey=False)

grid.map(sns.countplot, 'Vehicle', palette=['black', 'brown', 'orange'])
plt.show()

grid = sns.FacetGrid(data=df, col='Alert', height=4, aspect=1, sharey=False)

grid.map(sns.countplot, 'Speed', palette=['black', 'brown', 'orange'])
plt.show()

df.columns

y=df['Alert']
x=df.drop('Alert',axis=1)

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y)

from sklearn.linear_model import LogisticRegression
model=LogisticRegression()

model.fit(x_train,y_train)

pred=model.predict(x_test)
from sklearn.metrics import accuracy_score
accu=accuracy_score(y_test,pred)
accu

from sklearn.naive_bayes import GaussianNB
model1=GaussianNB()
model1.fit(x_train,y_train)
pred1=model1.predict(x_test)
from sklearn.metrics import accuracy_score
accu1=accuracy_score(y_test,pred1)
accu1

