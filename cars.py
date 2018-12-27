import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')

table1 = pd.read_csv('Caliente.csv')
table2 = pd.read_csv('Frio.csv')

data1 = table1
data2 = table2

# prepare the graphics the graphic
f, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2, 3, sharey=True)

# make the graphics
# Style 1
ax1.scatter(data1.millasg, data1.Automovil)

ax1.set_title('Style 1')
ax1.set_xlabel('miles')

# Style 2
ax2.scatter(data1.desp, data1.Automovil)

ax2.set_title('Style 2')
ax2.set_xlabel('desp')

# Style 3
ax3.scatter(data1.tiempo, data1.Automovil)

ax3.set_title('Style 3')
ax3.set_xlabel('tiempo')

# Style 4
ax4.scatter(data2.millasg, data1.Automovil)

ax4.set_title('Style 4')
ax4.set_xlabel('miles')

# Style 5
ax5.scatter(data2.desp, data1.Automovil)

ax5.set_title('Style 5')
ax5.set_xlabel('desp')

# Style 6
ax6.scatter(data2.tiempo, data1.Automovil)

ax6.set_title('Style 6')
ax6.set_xlabel('tiempo')

plt.show()
