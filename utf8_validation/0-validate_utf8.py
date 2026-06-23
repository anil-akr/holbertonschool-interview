#!/usr/bin/python3
"""Module providing a UTF-8 encoding validation function"""


def validUTF8(data):
    """Determine if a given data set represents a valid UTF-8 encoding.

    A character in UTF-8 can be 1 to 4 bytes long. Each integer in the
    list represents 1 byte of data; only the 8 least significant bits
    of each integer are considered.

    Args:
        data (list of int): list of integers, each representing 1 byte.

    Returns:
        bool: True if data is a valid UTF-8 encoding, False otherwise.
    """
    n_bytes = 0

    for num in data:
        byte = num & 0xFF

        if n_bytes == 0:
            if byte >> 7 == 0b0:
                n_bytes = 0
            elif byte >> 5 == 0b110:
                n_bytes = 1
            elif byte >> 4 == 0b1110:
                n_bytes = 2
            elif byte >> 3 == 0b11110:
                n_bytes = 3
            else:
                return False

        else:
            if byte >> 6 != 0b10:
                return False
            n_bytes = n_bytes - 1

    return n_bytes == 0
