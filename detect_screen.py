#!/usr/bin/env python3
import sys

def detect_device(width, height, touch_screen=False):
    ratio = width / height
    if touch_screen:
        if width < 600:
            return "Phone (portrait)"
        elif width < 1024:
            return "Phone landscape or small tablet"
        else:
            return "Tablet"
    else:
        # No touch – likely TV
        return "TV (remote control)"

if __name__ == "__main__":
    if len(sys.argv) > 2:
        w, h = int(sys.argv[1]), int(sys.argv[2])
        touch = input("Has touch screen? (y/n): ").lower() == 'y'
        print(detect_device(w, h, touch))
    else:
        print("Usage: detect_screen.py <width> <height>")
