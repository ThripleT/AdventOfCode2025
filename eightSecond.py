import math
import time

BOXES = open('08-input.txt').read().splitlines()

def get_closes_box(boxes):
    timer = time.time()
    closes_boxes = []
    for i, box in enumerate(boxes):
        for box2 in boxes[i+1:]:
            if box == box2:
                continue
            coor_1 = box.split(',')
            coor_2 = box2.split(',')
            distance = math.sqrt(math.pow(int(coor_1[0]) - int(coor_2[0]), 2)
                                + math.pow(int(coor_1[1]) - int(coor_2[1]), 2)
                                + math.pow(int(coor_1[2]) - int(coor_2[2]), 2))
            closes_boxes.append((box, box2, distance))
    closes_boxes = sorted(closes_boxes, key=lambda x: x[2])
    print("Time to find closes boxes:", time.time() - timer)
    print(len(closes_boxes), "closes boxes found")
    return closes_boxes

def make_circuits(connections=-1):
    timer = time.time()
    boxes_with_closes = get_closes_box(BOXES)
    circuits = []
    last_connection = None
    for box_info in boxes_with_closes[:connections]:
        finding = True
        for circuit in circuits:
            if box_info[0] in circuit and box_info[1] in circuit:
                finding = False
                break
            elif box_info[0] in circuit or box_info[1] in circuit:
                input("Unexpected case!")
        if not finding:
            continue
        new_circuit = [box_info[0], box_info[1]]
        one_circuit = False
        while finding:
            if len(new_circuit) >= len(BOXES):
                one_circuit = True
                break
            finding = False
            for box_info2 in boxes_with_closes[:connections]:
                if box_info2[0] in new_circuit or box_info2[1] in new_circuit:
                    if box_info2[0] not in new_circuit:
                        finding = True
                        new_circuit.append(box_info2[0])
                    if box_info2[1] not in new_circuit:
                        finding = True
                        new_circuit.append(box_info2[1])
                    if finding:
                        last_connection = box_info2
                        break
        circuits.append(new_circuit.copy())
        if one_circuit:
            break
    
    print("Time to make circuits:", time.time() - timer)
    print(len(circuits), "circuits found")
    return sorted(circuits, key=lambda x: len(x), reverse=True), last_connection

def main():
    timer = time.time()
    circuits, last_connection = make_circuits()
    multiplier = 1
    for box in last_connection[:2]:
        multiplier *= int(box.split(',')[0])
    return multiplier

if __name__ == "__main__":
    print(main())