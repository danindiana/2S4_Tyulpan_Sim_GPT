import math
import matplotlib.pyplot as plt

# Constants
G = 9.81  # Gravity constant (m/s^2)
E_PROP = 4500000  # Energy per unit mass of propellant in J/kg (Assumed value)

def calculate_muzzle_velocity(range, angle_deg):
    angle_rad = math.radians(angle_deg)
    # rearranging the range equation to solve for muzzle velocity
    return math.sqrt((range * G) / (math.sin(2 * angle_rad)))

def calculate_required_energy(mass, velocity):
    return 0.5 * mass * velocity ** 2

def estimate_propellant_charge(energy):
    return energy / E_PROP

def main():
    # Given
    projectile_mass = 134  # kg
    desired_range = 9000  # m (9 kilometers)
    launch_angle = 45  # degrees (maximum range for a given velocity is achieved at 45 degrees)
    
    # Calculations
    muzzle_velocity = calculate_muzzle_velocity(desired_range, launch_angle)
    required_energy = calculate_required_energy(projectile_mass, muzzle_velocity)
    propellant_charge = estimate_propellant_charge(required_energy)
    
    # Output
    print(f"Muzzle Velocity Required: {muzzle_velocity:.2f} m/s")
    print(f"Required Energy: {required_energy:.2f} Joules")
    print(f"Estimated Propellant Charge: {propellant_charge:.2f} kg")

if __name__ == '__main__':
    main()
