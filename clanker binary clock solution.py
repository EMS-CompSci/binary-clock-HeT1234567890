# -*- coding: utf-8 -*-
"""
Created on Tue Nov  4 10:12:41 2025

@author: henrytodd1
"""

# ...existing code...
#!/usr/bin/env python3
import time
from datetime import datetime
import sys

ON = "⬛"
OFF = "⬜"

def clear():
    sys.stdout.write("\x1b[2J\x1b[H")

def bits(value, width):
    return format(value, f'0{width}b')

def draw():
    now = datetime.now()
    h, m, s = now.hour, now.minute, now.second

    # Use 6 rows to accommodate seconds/minutes (0-59 -> 6 bits).
    bh = bits(h, 6)  # hours 0-23 fits in 5 bits; pad to 6 for alignment
    bm = bits(m, 6)
    bs = bits(s, 6)

    clear()
    print("Binary Clock (HH:MM:SS)   " + now.strftime("%H:%M:%S"))
    print()
    # Print MSB at top
    for i in range(6):
        cols = [
            ON if bh[i] == "1" else OFF,
            ON if bm[i] == "1" else OFF,
            ON if bs[i] == "1" else OFF,
        ]
        print("  ".join(cols))
    print()
    print(" H   M   S")

def main():
    try:
        while True:
            draw()
            # sleep until the start of the next second
            time.sleep(1 - (time.time() % 1))
    except KeyboardInterrupt:
        print()
        sys.exit(0)

if __name__ == "__main__":
    main()
# ...existing code...