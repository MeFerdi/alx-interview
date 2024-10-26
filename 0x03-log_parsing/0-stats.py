#!/usr/bin/python3
"""
Log parsing script that reads from stdin and computes metrics.
"""

import sys

def print_stats(total_size, status_codes):
    """
    Prints the current statistics.

    Args:
        total_size (int): Total file size.
        status_codes (dict): Dictionary of status codes and their counts.
    """
    print("File size: {}".format(total_size))
    for status in sorted(status_codes.keys()):
        if status_codes[status] > 0:
            print("{}: {}".format(status, status_codes[status]))

def main():
    total_size = 0
    status_codes = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
    }
    
    line_count = 0

    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) < 7:
                continue
            
            ip_address = parts[0]
            date = parts[2][1:] + " " + parts[3][:-1]  # Extract date and time
            request = parts[4] + " " + parts[5] + " " + parts[6]
            status_code = int(parts[7])
            file_size = int(parts[8])

            if status_code in status_codes:
                total_size += file_size
                status_codes[status_code] += 1

            line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        sys.exit(0)

    print_stats(total_size, status_codes)

if __name__ == "__main__":
    main()