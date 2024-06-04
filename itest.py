import speedtest
import pandas as pd
import time

def data(duracion_minutos):
    st = speedtest.Speedtest()
    resultados = []
    duracion_segundos = duracion_minutos * 60
    intervalo = 5  # segundos

    tiempo_inicio = time.time()
    tiempo_fin = tiempo_inicio + duracion_segundos

    while time.time() < tiempo_fin:
        st.get_best_server()
        servidor = st.results.server['sponsor']
        isp = st.results.client['isp']
        velocidad_descarga = st.download() / 1_000_000  # Mbps
        velocidad_subida = st.upload() / 1_000_000  # Mbps
        timestamp = pd.Timestamp.now()
        
        resultados.append({
            'Timestamp': timestamp,
            'Servidor': servidor,
            'ISP': isp,
            'Velocidad Descarga (Mbps)': velocidad_descarga,
            'Velocidad Subida (Mbps)': velocidad_subida
        })

        df = pd.DataFrame(resultados)
        df.to_csv('resultados_speedtest.csv', index=False)  # Guardar los resultados después de cada medición

        time.sleep(intervalo)

    print("Prueba completada. Resultados guardados en 'resultados_speedtest.csv'")

if __name__ == "__main__":
    duracion_minutos = 10
    data(duracion_minutos)

