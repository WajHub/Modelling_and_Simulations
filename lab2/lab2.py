import matplotlib.pyplot as plt
import numpy as np
import math 
from dataclasses import dataclass


# CONST
FIVE_BOUNCES = 5
K = 0.5
G = 10
M = 1

X_PLOT_RANGE_VEC = np.linspace(-15, 15, 100)
Y_PLOT_RANGE_VEC = np.linspace(-15, 15, 100)

X, Y = np.meshgrid(X_PLOT_RANGE_VEC, Y_PLOT_RANGE_VEC)
Z = X**2 + Y**2 + 6*X + 6*Y

# DATA
X_0 = 5
Y_0 = -5
Z_0 = 200

V_0x = 1
V_0y = 3
V_0z = 0

def df_dx(x, y):
    return 2*x + 6

def df_dy(x, y):
    return 2*y + 6

def find_time_collision(
        v_0x, v_0y, v_0z,
        x_0, y_0, z_0
        ):
    a = v_0x**2 + v_0y**2 + 0.5 * G
    b = 2 * x_0 * v_0x + 2 * y_0 * v_0y + 6 * v_0x + 6 * v_0y - v_0z
    c = x_0**2 + y_0**2 + 6 * x_0 + 6 * y_0 - z_0

    roots = np.roots([a, b, c])
    real_roots = roots[np.isreal(roots)].real
    future_roots = real_roots[real_roots > 1e-6]

    t_collision = np.min(future_roots)
    if t_collision <= 0:
        raise ValueError("No future collision found!")
    return float(t_collision)


fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(projection="3d")
ax.plot_surface(X, Y, Z, cmap="viridis", alpha=0.35)
print(f"{'XI':>9} | {'YI':>9} | {'ZI':>9} | {'Δt':>7} | {'E_kin':>9} | {'E_pot':>9} | {'E_total':>9}")
print("-" * 75)

for i in range(FIVE_BOUNCES):
    t_i = find_time_collision(V_0x, V_0y, V_0z, X_0, Y_0, Z_0)

    x = X_0 + V_0x * t_i
    y = Y_0 + V_0y * t_i
    z = Z_0 + V_0z * t_i - 1/2 * G * t_i**2

    v_before = np.array([
        V_0x, 
        V_0y, 
        V_0z - G * t_i
    ])

    dx = df_dx(x, y)
    dy = df_dy(x, y)
    N = np.array([-dx, -dy, 1]) 
    normal_vec = N / np.linalg.norm(N)

    t_points = np.linspace(0.0, t_i, 200)
    x_points = X_0 + V_0x * t_points
    y_points = Y_0 + V_0y * t_points
    z_points = Z_0 + V_0z * t_points - 1/2 * G * t_points**2
    ax.plot3D(x_points, y_points, z_points, linewidth=2)

    e_kin = M * (V_0x ** 2 + V_0y ** 2 + (V_0z - G * t_i) ** 2) / 2
    e_pot = M * G * z
    e_total = e_kin + e_pot

    print(f"{x:9.4f} | {y:9.4f} | {z:9.4f} | {t_i:7.4f} | {e_kin:9.4f} | {e_pot:9.4f} | {e_total:9.4f}")

    v_after = np.sqrt(K) * (v_before - 2 * np.dot(v_before, normal_vec) * normal_vec);
    X_0 = x
    Y_0 = y
    Z_0 = z

    V_0x, V_0y, V_0z = v_after

     
plt.show()

