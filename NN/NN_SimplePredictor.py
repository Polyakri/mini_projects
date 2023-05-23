import random
import matplotlib.pyplot as plt

dataset = []

for _ in range(1000):
  x = random.uniform(-10, 10)  # Random x value between -10 and 10
  y = random.uniform(-10, 10)  # Random y value between -10 and 10

  if x >= y:
    label = 1
  else:
    label = 0

  sample = {'x': x, 'y': y, 'label': label}
  dataset.append(sample)

# Separate x, y, and labels for plotting
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
