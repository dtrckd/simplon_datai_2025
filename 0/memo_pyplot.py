import numpy as np
import matplotlib.pyplot as plt


#
#   _____ _                 _                        _____   ___  _____
#  / ____(_)               | |                 /\   |_   _| |__ \| ____|
# | (___  _ _ __ ___  _ __ | | ___  _ __      /  \    | |      ) | |__
#  \___ \| | '_ ` _ \| '_ \| |/ _ \| '_ \    / /\ \   | |     / /|___ \
#  ____) | | | | | | | |_) | | (_) | | | |  / ____ \ _| |_   / /_ ___) |
# |_____/|_|_| |_| |_| .__/|_|\___/|_| |_| /_/    \_\_____| |____|____/
#                    | |
#                    |_|
#
#
#   Pyplot memo
#   --
#   The plot functions that are used most frequently
#   and that you need to know.
#
#   try it> python memo_pyplot.py


# Scatter plot
x = np.random.rand(100)
y = np.random.rand(100)
colors = np.where(x < 0.5, 'r', 'b')
plt.scatter(x, y, c=colors, label='Data Points')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.legend()
plt.title("Scatter plot")
plt.show()

# Line plot
x = np.linspace(0, 12, 50)
y = np.sin(x)
plt.plot(x, y, ".-", label='Sine Wave')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.legend()
plt.title("Line plot")
plt.show()

# Bar plot
x = ['A', 'B', 'C', 'D']
y = [10, 5, 8, 12]
plt.bar(x, y, label='Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.legend()
plt.title("Bar plot")
plt.show()

# Histogram
data = np.random.randn(2000)
plt.hist(data, bins=50, label='Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()
plt.title("Histogram")
plt.show()

# Pie chart
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.axis('equal')
plt.legend()
plt.title("Pie chart / Camenbert")
plt.show()
