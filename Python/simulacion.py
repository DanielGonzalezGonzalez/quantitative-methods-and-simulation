import numpy as np
from sklearn.decomposition import PCA
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale

# np.seterr(divide='ignore', invalid='ignore')


#Load data set
data = pd.read_csv('Datos.csv')
# del data['date_account_created']
# del data['date_first_active']
# del data['date_first_booking']
# del data['signup_method']
#

# print data.head()


#TODO
# data = data[['age','secs_elapsed']]
data = data['age']

# data = data[data.secs_elapsed != 0]
#
#
# for i in data['secs_elapsed']:
#   if i == 0:
#     print 'PUTA'





#convert it to numpy arrays
X=data.values

#Scaling the values
X = scale(X)

#TODO
X = X.reshape(-1,1) # for 1 value
# X = X.reshape(1,-1) # for more than 1 value

pca = PCA(n_components=1) #TODO

pca.fit(X)

#The amount of variance that each PC explains
var= pca.explained_variance_ratio_

#Cumulative Variance explains
var1=np.cumsum(np.round(pca.explained_variance_ratio_, decimals=4)*100)

print var1

plt.plot(var1)

#Looking at above plot I'm taking 30 variables
pca = PCA(n_components=1)
pca.fit(X)
X1=pca.fit_transform(X)

print X1
