import random
import math
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow.keras import layers

dataset = []

for _ in range(1000):
  x = random.uniform(-10, 10)  # Random x value between -10 and 10
  y = random.uniform(-10, 10)  # Random y value between -10 and 10

  if y >= 10 * math.sin(x):
    label = 1
  else:
    label = 0

  sample = {'x': x, 'y': y, 'label': label}
  dataset.append(sample)

# Separate x, y, and labels for plotting
x_values = [sample['x'] for sample in dataset]
y_values = [sample['y'] for sample in dataset]
labels = [sample['label'] for sample in dataset]

# Split dataset into train and test sets
x_train, x_test, y_train, y_test = train_test_split(x_values,
                                                    y_values,
                                                    test_size=0.2,
                                                    random_state=42)

# Convert lists to numpy arrays
x_train = np.array(x_train)
y_train = np.array(y_train)

# Normalize the input features
x_train = (x_train - np.mean(x_train)) / np.std(x_train)
y_train = (y_train - np.mean(y_train)) / np.std(y_train)

# Build the neural network model
model = keras.Sequential([
  layers.Dense(16, activation='relu', input_shape=(1, )),
  layers.Dense(16, activation='relu'),
  layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=10, batch_size=32)

# Generate new random test data
x_test_new = np.random.uniform(-10, 10, size=100)
y_test_new = np.random.uniform(-10, 10, size=100)

# Normalize the input features
x_test_new = (x_test_new - np.mean(x_test_new)) / np.std(x_test_new)
y_test_new = (y_test_new - np.mean(y_test_new)) / np.std(y_test_new)

# Perform predictions
predictions = model.predict(np.column_stack((x_test_new, y_test_new)))

# Create a scatter plot
plt.scatter(x_values, y_values, c=labels, cmap='viridis')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Dataset Visualization')
plt.colorbar(label='Class')
plt.show()

# Create a scatter plot for training set
plt.scatter(x_train, y_train, c='blue', label='Train')
# Create a scatter plot for testing set
plt.scatter(x_test, y_test, c='red', label='Test')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Dataset Split Visualization')
plt.legend()
plt.show()

# Plot the predictions for new data
plt.scatter(x_test_new, y_test_new, c=predictions.flatten(), cmap='viridis')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Predictions for New Data')
plt.colorbar(label='Prediction')
plt.show()
