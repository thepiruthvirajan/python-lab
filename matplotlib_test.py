import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4]

y1 = [0, 1, 4, 9, 16]
y2 = [0, 2, 4, 6, 8]
y3 = [0, 3, 9, 15, 18]
plt.scatter(x, y1, marker="o", label="Square", color="blue", s=100)
plt.scatter(x, y2, marker="*", label="Linear", color="green", s=10)
plt.scatter(x, y3, marker="^", label="Cubic", color="red", s=50)
#plt.plot(x, y1, marker="o", linestyle="--", label="Square", color="blue")
#plt.plot(x, y2, marker="*", linestyle="-", label="Linear", color="green")
#plt.plot(x, y3, marker="^", linestyle="-.", label="Cubic", color="red")
plt.legend()
plt.show()

subjects = ["Python", "C++", "Math", "ROS2"]
scores = [85, 70, 90, 60]

plt.bar(subjects, scores)

plt.show()

data = [12, 15, 13, 18, 21, 17, 15, 14, 22, 19,
        16, 15, 13, 20, 18, 17, 14, 16, 19, 15]

plt.hist(data, bins=10, color='blue', edgecolor='black')

plt.show()