import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from DataLoader import DataLoader
from LinearRegression import LinearRegressor



X, y = DataLoader().modifiedData()


#Linear Regression model with train vs test split ration as 4 : 1 
lr = LinearRegressor()
lr.Model(X, y)



print("DONE")