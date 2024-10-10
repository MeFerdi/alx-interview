#!/usr/bin/python3
"""
Module for unlocking boxes.

This module contains a function named `canUnlockAll` that determines
if all the boxes can be opened given a list of locked boxes and their
keys.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.

    Args:
        boxes (list of lists): A list where each box contains a list of keys
                                to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    unlocked = [False] * len(boxes)  # Track unlocked boxes
    unlocked[0] = True  # The first box is unlocked
    keys = boxes[0]  # Start with keys from the first box

    # Use a simple approach to track unlocked boxes
    for i in range(len(boxes)):
        for key in keys:
            if key < len(boxes) and not unlocked[key]:
                unlocked[key] = True  # Unlock the box
                keys.extend(boxes[key])  # Add newly found keys

    return all(unlocked)