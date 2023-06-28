import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

# Constants
G = 9.81  # Gravity constant (m/s^2)
MUZZLE_VELOCITIES = [158, 212, 272, 320, 362]  # m/s corresponding to the five-part propelling charge system
AMMO_TYPES = ['high-explosive', 'incendiary', 'chemical']
FUZE_SETTINGS = ['delayed-action', 'contact']
MAX_CEP = 300  # Maximum CEP in meters


def get_input():
    print("Select ammo type:")
    for index, ammo_type in enumerate(AMMO_TYPES, start=1):
        print(f"{index}. {ammo_type}")
    ammo_selection = int(input("Enter the number corresponding to ammo type: "))
    ammo_type = AMMO_TYPES[ammo_selection - 1]

    print("Select fuze setting for 53-F-864:")
    for index, fuze_setting in enumerate(FUZE_SETTINGS, start=1):
        print(f"{index}. {fuze_setting}")
    fuze_selection = int(input("Enter the number corresponding to fuze setting: "))
    fuze_setting = FUZE_SETTINGS[fuze_selection - 1]

    charge_part = int(input("Enter propellant charge part (1-5): "))
    angle = float(input("Enter angle of the mortar tube in degrees (0-90): "))
    return ammo_type, fuze_setting, charge_part, angle


def calculate_trajectory(muzzle_velocity, angle, t, cep):
    angle_rad = math.radians(angle)
    x = muzzle_velocity * math.cos(angle_rad) * t
    y = muzzle_velocity * math.sin(angle_rad) * t - 0.5 * G * t ** 2

    # Add error based on CEP (mild perturbations)
    error_radius = np.random.normal(0, cep / 10)
    error_angle = np.random.uniform(0, 2 * np.pi)
    x += error_radius * np.cos(error_angle)
    y += error_radius * np.sin(error_angle)

    # Z-axis represents the CEP
    z = cep

    return x, y, z


def animate(i, x_data, y_data, z_data, line, ax, muzzle_velocity, angle):
    t = i * 0.5  # Incrementing time
    distance = muzzle_velocity * t
    cep = min(15 + distance * 0.03, MAX_CEP)  # Linearly increasing CEP with distance
    x, y, z = calculate_trajectory(muzzle_velocity, angle, t, cep)

    # Stop the animation if the projectile hits the ground
    if y < 0:
        return line,
    x_data.append(x)
    y_data.append(y)
    z_data.append(z)
    line.set_data(x_data, y_data)
    line.set_3d_properties(z_data)

    return line,


if __name__ == '__main__':
    ammo_type, fuze_setting, charge_part, angle = get_input()

    muzzle_velocity = MUZZLE_VELOCITIES[charge_part-1]
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Set fixed axes limits
    ax.set_xlim3d(0, 15000)
    ax.set_ylim3d(0, 10000)
    ax.set_zlim3d(0, 1000)

    x_data, y_data, z_data = [], [], []
    line, = ax.plot([], [], [], 'b-', lw=2)

    ax.set_xlabel("Distance (m)")
    ax.set_ylabel("Height (m)")
    ax.set_zlabel("CEP (m)")

    ani = FuncAnimation(fig, animate, frames=500, fargs=(x_data, y_data, z_data, line, ax, muzzle_velocity, angle),
                        interval=10, blit=False)

    plt.show(block=True)
