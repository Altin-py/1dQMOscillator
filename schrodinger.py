#!/usr/bin/env python3
"""
Solves Schrödinger equation for a one dimensional time independent potential.
"""
import sys
import os.path
import argparse
import reading
import solver
import uncertainty
import writing
import interpolate as interpol
import numpy as np
import scipy.linalg as linalg

_DESCRIPTION = '''Solves the Schrödinger equation for a discretized one
dimensional time intependent quantum system. It requires an input file
"schrodinger.inp", containing the (everything in atomic units):
the mass, the interval and the number of divisions for the  discretization,
the first and last eigenvalues that should be obtained, the type of
interpolation that should be applied, the number of interpolation points and
x declarations with the corresponding potential values. It produces four
output files: on with the values of the interpolated potential for each
position, one with the selected eigenvalues, another with the chosen
eigenfunctions for each value of x and the last one with the expectation values
of the position operator on each eigenstate and the corresponding
uncertainty.'''

_INPUT_FILE = 'schrodinger.inp'

def main():
    '''Main driver routine.'''
    args = _parse_arguments()
    direc = args.directory

    try:
        file = os.path.join(direc, "schrodinger.inp")
        mass, diskr, num_eigv, ansatz, matinpo = reading.reading(file)
    except FileNotFoundError as exc:
        print("Not found a file called '{}' in the folder".format(_INPUT_FILE))
        print("Exception raised: {}".format(exc))
        sys.exit(1)

    pot = interpol.interpolate(diskr, ansatz, matinpo)[:, 1]
    pos = interpol.interpolate(diskr, ansatz, matinpo)[:, 0]

    writing.write_potential(pos, pot, direc)

    delta = (diskr[1] - diskr[0]) / diskr[2]

    first_eig = np.int(num_eigv[0]-1)
    last_eig = np.int(num_eigv[1])

    try:
        eigval, eigvec = solver.diagonalize(mass, delta)
    except linalg.LinAlgError as exc:
        print("The eigenvalue computation does not converge.")
        print("Exception raised: {}".format(exc))
        sys.exit(2)

    exp_val = uncertainty.expectationval(pos, eigvec[:, first_eig : last_eig],
                                         delta)
    sigma = uncertainty.uncertainty(pos, eigvec[:, first_eig : last_eig],
                                    delta)

    writing.write_energies(eigval[first_eig : last_eig], direc)
    writing.write_wavefuncs(pos, eigvec[:, first_eig : last_eig], direc)
    writing.write_expvalues(exp_val[first_eig : last_eig],
                            sigma[first_eig : last_eig], direc)



def _parse_arguments():
    parser = argparse.ArgumentParser(description=_DESCRIPTION)
    msg = 'Directory, where input file is located and where output should be'\
        ' written to (default: .)'
    parser.add_argument('-d', '--directory', default='.', help=msg)
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    main()
