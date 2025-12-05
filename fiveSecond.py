import fiveFirst

def get_fresh_ids(fresh_ids):
    fresh_id_list = []
    for fresh_id in fresh_ids:
        start = fresh_id[0]
        end = fresh_id[1]
        add_start = True
        add_end = True
        if fresh_id_list:
            for i, id in enumerate(fresh_id_list):
                if id[1] == 0:
                    if id[0] <= start <= fresh_id_list[i + 1][0]:
                        add_start = False
                        continue
                    elif start <= id[0] <= end:
                        add_start = False
                        fresh_id_list[i] = (start, 0)
                if id[1] == 1:
                    if id[0] >= end >= fresh_id_list[i - 1][0]:
                        add_end = False
                        continue
                    elif start <= id[0] <= end:
                        add_end = False
                        fresh_id_list[i] = (end, 1)
        if add_start:
            fresh_id_list.append((start, 0))
        if add_end:
            fresh_id_list.append((end, 1))
    
    return fresh_id_list

def main():
    counter = 0
    for id in get_fresh_ids(fiveFirst.FRESH_IDS):
        print(id)
        if id[1] == 0:
            counter -= id[0] - 1
        else:
            counter += id[0]
    
    return counter

if __name__ == "__main__":
    print(main())