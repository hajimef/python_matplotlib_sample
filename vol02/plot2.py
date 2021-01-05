import matplotlib.pyplot as plt

x = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ]
y_tokyo = [ 5.6, 7.2, 10.6, 13.6, 20.0, 21.8, 24.1, 28.4, 25.1, 19.4, 13.1, 8.5 ]
y_sapporo = [ -3.0, -2.6, 2.5, 8.0, 15.7, 17.4, 21.7, 22.5, 19.3, 13.3, 3.9, -0.8 ]
y_naha = [ 18.1, 20.0, 19.9, 22.3, 24.2, 26.5, 28.9, 29.2, 28.0, 26.0, 23.1, 20.0 ]
plt.figure(dpi = 120, figsize = (16, 9))
plt.plot(x, y_tokyo, marker = "o", linestyle = "-", linewidth = 3, color ="blue", markeredgecolor = "red", markersize = 10, markeredgewidth = 3, label = "Tokyo")
plt.plot(x, y_sapporo, marker = "s", linestyle = "--", linewidth = 3, color = "green", markeredgecolor = "red", markersize = 10, markeredgewidth = 3, label = "Sapporo")
plt.plot(x, y_naha, marker = "x", linestyle = "-.", linewidth = 3, color = "r", markeredgecolor = "blue", markersize = 10, markeredgewidth = 3, label = "Naha")
plt.xlabel("Month")
plt.ylabel("Average temperature")
plt.grid()
plt.legend()
plt.savefig("graph2.png", format = "png")
plt.show()
