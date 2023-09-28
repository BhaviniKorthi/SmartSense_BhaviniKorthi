# SmartSense_BhaviniKorthi


## Files attached:
1. Datasets
2. Predictions: Calls all the models to predict the price
3. DataLoader: Loads and manipulates the data from the given datasets
4. LinearRegression: Contains the Linear Regression Model.


## INSTRUCTIONS TO RUN:
1. Install the requirements using "requirements.txt"
2. Run the Predictions.py file in the CLI.
3. The output is displayed on the CLI itself.

## Data Visualization:
Dataset 1: CMO_MSP_Mandi

![image](https://github.com/BhaviniKorthi/SmartSense_BhaviniKorthi/assets/76489649/cfe04f25-028b-471f-b867-9f6025eeab61)

Dataset 2: Monthly_data_cmo

![image](https://github.com/BhaviniKorthi/SmartSense_BhaviniKorthi/assets/76489649/21d73cae-f7b9-456c-add9-4f3269603dfb)


The final data after merging the two given datasets:

![image](https://github.com/BhaviniKorthi/SmartSense_BhaviniKorthi/assets/76489649/2e9201d9-a4ec-4ff1-a0f6-450ea020edec)


## Prediction:

* In order to fit the data into the linear regression model, all the categorical values are modified into continuous values.
* Here, the columns Commodity, Type, APMC, district_name, and state_name are categorical in nature and, hence are modified into continuous values by assigning a unique value to them.
  
  ![image](https://github.com/BhaviniKorthi/SmartSense_BhaviniKorthi/assets/76489649/3c748ed0-3926-452a-92b5-d725a8a5f46e)


* The whole data is split into train and test in the ratio of 4 : 1
* Note that the value to be predicted here is "median_price"
* Therefore, y will be "median_price"

## Output:
* These are the original and predicted values of "median_price"

![image](https://github.com/BhaviniKorthi/SmartSense_BhaviniKorthi/assets/76489649/d74bec30-1b67-47da-88ab-e73cd50c9749)


The RMSE value is observed to be around 245 rupees.


