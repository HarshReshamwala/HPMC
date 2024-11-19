import sys
import os

# Assuming the modules are in a folder named "my_modules" one level up
# You can adjust the path as needed.
module_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), 'tile_generator'))
sys.path.append(module_folder)

# Now you can import the modules
from pattern_generator import *
from graphics_tk import *

# Set the scalar for scaling the tiles on the canvas
SCALAR = 30
# Set the target level to render
TARGET_LEVEL = 4  # Change this to your desired level

# Build tiles up to the target level
build_supertiles(TARGET_LEVEL)

# Draw only the target level
draw(TARGET_LEVEL)

# Render the tiles to the screen with specific width, height, and scalar


# draw_tiles(vertices_to_draw, width=1000, height=1000, scalar=SCALAR)

# Save the vertices of the tiles to a text file
with open('shapes_4.txt', 'w') as file:
    file.write("Vertices of the tiles:\n")
    for i, (vertices, fill) in enumerate(vertices_to_draw):
        file.write(f"Tile {i + 1}:\n")
        file.write(f"  Color: {fill}\n")  # Add color to the output
        for vertex in vertices:
            file.write(f"  Vertex: {vertex}\n")