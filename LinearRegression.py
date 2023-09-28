import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


class LinearRegressor:

    def Model(self, X, y ):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = LinearRegression()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        print(pd.DataFrame({"original":y_test, "Predicted":y_pred}))

        mse = mean_squared_error(y_test, y_pred)
        rmse = mse**0.5
        print(f'Root Mean Squared Error: {rmse}')
    