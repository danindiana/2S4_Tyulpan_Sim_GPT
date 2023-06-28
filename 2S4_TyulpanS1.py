import math
import matplotlib.pyplot as plt

# Constants
G = 9.81  # Gravity constant (m/s^2)
AMMUNITION_TYPES = {
    'high-explosive': {'range_factor': 1},
    'incendiary': {'range_factor': 0.9},
    'chemical': {'range_factor': 0.8},
}

def get_input():
    ammo_type = input("Enter type of munition (high-explosive, incendiary, chemical): ")
    charge = float(input("Enter propellant charge in percentage (0-100): "))
    angle = float(input("Enter angle of the mortar tube in degrees (0-90): "))
    return ammo_type, charge, angle

def calculate_trajectory(ammo_type, charge, angle):
    range_factor = AMMUNITION_TYPES[ammo_type]['range_factor']
    angle_rad = math.radians(angle)
    max_range = 20000 * (charge / 100) * range_factor  # Assuming 20km max range for 100% charge and high-explosive
    
    # Using kinematic equations to calculate time of flight and distance
    time_of_flight = 2 * max_range * math.sin(angle_rad) / G
    times = [t for t in range(int(time_of_flight) + 1)]
    x_coords = [max_range * math.cos(angle_rad) * t for t in times]
    y_coords = [max_range * math.sin(angle_rad) * t - 0.5 * G * t**2 for t in times]
    
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
    ammo_type, charge, angle = get_input()
    x_coords, y_coords = calculate_trajectory(ammo_type, charge, angle)
    plot_trajectory(x_coords, y_coords)
