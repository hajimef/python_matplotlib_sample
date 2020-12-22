import matplotlib.pyplot as plt

plt.figure(dpi = 120, figsize = (16, 9))
x = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ]
y = [ 5.6, 7.2, 10.6, 13.6, 20.0, 21.8, 24.1, 28.4, 25.1, 19.4, 13.1, 8.5 ]
plt.plot(x, y, label = "Average temperature")
plt.grid()
plt.legend()
plt.xlabel("Month")
plt.ylabel("Temperature")
plt.title("Changes in average temperature in Tokyo")
plt.savefig("graph.png", format = "png")
plt.show()
