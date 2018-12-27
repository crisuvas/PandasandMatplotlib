import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.stye.use('ggplot')

expected_profit = 40
expected_time = 10
expected_views = 20
expected_returns = 5

table1 = pd.read_csv('1.csv')
table2 = pd.read_csv('2.csv')
table3 = pd.read_csv('3.csv')

data1 = table1['Ganancias', 'TiempoEnSitio', 'PaginasVistas', 'RegresoVisitas']
data2 = table2['Ganancias', 'TiempoEnSitio', 'PaginasVistas', 'RegresoVisitas']
data3 = table3['Ganancias', 'TiempoEnSitio', 'PaginasVistas', 'RegresoVisitas']

avg1 = data1.apply(np.mean)
avg2 = data2.apply(np.mean)
avg3 = data3.apply(np.mean)

# prepare the graphics the graphic
f, ((ax1, ax2, ax3), (ax4, ax5, ax6), (ax7, ax8, ax9)) = plt.subplots(3, 3, sharey=True)

# make the graphics
# Style 1
ax1.scatter(data1.TiempoEnSitio, data1.Ganancias)

ax1.axvline(expected_time, color='k', linestyle='--')
ax1.axhline(expected_profit, color='k', linestyle='--')

ax1.axvline(avg1.TiempoEnSitio, color='k')
ax1.axhline(avg1.Ganancias, color='k')

ax1.set_title('Style 1')
ax1.set_xlabel('Time')
ax1.set_ylabel('Earn')

# Style 2
ax2.scatter(data2.TiempoEnSitio, data2.Ganancias)

ax2.axvline(expected_time, color='k', linestyle='--')
ax2.axhline(expected_profit, color='k', linestyle='--')

ax2.axvline(avg2.TiempoEnSitio, color='k')
ax2.axhline(avg2.Ganancias, color='k')

ax2.set_title('Style 2')
ax2.set_xlabel('Time')
ax2.set_ylabel('Earn')

# Style 3
ax3.scatter(data3.TiempoEnSitio, data3.Ganancias)

ax3.axvline(expected_time, color='k', linestyle='--')
ax3.axhline(expected_profit, color='k', linestyle='--')

ax3.axvline(avg3.TiempoEnSitio, color='k')
ax3.axhline(avg3.Ganancias, color='k')

ax3.set_title('Style 3')
ax3.set_xlabel('Time')
ax3.set_ylabel('Earn')
