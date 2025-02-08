#!/usr/bin/env python3
"""
predictive.py

Módulo para mantenimiento predictivo básico. Este módulo analiza los datos de la posición vertical
provenientes de la simulación para detectar anomalías en la aceleración.
"""

import numpy as np

# Constante de gravedad (m/s²)
GRAVITY = 9.81

def predict_maintenance(times, positions_y, threshold=0.5):
    """
    Analiza los datos de la posición vertical para detectar anomalías en la aceleración.
    
    Se calcula la aceleración numérica a partir de la derivada segunda de positions_y.
    En una simulación ideal, la aceleración debería ser aproximadamente -GRAVITY en todos los puntos.
    Si en algún punto la diferencia absoluta entre la aceleración calculada y (-GRAVITY) es mayor que 
    el umbral (threshold), se marca ese instante como una posible anomalía.
    
    Parámetros:
        times (array): Array de tiempos.
        positions_y (array): Array de posiciones verticales.
        threshold (float): Umbral para detectar desviaciones en la aceleración.
    
    Retorna:
        anomalies (list): Lista de tuplas (time, acceleration, index) donde se detectó una anomalía.
    """
    # Calcular la primera derivada (velocidad vertical) usando np.gradient
    v_y = np.gradient(positions_y, times)
    # Calcular la segunda derivada (aceleración) a partir de la velocidad
    a_y = np.gradient(v_y, times)
    
    anomalies = []
    for i, a in enumerate(a_y):
        # En una simulación perfecta, a_y debe ser aproximadamente -GRAVITY.
        # Si la diferencia es mayor que el umbral, se considera una anomalía.
        if abs(a + GRAVITY) > threshold:
            anomalies.append((times[i], a, i))
    return anomalies

if __name__ == "__main__":
    # Ejemplo de uso del módulo predictivo.
    # Se importa el módulo de simulación para generar datos.
    import simulation
    v0 = 50     # Velocidad inicial en m/s
    theta = 45  # Ángulo de lanzamiento en grados
    
    # Generar la simulación básica
    times, positions_x, positions_y = simulation.simulate_trajectory(v0, theta, time_step=0.1, total_time=10)
    
    # Opcional: Agregar ruido a los datos para simular condiciones reales
    noise = np.random.normal(0, 0.2, size=positions_y.shape)
    positions_y_noisy = positions_y + noise
    
    # Ejecutar el algoritmo predictivo con los datos ruidosos
    anomalies = predict_maintenance(times, positions_y_noisy, threshold=0.5)
    if anomalies:
        print("Anomalías detectadas:")
        for time, acceleration, index in anomalies:
            print(f"Tiempo: {time:.2f} s, Aceleración: {acceleration:.2f} m/s², Índice: {index}")
    else:
        print("No se detectaron anomalías.")
