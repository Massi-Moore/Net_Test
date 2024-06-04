import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos desde el archivo CSV
df = pd.read_csv('resultados_speedtest.csv')

# Graficar
plt.figure(figsize=(10, 6))
plt.plot(df['Timestamp'], df['Velocidad Descarga (Mbps)'], label='Descarga', marker='o')
plt.plot(df['Timestamp'], df['Velocidad Subida (Mbps)'], label='Subida', marker='o')
plt.title('Velocidad de Descarga y Subida en el Tiempo')
plt.xlabel('Tiempo')
plt.ylabel('Velocidad (Mbps)')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("graph.pdf")
plt.show()
