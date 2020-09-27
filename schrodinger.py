#!/usr/bin/env python3
"""
Solves Schrödinger equation for a one dimensional time independent potential.
"""
import sys
import os.path
import argparse
import reading as reading
import solver as solver
import uncertainty as uncertainty
import writing as writing
import interpolate as interpol
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
        mass, diskr, num_eigv, ansatz, matinpo = reading.reading(args.directory)
    except FileNotFoundError as exc:
        print("Not found a file called '{}' in the folder".format(_INPUT_FILE))
        print("Exception raised: {}".format(exc))
        sys.exit(1)

    interpol.interpolate(directory)
    delta = (diskr[1] - diskr[0]) / diskr[2]
    first_eig = np.int(num_eigv[0]-1)
    last_eig = int(num_eigv[1])
    pos = np.loadtxt("potential.dat")[:,0]
    ham = solver.hamiltonian(mass, delta)
    eigval, eigvec = solver.diagonalize(ham)
    writing.write_energies(eigval[first_eig:last_eig])
    writing.write_wavefuncs(pos, eigvec[:,first_eig:last_eig])
    exp_val = uncertainty.expectationval(pos, eigvec[:,first_eig:last_eig], delta)
    sigma = uncertainty.uncertainty(pos, eigvec[:,first_eig:last_eig], delta)
    writing.write_expvalues(exp_val[first_eig:last_eig], sigma[first_eig:last_eig])


def _parse_arguments():
    parser = argparse.ArgumentParser(description=_DESCRIPTION)
    msg = 'Directory, where input file is located and where output should be'\
        ' written to (default: .)'
    parser.add_argument('-d', '--directory', default='.', help=msg)
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    main()
