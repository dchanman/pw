#!/usr/bin/env python
import re
import argparse

def patch(filename, difpath, revert=False):
    code = open(filename, 'rb').read()
    dif = open(difpath, 'r').read()
    
    # Use regex to get the diff info as a 3-tuple
    m = re.findall('([0-9a-fA-F]+): ([0-9a-fA-F]+) ([0-9a-fA-F]+)', dif)
    for offset, old, new in m:
        # Patch the byte
        i = int(offset, 16)
        if revert:
            code = code[:i] + old.decode('hex') + code[i + 1:]
        else:
            code = code[:i] + new.decode('hex') + code[i + 1:]
    
    open(filename, 'wb').write(code)

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('binary', type=str,
                    help='Original binary file')
    parser.add_argument('dif', type=str,
                    help='Patch file')
    parser.add_argument('--revert', action='store_true',
                    help='Revert the patch')
    
    args = parser.parse_args()
    patch(args.binary, args.dif, args.revert)

if __name__ == "__main__":
    main()