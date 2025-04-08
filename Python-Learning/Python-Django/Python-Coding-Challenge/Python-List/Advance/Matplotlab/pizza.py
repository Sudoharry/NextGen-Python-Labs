import matplotlib.pyplot as plt

# Data
labels = ['Pepperoni', 'Mushrooms', 'Onions', 'Sausage', 'Extra cheese']
sizes = [30, 25, 15, 20, 10]  # Percentage of votes
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']
explode = (0.1, 0, 0, 0, 0)  # "Explode" the 1st slice (Pepperoni)

# Create pie chart
plt.figure(figsize=(7,7))
plt.pie(sizes, labels=labels, colors=colors, explode=explode, 
        autopct='%1.1f%%', shadow=True, startangle=140)

plt.title("🍕 Favorite Pizza Toppings")
plt.axis('equal')  # Equal aspect ratio ensures a circular pie chart
plt.show()
