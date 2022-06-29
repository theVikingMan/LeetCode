def maximumUnits(boxTypes, truckSize):
    total_units = 0
    boxTypes.sort(key=lambda x: x[1], reverse=True)

    for num_boxes, num_units in boxTypes:
        if truckSize <= num_boxes:
            total_units += truckSize * num_units
            break
        total_units += num_boxes * num_units
        truckSize -= num_boxes
    return total_units


print(maximumUnits([[5, 10], [2, 5], [4, 7], [3, 9]], 10))
