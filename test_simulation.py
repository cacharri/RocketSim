#!/usr/bin/env python3
"""
test_simulation.py

Pruebas unitarias para el módulo simulation.py.
"""

import unittest
import numpy as np
from simulation import simulate_trajectory, GRAVITY

class TestSimulation(unittest.TestCase):

    def test_initial_conditions(self):
        """
        Verifica que en t=0, la posición horizontal y vertical sean 0.
        """
        v0 = 50      # velocidad inicial en m/s
        theta = 45   # ángulo de lanzamiento en grados
        times, positions_x, positions_y = simulate_trajectory(v0, theta, time_step=0.1, total_time=10)
        
        # En t=0, esperamos que positions_x[0] y positions_y[0] sean 0
        self.assertAlmostEqual(positions_x[0], 0, places=5, msg="La posición horizontal en t=0 no es 0.")
        self.assertAlmostEqual(positions_y[0], 0, places=5, msg="La posición vertical en t=0 no es 0.")

    def test_physical_consistency(self):
        """
        Verifica que el tiempo de máxima altura se aproxime al calculado teóricamente:
        t_max = (v0 * sin(theta)) / g.
        """
        v0 = 50
        theta = 45
        theta_rad = np.radians(theta)
        expected_time_of_max_height = v0 * np.sin(theta_rad) / GRAVITY
        
        # Usamos un time_step más pequeño para mayor precisión
        times, positions_x, positions_y = simulate_trajectory(v0, theta, time_step=0.01, total_time=10)
        
        # Encontrar el índice en el que la posición vertical es máxima
        index_max = np.argmax(positions_y)
        time_of_max_height = times[index_max]
        
        self.assertAlmostEqual(time_of_max_height, expected_time_of_max_height, delta=0.1,
                               msg="El tiempo de máxima altura no coincide con el valor teórico.")

    def test_negative_y_at_end(self):
        """
        Verifica que al final de la simulación, la posición vertical sea negativa,
        lo que indica que el proyectil ha "aterrizado".
        """
        v0 = 50
        theta = 45
        times, positions_x, positions_y = simulate_trajectory(v0, theta, time_step=0.1, total_time=15)
        
        # La última posición en y debe ser menor que 0, indicando que ha pasado el punto de aterrizaje.
        self.assertLess(positions_y[-1], 0, msg="La posición vertical final no es negativa.")

if __name__ == '__main__':
    unittest.main()
