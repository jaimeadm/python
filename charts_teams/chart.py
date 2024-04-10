import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('semana_telefonia.csv') 

# Form DataFrame from data
df = pd.DataFrame(data, columns=["Dia", "Total de Ligações", "Ligações com Problemas"])
 
font1 = {'family':'serif','color':'black','size':30}

# Plot unstacked multiple columns such from DataFrame
df.plot(x="Dia", y=["Total de Ligações", "Ligações com Problemas"], kind="bar", figsize=(15, 15))
plt.title("Relatório de Telefonia da Última Semana", fontdict=font1)
plt.xticks(rotation=25, ha="right")
 
# Display plot
#plt.show()

# Save to Disk
plt.savefig("tel_chart.png")