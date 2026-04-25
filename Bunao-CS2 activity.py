import math

theta_deg = float(input("Enter launch angle (degrees): "))
R = float(input("Enter max horizontal distance (meters): "))
g = 9.81

theta_rad = math.radians(theta_deg)
v0 = math.sqrt(R * g / math.sin(2 * theta_rad))
print(f"Initial velocity: {v0:.2f} m/s")