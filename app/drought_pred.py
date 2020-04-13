import numpy as np
import pandas as pd 
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

county = pd.read_csv('../input/united-states-droughts-by-county/county_info_2016.csv', encoding = 'ISO-8859-1')
drought = pd.read_csv('../input/united-states-droughts-by-county/us-droughts.csv')

print("1")

# CLEANING DATA AND SELECTING FEATURES
county = county.dropna(axis=0)
drought = drought.dropna(axis=0)

# Merging county and drought data
df = pd.merge(left=county, right=drought, left_on='GEOID', right_on='FIPS')

print("2")

# Calculating drought occurrences
locations = df['GEOID']
dr_freq = { loc : 0 for loc in locations }
for dr in df.index:
    if (df['NONE'][dr]) != 100.0:
            dr_freq[df['GEOID'][dr]] += 1

dr = pd.DataFrame(list(dr_freq.items()), columns=['GEOID', 'DroughtOccurrence'])

print("3")
        
# Adding drought occurrence to df
df_final = pd.merge(left=df, right=dr, left_on='GEOID', right_on='GEOID')

print('4')

# Feature selection
features = ['GEOID', 'ALAND', 'AWATER', 'NONE', 'D0', 'D1', 'D2', 'D3', 'D4']
X = df_final[features]
y = df_final.DroughtOccurrence
# features = ['GEOID', 'ALAND', 'AWATER']
# X = df[features]
# y = df.NONE

# LINEAR REGRESSION MODEL
train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.3, random_state = 0)
model = LinearRegression().fit(train_X, train_y)

pred = model.predict(test_X)