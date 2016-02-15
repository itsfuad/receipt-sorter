#!/usr/bin/env python3
"""Command-line interface for receipt-sorter."""
import argparse
import json
import sys
from receipt_sorter import analyze

def main(argv=None):
    parser = argparse.ArgumentParser(description='Calculate per-merchant spending from exported expense rows')
    parser.add_argument('path', help='Input data file, or - for standard input')
    parser.add_argument('--pretty', action='store_true', help='Indent JSON output')
    args = parser.parse_args(argv)
    if args.path == '-':
        data = sys.stdin.read()
    else:
        with open(args.path, encoding='utf-8') as f:
            data = f.read()
    print(json.dumps(analyze(data), sort_keys=True, indent=2 if args.pretty else None))
    return 0

if __name__ == '__main__':
    sys.exit(main())
