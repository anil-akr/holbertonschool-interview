#!/usr/bin/python3
"""Log parsing script that reads stdin and computes metrics"""
import sys


def print_stats(total_size, status_counts):
    """Print accumulated statistics"""
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))


valid_codes = [200, 301, 400, 401, 403, 404, 405, 500]

total_size = 0
line_count = 0
status_counts = {code: 0 for code in valid_codes}

try:
    for line in sys.stdin:
        parts = line.split()

        if len(parts) < 7:
            continue

        try:
            status = int(parts[-2])
            file_size = int(parts[-1])
        except ValueError:
            continue

        if status in status_counts:
            status_counts[status] += 1

        total_size += file_size
        line_count += 1

        # Affiche toutes les 10 lignes
        if line_count % 10 == 0:
            print_stats(total_size, status_counts)

except KeyboardInterrupt:
    print_stats(total_size, status_counts)
    raise
