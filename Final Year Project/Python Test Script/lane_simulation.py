from shapely.geometry import Point, LineString

import matplotlib.pyplot as plt
import matplotlib.animation as animation

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from matplotlib.patches import Rectangle, FancyBboxPatch


class Lane:
    def __init__(self, id, start, end):
        self.id = id
        self.line = LineString([start, end])

class Vehicle:
    def __init__(self, position):
        self.position = Point(position)


lanes = [
    Lane(1, (-7.128107, 52.246004), (-7.128207, 52.246104)),
    # Define more lanes as needed...
]

vehicle = Vehicle((-7.128157, 52.246054))  # Starting position


def is_vehicle_in_lane(vehicle, lane):
    return lane.line.buffer(0.0001).contains(vehicle.position)  # Adjust buffer for lane width

for lane in lanes:
    if is_vehicle_in_lane(vehicle, lane):
        print(f"Vehicle is in lane {lane.id}")





# Initialize the plot
fig, ax = plt.subplots(figsize=(8, 4))

# Simplified road layout based on the image provided
road = Rectangle((0, 0.4), 1, 0.2, color="gray")  # Main road
junction = Rectangle((0.8, 0.4), 0.2, 0.6, color="gray")  # Junction

ax.add_patch(road)
ax.add_patch(junction)

# Initial car location
car = plt.Circle((0.1, 0.5), 0.05, color='blue')

ax.add_patch(car)

# Set plot limits
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# Hide axes
ax.axis('off')

# Function to animate the car
def update(frame):
    x, y = car.center
    # Animate car moving to the right
    if x < 0.8:
        car.set_center((x + 0.01, y))
    # Car has reached the junction
    elif y < 0.8:
        car.set_color('red')  # Signal car is not allowed to turn
        if frame > 40:  # Wait for some frames before moving up
            car.set_center((x, y + 0.01))

    return car,

# Run the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=100, blit=True)

plt.show()



