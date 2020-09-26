#!/usr/bin/env python3
"""
Solves Schrödinger equation for a one dimensional time independent potential.
"""
import sys
import os.path
import argparse
import SOSE.reading as reading
import SOSE.diagonalizer as diag
import SOSE.uncertainty as uncertainty
import SOSE.writing as writing

_DESCRIPTION = '''ygiheñ'''

_INPUT_FILE = 'schrodinger.inp'

def main():
    '''Main driver routine.'''
    args = _parse_arguments()
    try:
        mass, diskr, eigv, ansatz, matinpo = reading.reading(args.directory)
    except OSError as exc:
        print("Failed to read input file '{}'".format(_INPUT_FILE))
        print("Exception raised: {}".format(exc))
        sys.exit(1)


def _parse_arguments():
    parser = argparse.ArgumentParser(description=_DESCRIPTION)
    msg = 'Directory, where input file is located and where output should be'\
        ' written to (default: .)'
    parser.add_argument('-d', '--directory', default='.', help=msg)
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    main()