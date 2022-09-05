import arcade
import src.const as C

# Set how many rows and columns we will have
ROW_COUNT = 20
COLUMN_COUNT = 30

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 32 * C.SETTINGS.GLOBAL_SCALE
HEIGHT = 32 * C.SETTINGS.GLOBAL_SCALE

MARGIN = 0


class Grid(arcade.Sprite):
    """
    Grid
    """

    def __init__(self) -> None:
        super().__init__()

        # Create a 2 dimensional array.
        self.grid = []
        for row in range(ROW_COUNT):
            # Add an empty array that will hold each cell
            # in this row
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append({"color": (0, 0, 0, 0)})  # Append a cell
        self.hover_column = 0
        self.hover_row = 0

    def on_draw(self):
        """
        Render the screen.
        """

        # Draw the grid
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):

                # Do the math to figure out where the box is
                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

                # Draw the box
                color = self.grid[row][column]["color"]
                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)

    def on_mouse_press(self, x, y):
        """
        Called when the user presses a mouse button.
        """

        # Change the x/y screen coordinates to grid coordinates
        column = int(x // (WIDTH + MARGIN))
        row = int(y // (HEIGHT + MARGIN))

        print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({row}, {column})")

        # Make sure we are on-grid. It is possible to click in the upper right
        # corner in the margin and go to a grid location that doesn't exist
        if row < ROW_COUNT and column < COLUMN_COUNT:
            self.grid[row][column]["color"] = (0, 0, 0, 255)

    def on_hover(self, x, y):
        """
        Called when the mouse motion is detected
        """

        # Change the x/y screen coordinates to grid coordinates
        column = int(x // (WIDTH + MARGIN))
        row = int(y // (HEIGHT + MARGIN))

        # print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({row}, {column})")

        # Make sure we are on-grid. It is possible to click in the upper right
        # corner in the margin and go to a grid location that doesn't exist
        if row < ROW_COUNT and column < COLUMN_COUNT:

            if self.hover_column != column or self.hover_row != row:
                # remove hover effect from older hover cell
                self.grid[self.hover_row][self.hover_column]["color"] = (0, 0, 0, 0)

                # save new hover cell
                self.hover_column = column
                self.hover_row = row

                # add hover effect to new cell
                self.grid[row][column]["color"] = (255, 0, 0, 64)
        else:
            self.grid[self.hover_row][self.hover_column]["color"] = (0, 0, 0, 0)
