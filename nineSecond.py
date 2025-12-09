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

def get_outline(tiles):
    outline = set()
    for i, tile in enumerate(tiles):
        x, y = map(int, tile.split(','))
        outline.add((x, y))
        x2, y2 = map(int, tiles[i-1].split(','))
        if x == x2:
            for yy in range(min(y, y2), max(y, y2)+1):
                outline.add((x, yy))
        elif y == y2:
            for xx in range(min(x, x2), max(x, x2)+1):
                outline.add((xx, y))
    return outline

def main():
    rectangles = sorted(get_rectangles(TILES), key=lambda x: x[0], reverse=True)
    outline = get_outline(TILES)
    for rect in rectangles:
        is_valid = True
        tile_a = tuple(map(int, rect[1][0].split(',')))
        tile_b = tuple(map(int, rect[1][1].split(',')))
        is_valid = True
        for tile in outline:
            # Edge cases will not be relevant here (two outlines touching)
            if tile_a[0] < tile[0] < tile_b[0] or tile_a[0] > tile[0] > tile_b[0]:
                if tile_a[1] < tile[1] < tile_b[1] or tile_a[1] > tile[1] > tile_b[1]:
                    is_valid = False
                    break
        if is_valid:
            return rect

if __name__ == "__main__":
    print(main())