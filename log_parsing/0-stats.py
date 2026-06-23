#!/usr/bin/python3
"""Log parsing script that reads stdin and computes metrics"""
import sys
import re


def print_stats(total_size, status_counts):
    """Print accumulated statistics"""
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))


if __name__ == "__main__":
    pattern = re.compile(
        r'^\d+\.\d+\.\d+\.\d+ - \[.+\] "GET /projects/260 HTTP/1\.1" \d+ \d+$'
    )

    valid_codes = [200, 301, 400, 401, 403, 404, 405, 500]

    total_size = 0
    line_count = 0
    status_counts = {code: 0 for code in valid_codes}

    try:
        for line in sys.stdin:
            line = line.strip()

            if not pattern.match(line):
                continue

            parts = line.split()

            try:
                status = int(parts[-2])
                file_size = int(parts[-1])
            except ValueError:
                continue

            if status in status_counts:
                status_counts[status] += 1

            total_size += file_size
            line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        raise
