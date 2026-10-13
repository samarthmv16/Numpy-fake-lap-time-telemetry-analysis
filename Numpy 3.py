
import numpy as np

# Simulated lap data
time = np.linspace(0, 90, 500)  # 90-second lap

# Simulate speed in km/h
speed = (
    180
    + 70 * np.sin(2 * np.pi * time / 30)
    + 20 * np.sin(2 * np.pi * time / 12)
)

# Forces speed between 70 to 330
speed = np.clip(speed, 70, 330)

# Convert km/h to m/s
speed_ms = speed / 3.6

# TODO 1: Calculate acceleration using np.diff()
# Remember: acceleration = change in velocity / change in time
acceleration = np.diff(speed_ms) / np.diff(time)

max_acc = np.max(acceleration)
min_acc = np.min(acceleration)

# TODO 2: Find maximum, minimum and average speed
max_s = np.max(speed)
min_s = np.min(speed)
avg_s = np.mean(speed)

# TODO 3: Find every point where speed is below 120 km/h
below120 = speed[speed < 120]

# TODO 4: Calculate the percentage of the lap spent below 120 km/h
time_below120 = time[speed < 120]
percentage_oftime_below120 = np.mean(speed < 120) * 100

# TODO 5: Find the time at which maximum speed occurs
speed_max_time = time[np.argmax(speed)]

print(f"Maximum speed in km/h = {max_s:.2f}")
print(f"Minimum speed in km/h = {min_s:.2f}")
print(f"Average speed in km/h = {avg_s:.2f}")
print(f"Time in which speed is lesser than 120 km/h = {np.round(below120, 2)}")
print(f"Percentage of lap time below 120 km/h = {percentage_oftime_below120:.2f} seconds")
print(f"Time in which speed is maxium = {speed_max_time:.2f} seconds with speed = {max_s:.2f} km/h")
print(f"Acceleration in m/s^2 = {acceleration}")