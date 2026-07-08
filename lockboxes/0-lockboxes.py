#!/usr/bin/python3
"""Determines whether all the boxes can be opened."""


def canUnlockAll(boxes):
    """
    Determine if all the boxes can be opened.

    Args:
        boxes (list of list): boxes[i] holds the keys found inside box i.

    Returns:
        bool: True if all the boxes can be opened, otherwise False.
    """
    number_of_boxes = len(boxes)

    opened_boxes = {0}

    boxes_to_explore = [0]

    while boxes_to_explore:
        current_box = boxes_to_explore.pop()

        for key in boxes[current_box]:
            if 0 <= key < number_of_boxes and key not in opened_boxes:
                opened_boxes.add(key)
                boxes_to_explore.append(key)

    return len(opened_boxes) == number_of_boxes
