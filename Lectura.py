from __future__ import print_function
import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv
import math
import datetime
from scipy import stats

# Set figure aesthetics
sns.set_style("white", {'ytick.major.size': 10.0})
sns.set_context("poster", font_scale=1.1)

# Load the data into DataFrames
train_users = pd.read_csv('train_users_2.csv')
test_users = pd.read_csv('test_users.csv')
sessions_users = pd.read_csv('sessions.csv')
cleanSessions = pd.read_csv('Datos.csv')


# Merge train and test users
# users = pd.concat((train_users, test_users), axis=0, ignore_index=True)
# users.head()
#
# users.gender.replace('-unknown-', np.nan, inplace=True)
# users_nan = (users.isnull().sum() / users.shape[0]) * 100
# users_nan[users_nan > 0].drop('country_destination')
# users.age.describe()
# users[users.age > 122]['age'].describe()
# users[users.age < 18]['age'].describe()
# users.loc[users.age > 95, 'age'] = np.nan
# users.loc[users.age < 13, 'age'] = np.nan
#
# ########################################
# categorical_features = [
#     'affiliate_channel',
#     'affiliate_provider',
#     'country_destination',
#     'first_affiliate_tracked',
#     'first_browser',
#     'first_device_type',
#     'gender',
#     'language',
#     'signup_app',
#     'signup_method'
# ]
#
# for categorical_feature in categorical_features:
#     users[categorical_feature] = users[categorical_feature].astype('category')
#
# users['date_account_created'] = pd.to_datetime(users['date_account_created'])
# users['date_first_booking'] = pd.to_datetime(users['date_first_booking'])
# #print(users)
# users['date_first_active'] = pd.to_datetime((users.timestamp_first_active // 1000000), format='%Y%m%d')
#
#
# cleanUsers = users[users['date_first_booking'].notnull()]
# cleanUsers = cleanUsers.sort_values(['id'], ascending=[1])
# notCleanUseres = users[users['date_first_booking'].isnull()]
# sessions_users.rename(columns={'user_id':'id'}, inplace=True)
#
# # #Plot de porcetaje de edades
# # plt.xlabel("Edad")
# # plt.ylabel("Porcentaje")
# # sns.distplot(cleanUsers.age.dropna(), color='#FD5C64')
# # sns.despine()
#
# cleanSessions = cleanUsers[cleanUsers['date_first_booking'] > pd.to_datetime(20130101, format='%Y%m%d')]
# cleanSessions = cleanSessions[cleanSessions['date_first_booking'] < pd.to_datetime(20140101, format='%Y%m%d')]
# cleanSessions['date_first_booking'] = cleanSessions['date_first_booking'].astype("datetime64[ns]")
#
# grpby = sessions_users.groupby(['id'])['secs_elapsed'].sum().reset_index()
# grpby.columns = ['id','secs_elapsed']
#
# cleanGroupSec = grpby[grpby['secs_elapsed'].notnull()]
#
# cleanSessions = cleanUsers.merge(cleanGroupSec, how="left")
#
# #Limpiamos los NaNs en secs_elapsed
# cleanSessions = cleanSessions[~np.isnan(cleanSessions['secs_elapsed'])]
# #Limpiamos los NaN en age
# cleanSessions = cleanSessions[~np.isnan(cleanSessions['age'])]
#
#
#
# cont = 0
# for x in cleanSessions['secs_elapsed']:
#     cleanSessions['secs_elapsed'][cont] = math.ceil(x.astype(float) / 60)
#     cont += 1
#
# plt.show()
#
# cleanSessions.to_csv("Datos.csv")


#Plot de first booking en meses
#cleanSessions['date_first_booking'].groupby(cleanSessions['date_first_booking'].dt.month).count().plot(kind="line")


cleanSessions['date_first_booking'] = pd.to_datetime(cleanSessions['date_first_booking'])
cleanSessions['date_account_created'] = pd.to_datetime(cleanSessions['date_account_created'])
cleanSessions['bookingtime'] = cleanSessions['date_first_booking'] - cleanSessions['date_account_created']

#print(cleanSessions['bookingtime'])

#Plot de buckets de tiempo
cleanSessions['bookingtime'].groupby(cleanSessions['bookingtime'].dt.day).sum().plot(kind='bar')


plt.xlabel("Tiempo")
plt.ylabel("Cantidad")
plt.show()

###########
#Funciones
def printStatistics():
    row, minmax, mean, variance, skewness, kurtosis = stats.describe(cleanSessions['age'])
    print('*Age descriptive statistics*\n''rows: ', row, '\t', 'min and max: ', minmax, '\t', 'mean: ', '{0:.5g}'.format(mean), '\t', 'variance: ', '{0:.5g}'.format(variance), '\t', 'skewness: ', '{0:.5g}'.format(skewness), '\t', 'kurtosis: ', '{0:.5g}'.format(kurtosis), '\n')

    row, minmax, mean, variance, skewness, kurtosis = stats.describe(cleanSessions['min_elapsed'])
    print('*Sessions duration descriptive statistics*\n''rows: ', row, '\t', 'min and max: ', minmax, '\t', 'mean: ', '{0:.5g}'.format(mean), '\t', 'variance: ', '{0:.5g}'.format(variance), '\t', 'skewness: ', '{0:.5g}'.format(skewness), '\t', 'kurtosis: ', '{0:.5g}'.format(kurtosis), '\n')
