import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider

# Function to update the rule and cells when the slider value is changed
def update_rule(val):
    global RULE
    RULE = int(val)
    update_cells()

# Function to update the cells based on the current rule
def update_cells():
    global cells, left_shifted, right_shifted, pattern
    cells = np.zeros((ITERATIONS, CELLS), dtype=np.uint8)
    cells[0, CELLS // 2] = 1  # initialize middle cell to 1
    for i in range(1, ITERATIONS):
        left_shifted = np.roll(cells[i - 1], 1)
        right_shifted = np.roll(cells[i - 1], -1)
        pattern = (left_shifted * 4) + (cells[i - 1] * 2) + right_shifted
        cells[i] = np.bitwise_and(np.right_shift(RULE, pattern), 1)
    im.set_data(cells)
    ax.set_title(f"Cellular Automata with Rule {RULE}")

# Function to update the animation for each frame
def update(num):
    update_cells()
    im.set_data(cells[:num])

# Initial values for rule, number of iterations, and number of cells
RULE = 30
ITERATIONS = 400
CELLS = 500

cells = np.zeros((ITERATIONS, CELLS), dtype=np.uint8)
cells[0, CELLS // 2] = 1  # initialize middle cell to 1

# Create the figure and axis for the plot
fig, ax = plt.subplots()
im = ax.imshow(cells, cmap='binary', interpolation='nearest')
ax.set_title(f"Cellular Automata with Rule {RULE}")
ax.set_xlabel("Cell Position")
ax.set_ylabel("Iteration")

# Add the rule slider to the figure
ax_rule = plt.axes([0.25, 0.1, 0.65, 0.03])
slider_rule = Slider(ax_rule, 'Rule', 0, 255, valinit=RULE, valstep=1)
slider_rule.on_changed(update_rule)

# Create the animation and display the plot
update_cells()
#ani = FuncAnimation(fig, update, frames=range(1, ITERATIONS), repeat=True, interval=10)
plt.show()
