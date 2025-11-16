#First install
#pip install numpy pandas scikit-learn keras tensorflow yfinance matplotlib

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
from sklearn.metrics import accuracy_score

# Step 1: Download Google stock price data using Yahoo Finance
# You can change the start and end date to get more historical data.
ticker = 'GOOGL'
data = yf.download(ticker, start='2015-01-01', end='2023-01-01')

# Step 2: Prepare the data
# Use 'Close' price for predictions
data = data[['Close']]
data = data.dropna()

# Step 3: Normalize the data
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(data)

# Step 4: Create a dataset for the RNN
# Use the last 60 days of data to predict the next day
def create_dataset(dataset, time_step=60):
    X, Y = [], []
    for i in range(len(dataset) - time_step - 1):
        X.append(dataset[i:(i + time_step), 0])
        Y.append(dataset[i + time_step, 0])
    return np.array(X), np.array(Y)

time_step = 60
X, Y = create_dataset(scaled_data, time_step)

# Step 5: Reshape input data to 3D for LSTM [samples, time steps, features]
X = X.reshape(X.shape[0], X.shape[1], 1)

# Step 6: Split the data into training and testing sets
train_size = int(len(X) * 0.8)
X_train, X_test = X[:train_size], X[train_size:]
Y_train, Y_test = Y[:train_size], Y[train_size:]

# Step 7: Build the RNN model using LSTM layers
model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], 1)))
model.add(LSTM(units=50, return_sequences=False))
model.add(Dense(units=25))
model.add(Dense(units=1))

# Step 8: Compile and train the model
model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(X_train, Y_train, batch_size=64, epochs=20)

# Step 9: Predict stock prices for the test set
predictions = model.predict(X_test)
predictions = scaler.inverse_transform(predictions.reshape(-1, 1))

# Step 10: Calculate accuracy for increase/decrease trend
Y_test_actual = scaler.inverse_transform(Y_test.reshape(-1, 1))

# Step 11: Determine if the price is increasing or decreasing
# (if tomorrow's price > today's price -> increase, else decrease)
pred_trend = np.where(predictions[1:] > predictions[:-1], 1, 0)
actual_trend = np.where(Y_test_actual[1:] > Y_test_actual[:-1], 1, 0)

# Calculate accuracy
accuracy = accuracy_score(actual_trend, pred_trend) * 100
print(f'Trend Prediction Accuracy: {accuracy:.2f}%')

# Step 12: Plot the predictions and actual prices
plt.figure(figsize=(14, 7))
plt.plot(Y_test_actual, color='blue', label='Actual Google Stock Price')
plt.plot(predictions, color='red', label='Predicted Google Stock Price')
plt.title('Google Stock Price Prediction')
plt.xlabel('Time')
plt.ylabel('Stock Price')
plt.legend()
plt.show()
