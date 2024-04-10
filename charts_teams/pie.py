import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Total de Ligações', 'Ligações com Problemas'
total = [1600, 5]
explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(total, explode=explode, colors=['green', 'red'], labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=60, textprops={'fontsize': 12})
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.legend(["Total de Ligações", "Ligações com Problemas"], fontsize="10", loc ="upper left")
ax1.set_title("Relatório de Telefonia", fontsize="20")

#plt.show()
plt.savefig('chart.png')

