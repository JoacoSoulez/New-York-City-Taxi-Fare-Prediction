import pandas as pd
import numpy as np
from TaxiFareModel import data
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
# imports

class Trainer():
    def __init__(self, X, y):
        """
            X: pandas DataFrame
            y: pandas Series
        """
        self.pipeline = None
        self.X = X
        self.y = y

    def set_pipeline(self):
        dist_pipe = Pipeline([
        ('dist_trans', DistanceTransformer()),
        ('stdscaler', StandardScaler())
    ])
        time_pipe = Pipeline([
        ('time_enc', TimeFeaturesEncoder('pickup_datetime')),
        ('ohe', OneHotEncoder(handle_unknown='ignore'))
    ])
        preproc_pipe = ColumnTransformer([
        ('distance', dist_pipe, ["pickup_latitude", "pickup_longitude", 'dropoff_latitude', 'dropoff_longitude']),
        ('time', time_pipe, ['pickup_datetime'])
    ], remainder="drop")
        pipe = Pipeline([
        ('preproc', preproc_pipe),
        ('linear_model', LinearRegression())
    ])
        return pipe

    def run(self):
        pipeline.fit(X, y)
        return pipeline
        

    def evaluate(self, X_test, y_test):
        y_pred = pipeline.predict(X)
        rmse = compute_rmse(y_pred, y)
        print(rmse)
        return rmse
        

if __name__ == "__main__":
    df = data.get_data()
    clean_data = data.clean_data(df)
    y = df.pop("fare_amount")
    X = df
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # get data
    # clean data
    # set X and y
    # hold out
    # train
    # evaluate
    #print('TODO')
