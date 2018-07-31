# Import modules
# Import Keras library
from keras.models import Sequential
from keras.layers import Dense

# Import scikit-learn
from sklearn.model_selection import train_test_split

# Import NumPy
import numpy as np

# Dummy data (replace X_data with hospital dataset and y with PIA Time)
X_data = np.array([[1,2,3,4,5],
                 [1,2,3,4,5],
                 [1,2,3,4,5],
                 [1,2,3,4,5],
                 [1,2,3,4,5]]) # input data
y = np.array([1,1,1,1,1])

# Reshape data
y = y.reshape(len(y), -1)

# Split training and testing data
X_train, X_test, y_train, y_test = train_test_split(X_data, y, test_size=0.2)

# Build model
model = Sequential()
model.add(Dense(10, input_dim=X_train.shape[1], activation="sigmoid"))
model.add(Dense(5, activation="sigmoid"))
model.add(Dense(1, activation="sigmoid"))
model.compile(loss="mean_squared_error", optimizer="adam", metrics=['accuracy'])

# Run model
history = model.fit(X_train, y_train, epochs=50, batch_size=2, validation_split=0.2)

# Accuracy of neural network
los, acc = model.evaluate(X_test, y_test)
print(f"Loss: {los}")
print(f"Accuracy: {acc*100}")

# Used for predictions
pred = model.predict(X_test)
print("PREDICTIONS:")
for item in pred:
    print(f"prediction: {item}")

# Save model for future use
model.save("model.h5")
