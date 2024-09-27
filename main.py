import os

from PIL import Image, ImageTk
import tkinter as tk


def load_images():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_dir = os.path.join(script_dir, 'images/100x100')

    images = {
        "pipe00": Image.open(os.path.join(image_dir, 'pipe00.png')),
        "pipe10": Image.open(os.path.join(image_dir, 'pipe10.png')),
        "pipe01": Image.open(os.path.join(image_dir, 'pipe01.png')),
        "pipe11": Image.open(os.path.join(image_dir, 'pipe11.png')),
        "pipe21": Image.open(os.path.join(image_dir, 'pipe21.png')),
        "pipe31": Image.open(os.path.join(image_dir, 'pipe31.png')),
        "pipe02": Image.open(os.path.join(image_dir, 'pipe02.png')),
        "pipe12": Image.open(os.path.join(image_dir, 'pipe12.png')),
        "pipe22": Image.open(os.path.join(image_dir, 'pipe22.png')),
        "pipe32": Image.open(os.path.join(image_dir, 'pipe32.png')),
        "pipe03": Image.open(os.path.join(image_dir, 'pipe03.png')),
        "pipe13": Image.open(os.path.join(image_dir, 'pipe13.png')),
        "pipe23": Image.open(os.path.join(image_dir, 'pipe23.png')),
        "pipe33": Image.open(os.path.join(image_dir, 'pipe33.png')),
        "pipe04": Image.open(os.path.join(image_dir, 'pipe04.png')),
        "pipe14": Image.open(os.path.join(image_dir, 'pipe14.png')),
        "pipe24": Image.open(os.path.join(image_dir, 'pipe24.png')),
        "pipe34": Image.open(os.path.join(image_dir, 'pipe34.png'))
    }
    return images


def get_tile_symbol(title):
    symbols = {
        (1, 0, 1, 0, 0): 'pipe00',
        (0, 1, 0, 1, 0): 'pipe10',
        (0, 1, 1, 1, 0): 'pipe01',
        (1, 0, 1, 1, 0): 'pipe11',
        (1, 1, 0, 1, 0): 'pipe21',
        (1, 1, 1, 0, 0): 'pipe31',
        (0, 0, 1, 1, 0): 'pipe02',
        (1, 0, 0, 1, 0): 'pipe12',
        (1, 1, 0, 0, 0): 'pipe22',
        (0, 1, 1, 0, 0): 'pipe32',
        (0, 0, 1, 0, 1): 'pipe03',
        (0, 0, 0, 1, 1): 'pipe13',
        (1, 0, 0, 0, 1): 'pipe23',
        (0, 1, 0, 0, 1): 'pipe33',
        (0, 0, 1, 0, 2): 'pipe04',
        (0, 0, 0, 1, 2): 'pipe14',
        (1, 0, 0, 0, 2): 'pipe24',
        (0, 1, 0, 0, 2): 'pipe34'
    }
    return symbols.get(title, ' ')


