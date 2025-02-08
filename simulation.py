#!/usr/bin/env python3
"""
simulation.py

Módulo básico para simular la trayectoria de un proyectil basado en
física clásica. Este script calcula y grafica la trayectoria de un
cohete utilizando la velocidad inicial y el ángulo de lanzamiento.
"""

import math
import numpy as np
import matplotlib.pyplot as plt

# Constante de gravedad (en m/s^2)
GRAVITY = 9.81

def simulate_trajectory(v0, theta, time_step=0.1, total_time=10):
    """
    Simula la trayectoria de un proyectil.

    Parámetros:
        v0 (float): Velocidad inicial en m/s.
        theta (float): Ángulo de lanzamiento en grados.
        time_step (float): Intervalo de tiempo para la simulación.
        total_time (float): Tiempo total de simulación.
    
    Retorna:
        tuple: (times, positions_x, positions_y)
    """
    theta_rad = math.radians(theta)
    times = np.arange(0, total_time, time_step)
    positions_x = v0 * math.cos(theta_rad) * times
    positions_y = v0 * math.sin(theta_rad) * times - 0.5 * GRAVITY * times**2
    return times, positions_x, positions_y

def plot_trajectory(times, positions_x, positions_y):
    """
    Grafica la trayectoria del proyectil y la guarda en un archivo.
    
    Parámetros:
        times (array): Array de tiempos.
        positions_x (array): Posiciones horizontales.
        positions_y (array): Posiciones verticales.
    """
    plt.figure(figsize=(8, 4))
    plt.plot(positions_x, positions_y, label="Trayectoria")
    plt.title("Simulación de Trayectoria de Proyectil")
    plt.xlabel("Distancia (m)")
    plt.ylabel("Altura (m)")
    plt.legend()
    plt.grid(True)
    
    # Guardar la gráfica en un archivo en lugar de mostrarla interactivamente.
    plt.savefig("trajectory.png")
    print("La gráfica se ha guardado en 'trajectory.png'.")

def main():
    # Ejemplo de uso del módulo
    v0 = 50     # Velocidad inicial en m/s
    theta = 45  # Ángulo de lanzamiento en grados
    
    times, positions_x, positions_y = simulate_trajectory(v0, theta, time_step=0.1, total_time=10)
    plot_trajectory(times, positions_x, positions_y)

if __name__ == "__main__":
    main()
