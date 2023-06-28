import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
G = 9.81  # Gravity constant (m/s^2)
MUZZLE_VELOCITIES = [158, 212, 272, 320, 362]  # m/s corresponding to the five-part propelling charge system
AMMO_TYPES = ['high-explosive', 'incendiary', 'chemical']
FUZE_SETTINGS = ['delayed-action', 'contact']

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

def calculate_trajectory(muzzle_velocity, angle, t):
    angle_rad = math.radians(angle)
    x = muzzle_velocity * math.cos(angle_rad) * t
    y = muzzle_velocity * math.sin(angle_rad) * t - 0.5 * G * t**2
    return x, y

def animate(i, x_data, y_data, line, muzzle_velocity, angle):
    t = i * 0.1  # Incrementing time
    x, y = calculate_trajectory(muzzle_velocity, angle, t)
    x_data.append(x)
    y_data.append(y)
    line.set_data(x_data, y_data)
    return line,

if __name__ == '__main__':
    ammo_type, fuze_setting, charge_part, angle = get_input()

    muzzle_velocity = MUZZLE_VELOCITIES[charge_part-1]
    fig, ax = plt.subplots()
    x_data, y_data = [], []
    line, = plt.plot([], [], 'b-', lw=2)

    # Setting x and y axis limits
    ax.set_xlim(0, 10000)
    ax.set_ylim(0, 4000)

    ax.set_xlabel("Distance (m)")
    ax.set_ylabel("Height (m)")
    ax.grid()

    ani = FuncAnimation(fig, animate, frames=300, fargs=(x_data, y_data, line, muzzle_velocity, angle),
                        interval=20, blit=True)

    plt.show()
