import random
import math
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

dataset = []

for _ in range(1000):
    x = random.uniform(-10, 10)  # Random x value between -10 and 10
    y = random.uniform(-10, 10)  # Random y value between -10 and 10
    
    if y >= 10*math.sin(x):
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
x_train, x_test, y_train, y_test = train_test_split(x_values, y_values, test_size=0.2, random_state=42)

x_values = [sample['x'] for sample in dataset]
y_values = [sample['y'] for sample in dataset]
labels = [sample['label'] for sample in dataset]

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