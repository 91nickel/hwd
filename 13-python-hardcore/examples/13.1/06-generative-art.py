import matplotlib.pyplot as plt
import random

fig, ax = plt.subplots(figsize=(6, 6))
for _ in range(20):
    x, y = random.random(), random.random()
    w, h = random.random() / 3, random.random() / 3
    color = random.choice(["red", "blue", "yellow", "white", "black"])
    ax.add_patch(plt.Rectangle((x, y), w, h, facecolor=color, edgecolor="black", linewidth=2))

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")
plt.show()
