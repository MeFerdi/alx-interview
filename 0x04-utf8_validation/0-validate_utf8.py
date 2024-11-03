#!/usr/bin/python3
"""
UTF-8 Validation Module
"""

def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): A list of integers representing bytes.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    num_bytes = 0

    for byte in data:
        # Get the last 8 bits of the byte
        mask = 0b10000000
        
        # If no bytes expected, determine how many bytes to expect
        if num_bytes == 0:
            # Count leading ones
            while mask & byte:
                num_bytes += 1
                mask >>= 1
            
            # If it's a single-byte character (0xxxxxxx), reset num_bytes to 0
            if num_bytes == 0:
                continue
            
            # If num_bytes is more than 4 or less than 2, it's invalid
            if num_bytes == 1 or num_bytes > 4:
                return False
        
        else:
            # For continuation bytes, check if they start with '10'
            if not (byte & 0b11000000 == 0b10000000):
                return False
        
        # Decrease the number of expected bytes
        num_bytes -= 1

    return num_bytes == 0
