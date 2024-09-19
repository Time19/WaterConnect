import os
from PIL import Image, ImageTk
import tkinter as tk


def load_images():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_dir = os.path.join(script_dir, 'images')

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
        (0, 1, 0, 1, 0): 'pipe00',
        (0, 0, 1, 0, 1): 'pipe10',
        (0, 0, 1, 1, 1): 'pipe01',
        (0, 1, 0, 1, 1): 'pipe11',
        (0, 1, 1, 0, 1): 'pipe21',
        (0, 1, 1, 1, 0): 'pipe31',
        (0, 0, 0, 1, 1): 'pipe02',
        (0, 1, 0, 0, 1): 'pipe12',
        (0, 1, 1, 0, 0): 'pipe22',
        (0, 0, 1, 1, 0): 'pipe32',
        (1, 0, 0, 1, 0): 'pipe03',
        (1, 0, 0, 0, 1): 'pipe13',
        (1, 1, 0, 0, 0): 'pipe23',
        (1, 0, 1, 0, 0): 'pipe33',
        (2, 0, 0, 1, 0): 'pipe04',
        (2, 0, 0, 0, 1): 'pipe14',
        (2, 1, 0, 0, 0): 'pipe24',
        (2, 0, 1, 0, 0): 'pipe34'
    }
    return symbols.get(title, ' ')


#Playfield hehe
class Playfield:
    def __init__(self, rows, cols):
        self.playfield = [[(2, 0, 0, 1, 0), (0, 0, 1, 1, 0), (0, 0, 1, 1, 0)],
                     [(1, 0, 0, 1, 0), (0, 1, 1, 0, 1), (0, 1, 0, 0, 1)],
                     [(0, 1, 0, 1, 0), (0, 1, 1, 0, 0), (2, 1, 0, 0, 0)]]

        self.rows = rows
        self.cols = cols

        def getplayfield(self):
            return self.playfield

        def __str__(self):
            return str(self.playfield) + "\nrows: " + str(self.rows) + "\ncols: " + str(self.cols)


def create_playfield(rows, cols):
    # static version
    playfield = [[(2, 0, 0, 1, 0), (0, 0, 1, 1, 0), (0, 0, 1, 1, 0)],
                 [(1, 0, 0, 1, 0), (0, 1, 1, 0, 1), (0, 1, 0, 0, 1)],
                 [(0, 1, 0, 1, 0), (0, 1, 1, 0, 0), (2, 1, 0, 0, 0)]]

    # dynamic version not implemented yet, only vertical pipes lol
    """playfield = []
    for _ in range(rows):
        row = []
        for _ in range(cols):
            row.append((0, 1, 0, 1, 0))  # default is a vertical pipe
        playfield.append(row)"""

    # modify_playfield(playfield, 0, 0, (1, 1, 0, 0, 0))
    return playfield


def modify_playfield(playfield, row, col, tile):
    new_type, new_north, new_east, new_south, new_west = tile

    playfield[row][col] = (new_type, new_north, new_east, new_south, new_west)
    return playfield


def rotate_tile(playfield, row, col):
    # rotating the tile 90 degrees clockwise
    types, north, east, south, west = playfield[row][col]
    new_north = west
    new_east = north
    new_south = east
    new_west = south

    playfield[row][col] = (types, new_north, new_east, new_south, new_west)
    print(playfield)


    check_if_connected(playfield, row, col)

    return playfield


def check_if_connected(playfield, row, col):
    tuple1 = playfield[row][col]

    #try checking for north tile
    try:
        if tuple1[1] & (playfield[row - 1][col])[3]:
            print("Connection to North:")
            print(playfield[row - 1][col])
            return(row - 1, col)
    except IndexError:
        pass


    #try checking for east tile
    try:
        if tuple1[2] & (playfield[row][col + 1])[4]:
            print("Connection to East:")
            print(playfield[row][col + 1])
            return(row, col + 1)

    except IndexError:
        pass

    #try checking for south tile
    try:
        if tuple1[3] & (playfield[row + 1][col])[1]:
            print("Connection to South")
            print(playfield[row + 1][col])
            return(row + 1, col)

    except IndexError:
        pass

    # try checking for west tile
    try:
        if tuple1[4] & (playfield[row][col - 1])[2]:
            print("Connection to West:")
            print(playfield[row][col - 1])
            return(row, col - 1)

    except IndexError:
        pass

def display_playfield(playfield, images, canvas, image_refs):
    canvas.delete("all")  # Clear existing images
    tile_size = 200

    for row_idx, row in enumerate(playfield):
        for col_idx, tile in enumerate(row):
            symbol = get_tile_symbol(tile)
            if symbol in images:
                img = ImageTk.PhotoImage(images[symbol])
                canvas.create_image(col_idx * tile_size, row_idx * tile_size, anchor=tk.NW, image=img)
                image_refs.append(img)  # Keep a reference to avoid garbage collection


def main():
    root = tk.Tk()

    playfield = create_playfield(4, 4)
    images = load_images()

    tile_size = 200
    canvas_width = len(playfield[0]) * tile_size
    canvas_height = len(playfield) * tile_size

    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
    canvas.pack()

    image_refs = []  # To store image references

    def on_click(event):
        col = event.x // tile_size
        row = event.y // tile_size
        rotate_tile(playfield, row, col)
        display_playfield(playfield, images, canvas, image_refs)

    canvas.bind("<Button-1>", on_click)
    display_playfield(playfield, images, canvas, image_refs)

    root.mainloop()


if __name__ == "__main__":
    main()