# Playfield hehe
class Playfield:
    def __init__(self, rows, cols):
        self.playfield = [[(0, 1, 0, 0, 2), (0, 0, 1, 1, 0), (0, 1, 1, 0, 0)],
                          [(1, 0, 0, 0, 1), (0, 1, 1, 0, 0), (0, 0, 1, 1, 0)],
                          [(1, 0, 1, 0, 0), (0, 1, 1, 0, 0), (1, 0, 0, 0, 2)]]

        self.rows = rows
        self.cols = cols

        self.well = (1, 0)
        self.bushes = {(0, 0), (2, 2)}
        self.tree = Tree(self, self.well)

    def __getitem__(self, index):
        r, c, e = index
        return self.playfield[r][c][e]

    def _find_bush_positions(self):
        bush_positions = set()
        for r in range(self.rows):
            for c in range(self.cols):
                if self.playfield[r][c][0] == 2:  # '2' indicates a bush
                    bush_positions.add((r, c))
        return bush_positions

    # rotating one tile
    def rotateTile(self, row, col):
        north, east, south, west, types = self.playfield[row][col]
        new_north = west
        new_east = north
        new_south = east
        new_west = south
        self.playfield[row][col] = new_north, new_east, new_south, new_west, types
        # Calling checkIfConnected to look for adjacent tiles
        self.tree.update()

    # tile must be in format (x,y,y,y,y)
    def modifyPlayfield(self, row, col, tile):
        self.playfield[row][col] = tile

    # checking each side of tile if connected.
    def checkIfConnected(self, row, col, direction):
        tuple1 = self.playfield[row][col]
        print("-------")

        # try checking for north tile
        if direction == 0:
            try:
                if tuple1[1] & (self.playfield[row - 1][col])[3]:
                    print("Connection to North:")
                    print(self.playfield[row - 1][col])
                    return True
            except IndexError:
                pass

        # try checking for east tile
        elif direction == 1:
            try:
                if tuple1[2] & (self.playfield[row][col + 1])[4]:
                    print("Connection to East:")
                    print(self.playfield[row][col + 1])
                    return True
            except IndexError:
                pass

        # try checking for south tile
        elif direction == 2:
            try:
                if tuple1[3] & (self.playfield[row + 1][col])[1]:
                    print("Connection to South")
                    print(self.playfield[row + 1][col])
                    return True
            except IndexError:
                pass

        # try checking for west tile
        elif direction == 3:
            try:
                if tuple1[4] & (self.playfield[row][col - 1])[2]:
                    print("Connection to West:")
                    print(self.playfield[row][col - 1])
                    return True
            except IndexError:
                pass

        # if no adjacent pipe connection:
        else:
            return False

    # Displaying playfield on screen
    def displayPlayfield(self, images, canvas, image_refs):
        canvas.delete("all")  # Clear existing images

        for row_idx, row in enumerate(self.playfield):
            for col_idx, tile in enumerate(row):
                symbol = get_tile_symbol(tile)
                if symbol in images:
                    img = ImageTk.PhotoImage(images[symbol])
                    canvas.create_image(col_idx * PHOTO_SIZE, row_idx * PHOTO_SIZE, anchor=tk.NW, image=img)
                    image_refs.append(img)  # Keep a reference to avoid garbage collection


class Tree:
    def __init__(self, playfield, position):
        self.position = position

        self.north = None
        self.east = None
        self.south = None
        self.west = None

        self.playfield = playfield

    def update(self, visited=None, connected_bushes=None):

        # if set's don't exist --> create them
        if visited is None:
            visited = set()

        if connected_bushes is None:
            connected_bushes = set()

        # adding to set to maintain recursion end
        visited.add(self.position)

        if self.playfield[self.position[0], self.position[1], 4] == 2:
            connected_bushes.add(self.position)

        if connected_bushes == self.playfield.bushes:
            print("Congrats, you have won the game :)")

        for direction, (dr, dc), attr in zip(
                range(4),
                [(-1, 0), (0, 1), (1, 0), (0, -1)],
                ["north", "east", "south", "west"]):

            # setting new position
            newPosition = (self.position[0] + dr, self.position[1] + dc)

            # check for each direction
            if (0 <= newPosition[0] < self.playfield.rows and
                    0 <= newPosition[1] < self.playfield.cols and
                    newPosition not in visited and
                    self.playfield.checkIfConnected(self.position[0], self.position[1], direction)):
                # create subtree
                subtree = Tree(self.playfield, newPosition)
                setattr(self, attr, subtree)
                subtree.update(visited, connected_bushes)



def main():
    root = tk.Tk()

    pf = Playfield(PLAYFIELD_SIZE, PLAYFIELD_SIZE)
    images = load_images()


    canvas_width = len(pf.playfield[0]) * PHOTO_SIZE
    canvas_height = len(pf.playfield) * PHOTO_SIZE

    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
    canvas.pack()

    image_refs = []  # To store image references

    def on_click(event):
        print("#####################")
        col = event.x // PHOTO_SIZE
        row = event.y // PHOTO_SIZE

        pf.rotateTile(row, col)
        pf.displayPlayfield(images, canvas, image_refs)

    canvas.bind("<Button-1>", on_click)
    pf.displayPlayfield(images, canvas, image_refs)

    root.mainloop()

PHOTO_SIZE = 100
PLAYFIELD_SIZE = 3

if __name__ == "__main__":
    main()

