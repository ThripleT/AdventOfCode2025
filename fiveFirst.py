DATABASE = open('05-input.txt').read().splitlines()
FRESH_IDS = []
INGREDIENTS = []
helper = True
for entry in DATABASE:
    if not entry:
        helper = False
        continue
    if helper:
        FRESH_IDS.append((int(entry.split('-')[0]), int(entry.split('-')[1])))
    else:
        INGREDIENTS.append(int(entry))
FRESH_IDS.sort()


def is_fresh(fresh_ids, ingredient):
    for fresh_id in fresh_ids:
        if fresh_id[0] <= ingredient <= fresh_id[1]:
            return True
    return False

def main():
    counter = 0
    for ingredient in INGREDIENTS:
        if is_fresh(FRESH_IDS, ingredient):
            counter += 1
    return counter

if __name__ == "__main__":
    print(main())
