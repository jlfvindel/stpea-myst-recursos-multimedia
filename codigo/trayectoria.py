"""Trayectoria de un proyectil sin rozamiento.

Calcula la posición (x, y) a lo largo del tiempo para una velocidad
inicial v0 (m/s) y un ángulo de lanzamiento (grados).
"""
import math

G = 9.81  # aceleración de la gravedad (m/s²)


def trayectoria(v0, angulo_grados, pasos=50):
    """Devuelve una lista de puntos (t, x, y) hasta que el proyectil cae."""
    theta = math.radians(angulo_grados)
    vx = v0 * math.cos(theta)
    vy = v0 * math.sin(theta)
    t_vuelo = 2 * vy / G
    puntos = []
    for i in range(pasos + 1):
        t = t_vuelo * i / pasos
        x = vx * t
        y = vy * t - 0.5 * G * t**2
        puntos.append((t, x, y))
    return puntos


def alcance(v0, angulo_grados):
    """Distancia horizontal recorrida: R = v0² · sen(2θ) / g."""
    theta = math.radians(angulo_grados)
    return v0**2 * math.sin(2 * theta) / G


if __name__ == "__main__":
    for angulo in (30, 45, 60):
        print(f"{angulo}°: alcance = {alcance(20, angulo):.1f} m")
