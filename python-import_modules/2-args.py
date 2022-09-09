#!/usr/bin/python3
import sys
if __name__ == "__main__":
    if (len(sys.argv) - 1) == 0:
        print("0 arguments.")
    else:
        print('{} {}:'.format(len(sys.argv) - 1,\
            "argument" if len(sys.argv) - 1 == 1 else "arguments"))
    for i in range(1, len(sys.argv)):
        print('{}: {}'.format(i, sys.argv[i]))
