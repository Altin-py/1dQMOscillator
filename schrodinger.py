#!/usr/bin/env python3
"""
Solves Schrödinger equation for a one dimensional time independent potential.
"""
import sys
import os.path
import argparse
import SOSE.reading as reading
import SOSE.solver as solver
import SOSE.uncertainty as uncertainty
import SOSE.writing as writing
import SOSE.interpolate as interpol
import numpy as np

_DESCRIPTION = '''Solves the Schrödinger equation for a discretized one
dimensional quantum system. It requires an input file "schrodinger.inp",
containing the ...'''

_INPUT_FILE = 'schrodinger.inp'

def main():
    '''Main driver routine.'''
    args = _parse_arguments()
    directory = args.directory
    try:
        mass, diskr, eigv, ansatz, matinpo = reading.reading(args.directory)
    except OSError as exc:
        print("Failed to read input file '{}'".format(_INPUT_FILE))
        print("Exception raised: {}".format(exc))
        sys.exit(1)

    interpol.interpolate(directory)
    delta = (diskr[2] - diskr[1]) / diskr[3]
    pos = np.loadtxt("potential.dat")[0]
    ham = solver.hamiltonian(mass, delta)
    eigval, eigvec = solver.diagonalize(ham)
    writing.write_energies(eigval)
    writing.write_wavefuncs(pos, eigvec)
    exp_val = uncertainty.expectationval(pos, eigvec, delta)
    sigma = uncertainty.uncertainty(pos, eigvec, delta)
    writing.write_expvalues(exp_val, sigma)


def _parse_arguments():
    parser = argparse.ArgumentParser(description=_DESCRIPTION)
    msg = 'Directory, where input file is located and where output should be'\
        ' written to (default: .)'
    parser.add_argument('-d', '--directory', default='.', help=msg)
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    main()