TILES = open('09-input.txt').read().splitlines()

def get_rectangles(tiles):
    rectangles = []
    for i, tile_a in enumerate(tiles):
        for tile_b in tiles[i+1:]:
            if tile_a == tile_b:
                continue
            diff_x = abs(int(tile_a.split(',')[0]) - int(tile_b.split(',')[0]) + 1)
            diff_y = abs(int(tile_a.split(',')[1]) - int(tile_b.split(',')[1]) + 1)
            size = diff_x * diff_y
            rectangles.append((size, (tile_a, tile_b)))
    return rectangles

def main():
    rectangles = get_rectangles(TILES)
    largest_rectangle = max(rectangles, key=lambda x: x[0])
    return largest_rectangle

if __name__ == "__main__":
    print(main())
            