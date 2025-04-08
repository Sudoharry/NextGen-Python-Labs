import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 8, 7]

# Create the plot
plt.plot(x, y, marker='o', linestyle='-', color='b', label='Line 1')

# Add titles and labels
plt.title('Simple Line Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
