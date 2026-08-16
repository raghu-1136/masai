import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

def build_baseline_and_model(data: dict):
    # TODO: build a DataFrame from `data`
    df = pd.DataFrame(data)
   
   # TODO: separate input features (car_age, km_driven_k) from the target (price_k)
    car_x = df.drop("price_k",axis =1)
    car_y = df["price_k"]

    # TODO: split into train/test with test_size=0.2, random_state=42
    car_X_train, car_X_test, car_y_train, car_y_test = train_test_split(
    car_x,
    car_y,
    test_size=0.20,
    random_state=42
    )

    # TODO: build baseline predictions using the mean of the training target
    baseline_value = car_y_train.mean()

    baseline_predictions = [baseline_value] * len(car_y_test)

    baseline_mae = mean_absolute_error(
        car_y_test,
        baseline_predictions
    )

    
    # TODO: fit a LinearRegression model on the training data only
    linear_model = LinearRegression()

    linear_model.fit(
         car_X_train,
         car_y_train
    )

    linear_predictions = linear_model.predict(
        car_X_test
    )
    linear_mae = mean_absolute_error(
        car_y_test,
        linear_predictions
    )
    # TODO: compute MAE for both the baseline and the fitted model on the test set
    return{
        "baseline_mae": baseline_mae,
        "fitted_mae": linear_mae
    }

if __name__ == "__main__":
    sample_data = {
        "car_age": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "km_driven_k": [15, 20, 25, 40, 55, 60, 70, 85, 95, 110],
        "price_k": [20, 19, 18, 16, 15, 14, 12, 11, 9, 8],
    }
    print(build_baseline_and_model(sample_data))
