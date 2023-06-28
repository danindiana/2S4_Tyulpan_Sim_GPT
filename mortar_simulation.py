import math
import matplotlib.pyplot as plt

# Constants
G = 9.81  # Gravity constant (m/s^2)

# Parameters for 53-F-864
WEIGHT = 130  # kg
MUZZLE_VELOCITIES = [158, 212, 272, 320, 362]  # m/s corresponding to the five-part propelling charge system
MAX_RANGE = 9650  # m

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

def calculate_trajectory(ammo_type, fuze_setting, charge_part, angle):
    muzzle_velocity = MUZZLE_VELOCITIES[charge_part-1]
    angle_rad = math.radians(angle)
    
    # Using kinematic equations to calculate time of flight and distance
    time_of_flight = 2 * muzzle_velocity * math.sin(angle_rad) / G
    times = [t/100 for t in range(int(time_of_flight * 100) + 1)]  # step size of 0.01s for smoother curve
    x_coords = [muzzle_velocity * math.cos(angle_rad) * t for t in times]
    y_coords = [muzzle_velocity * math.sin(angle_rad) * t - 0.5 * G * t**2 for t in times]
    
    return x_coords, y_coords

def plot_trajectory(x_coords, y_coords):
    plt.figure()
    plt.plot(x_coords, y_coords)
    plt.title("Mortar Shell Trajectory")
    plt.xlabel("Distance (m)")
    plt.ylabel("Height (m)")
    plt.grid()
    plt.show()

if __name__ == '__main__':
    ammo_type, fuze_setting, charge_part, angle = get_input()
    if 1 <= charge_part <= 5:
        print("Firing mortar...")
        x_coords, y_coords = calculate_trajectory(ammo_type, fuze_setting, charge_part, angle)
        print("Plotting ballistic trajectory...")
        plot_trajectory(x_coords, y_coords)
    else:
        print("Invalid charge part. It must be between 1 and 5.")
