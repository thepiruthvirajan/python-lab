import numpy as np
import matplotlib.pyplot as plt

position = np.array([2.0, 3.0])
velocity = np.array([0.0, 0.0]) 
target = np.array([15.0, 12.0])
pos_list = []


speed = 2.0
forward_vector = np.array([0.0, 1.0])

obstacles = np.array([
    [5, 6],
    [8, 10],
    [12, 7],
    [10, 14]
])

while np.linalg.norm(target - position) > 0.5:
    obstacle_near = 100
    near_obstacle = None
    direction = target - position
    distance = np.linalg.norm(direction)
    normalized_direction = direction / distance
    velocity = normalized_direction * speed
    print(f"Current Position: {position}, Velocity: {velocity}, Distance to Target: {distance}", "Normalized Direction:", normalized_direction)
    pos_list.append(position.copy())

    for obstacle in obstacles:
        if np.linalg.norm(position - obstacle) < obstacle_near:
            near_obstacle = obstacle
            obstacle_near = np.linalg.norm(position - obstacle)
            obstacle_distance = obstacle - position
            obstacle_normalized_dir = obstacle_distance / obstacle_near
            print(f"Near Obstacle: {near_obstacle}, Obstacle Normalized Direction: {obstacle_normalized_dir}")
    obstacle_find_near = np.dot(forward_vector, obstacle_normalized_dir) 
    if obstacle_near < 3 and obstacle_find_near > 0.3:
        where_obstacle = (forward_vector[0] * obstacle_normalized_dir[1]- forward_vector[1] * obstacle_normalized_dir[0])
        if where_obstacle > 0:
            velocity = np.array([-forward_vector[1], forward_vector[0]]) * speed
            position = position + velocity
            pos_list.append(position.copy())
            forward_vector = normalized_direction
        else:  
              velocity = np.array([forward_vector[1], -forward_vector[0]]) * speed
              position = position + velocity
              pos_list.append(position.copy())
              forward_vector = normalized_direction
        print(f"Obstacle Avoidance: New Velocity: {velocity}, New Position: {position}")
    else:
        position = position + velocity
        pos_list.append(position.copy())
        print(f"Moving Towards Target: New Position: {position}")
        forward_vector = normalized_direction

print(f"Final Position: {position}")
pos_array = np.array(pos_list)
plt.plot(pos_array[:, 0], pos_array[:, 1], marker="o", linestyle="-", label="Robot Path")
plt.scatter(target[0], target[1], marker="x", color="red", s=100, label="Target")
plt.scatter(obstacles[:, 0], obstacles[:, 1], marker="s", color="black", s=100, label="Obstacles")
plt.legend()
plt.show()
