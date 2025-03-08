# import matplotlib.pyplot as plt
# import numpy as np

# y = np.array([35, 25, 25, 15])

# plt.pie(y)
# plt.show() 



# import matplotlib.pyplot as plt
# import numpy as np

# y = np.array([35, 25, 25, 15])
# mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

# plt.pie(y, labels = mylabels)
# plt.show()


import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.5, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode)
plt.show() 