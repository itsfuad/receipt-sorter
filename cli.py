#!/usr/bin/env python3
"""Command-line interface for receipt-sorter."""
import argparse
import json
import sys
from receipt_sorter import analyze

def main(argv=None):
    parser = argparse.ArgumentParser(description='Calculate per-merchant spending from exported expense rows')
    parser.add_argument('path', help='Input data file, or - for standard input')
    parser.add_argument('--pick', metavar='KEY', help='Print one top-level result field')
    parser.add_argument('--pretty', action='store_true', help='Indent JSON output')
    args = parser.parse_args(argv)
    if args.path == '-':
        data = sys.stdin.read()
    else:
        with open(args.path, encoding='utf-8') as f:
            data = f.read()
    output = analyze(data)
    if args.pick:
        if args.pick not in output: parser.error('Unknown output field: ' + args.pick)
        output = output[args.pick]
    print(json.dumps(output, sort_keys=True, indent=2 if args.pretty else None))
    return 0

if __name__ == '__main__':
    sys.exit(main())
