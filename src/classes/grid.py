import arcade
import src.const as C


class Grid(arcade.Sprite):
    """
    Grid
    """

    def __init__(self, rows_count: int, columns_count: int) -> None:
        super().__init__()

        self.rows_count = rows_count
        self.columns_count = columns_count

        # Create a 2 dimensional array.
        self.grid = []
        for row in range(self.rows_count):
            # Add an empty array that will hold each cell
            # in this row
            self.grid.append([])
            for column in range(self.columns_count):
                self.grid[row].append(
                    {"color": (0, 0, 0, 0), "tower": None}
                )  # Append a cell
        self.hover_column = 0
        self.hover_row = 0

    def set_size(self, rows: int, columns: int):
        self.rows_count = rows
        self.columns_count = columns

    def on_draw(self):
        """
        Render the screen.
        """

        # Draw the grid
        for row in range(self.rows_count):
            for column in range(self.columns_count):

                # Draw the tower
                if self.grid[row][column]["tower"]:
                    self.grid[row][column]["tower"].draw()

                color = self.grid[row][column]["color"]

                for i in range(2):
                    for j in range(2):

                        # Do the math to figure out where the box is
                        x = (
                            (C.GRID.MARGIN + C.GRID.WIDTH) * (column + i)
                            + C.GRID.MARGIN
                            + C.GRID.WIDTH // 2
                        )
                        y = (
                            (C.GRID.MARGIN + C.GRID.HEIGHT) * (row + j)
                            + C.GRID.MARGIN
                            + C.GRID.HEIGHT // 2
                        )

                        # Draw the box

                        arcade.draw_rectangle_filled(
                            x, y, C.GRID.WIDTH, C.GRID.HEIGHT, color
                        )

    def get_cell(self, x, y):
        """
        Called when the user presses a mouse button.
        """

        # Change the x/y screen coordinates to grid coordinates
        column = int(x // (C.GRID.WIDTH + C.GRID.MARGIN))
        row = int(y // (C.GRID.HEIGHT + C.GRID.MARGIN))

        print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({row}, {column})")

        # Make sure we are on-grid. It is possible to click in the upper right
        # corner in the margin and go to a grid location that doesn't exist
        if row < self.rows_count and column < self.columns_count:
            return [row, column]
        return [-1, -1]

    def on_hover(self, x, y):
        """
        Called when the mouse motion is detected
        """

        # Change the x/y screen coordinates to grid coordinates
        column = int(x // (C.GRID.WIDTH + C.GRID.MARGIN))
        row = int(y // (C.GRID.HEIGHT + C.GRID.MARGIN))

        # print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({row}, {column})")

        # Make sure we are on-grid. It is possible to click in the upper right
        # corner in the margin and go to a grid location that doesn't exist
        if row < self.rows_count and column < self.columns_count:

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
