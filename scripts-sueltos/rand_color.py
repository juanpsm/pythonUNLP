import matplotlib.pyplot as plt
import random

number_of_colors = 8

color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
             for i in range(number_of_colors)]
print(color)

# ~ ['#C7980A', '#F4651F', '#82D8A7', '#CC3A05', '#575E76', '#156943', '#0BD055', '#ACD338']

# ~ Lets try plotting them in a scatter plot

for i in range(number_of_colors):
    plt.scatter(random.randint(0, 10), random.randint(0,10), c=color[i], s=200)

plt.show()
