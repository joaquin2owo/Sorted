#calculo de la desviacion media para datos no agr

def DM(datos):
    # Calculamos la media de los datos
    media = sum(datos) / len(datos)

    # Calculamos la suma de las diferencias absolutas entre cada dato y la media
    suma_diferencias_absolutas = sum(abs(dato - media) for dato in datos)

    # Calculamos la desviación media dividiendo la suma de las diferencias absolutas por el número de datos
    desviacion_media = suma_diferencias_absolutas / len(datos)

    return desviacion_media
datos = [10, 7, 8, 10, 6]
print(DM(datos))