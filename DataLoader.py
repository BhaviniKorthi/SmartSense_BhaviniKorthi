import pandas as pd

class DataLoader:
    def modifiedData(self):
        data1 = pd.read_csv('Data/CMO_MSP_Mandi.csv')
        data1.rename(columns = {"commodity": "Commodity", "year": "Year" }, inplace= True)
        data1 ["Commodity"] = data1["Commodity"].str.upper()

        data2 = pd.read_csv('Data/Monthly_data_cmo.csv')
        data2 ["Commodity"] = data2["Commodity"].str.upper()

        final_data = pd.merge(data1, data2, on=['Commodity', 'Year'])

        print("Merged data:", final_data)

        final_data['Date'] = pd.to_datetime(final_data['date'])
        final_data['Month'] = final_data['Date'].dt.month
        final_data['Season'] = (final_data['Month'] % 12 + 3) 


        features_for_Prediction = ['Commodity', 'Year', 'Type', 'APMC', 'Month','arrivals_in_qtl', 'min_price', 'max_price', 'district_name', 'state_name', 'Season']
        target_to_Predict = 'modal_price'
        categorical_columns = ["Commodity", "Type", "APMC", "district_name", "state_name"]
        X = final_data[features_for_Prediction]
        y = final_data[target_to_Predict]

        for i in categorical_columns:
            val = X[i].unique()
            arr = [j for j in range(len(val))]
            X[i].replace(val, arr, inplace=True)

        return X, y