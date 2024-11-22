import numpy as np
import tkinter as tk

# Define grid size and parameters
nx, ny = 10, 10  # number of grid points in x and y
dx, dy = 100, 100  # grid cell size (pixels)

# Create a Tkinter window
root = tk.Tk()
root.title("Wind Arrow Display")

# Function to draw arrows at each grid point
def draw_arrows():
    canvas.delete("all")  # Clear the canvas

    for i in range(nx):
        for j in range(ny):
            arrow_x = i * dx + 50  # Center of the cell
            arrow_y = j * dy + 50

            # Calculate the wind vector at this point
            wind_u = np.random.uniform(-1, 1)  # Random x-component
            wind_v = np.random.uniform(-1, 1)  # Random y-component

            # Draw an arrow at this point
            canvas.create_line(arrow_x, arrow_y,
                                arrow_x + wind_u * 50,
                                arrow_y + wind_v * 50,
                                fill='blue', arrow=tk.LAST)

    root.after(1000, draw_arrows)  # Update every second

# Create a Tkinter canvas to draw on
canvas = tk.Canvas(root, width=nx*dx+100, height=ny*dy+100)
canvas.pack()

draw_arrows()  # Start drawing arrows

root.mainloop()
