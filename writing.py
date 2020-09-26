#!/usr/bin/env python3
"""
Output for the Schrodinger equation resolution.
"""
import numpy as np


def write_energies(aa,  filename="energies.dat"):
    '''Writes the eigenvalues of the Hamiltonian into a file.

    Args:
        filename: Name of the file where the results should be written to. By
        default: "energies.dat".
        aa: Vector with all the eigenvalues (s,)
    '''
    np.savetxt(filename, aa, delimiter='\n')


def write_wavefuncs(aa, bb,  filename="wavefuncs.dat"):
    '''Writes the eigenfunctions of the Hamiltonian into a file.

    Args:
        filename: Name of the file where the results should be written to. By
        default: "eigenfuncs.dat".
        aa: Vector with all the discretized positions. Shape: (n,)
        bb: Matrix with all the eigenfuncions at each postion. Shape: (n, s)
    '''
    #First we create a matrix as aa as first column and then the bb matrix
    info=np.append(aa.transpose(), bb, axis=1)
    np.savetxt(filename, info)


def write_expvalues(aa, bb , filename="expvalues.dat"):
    '''Writes the expectation values of an operator, together with the
    corresponding uncertainty, for each eigenstate into a file.

    Args:
        filename: Name of the file where the results should be written to. By
        default: "expvalues.dat".
        aa: Vector of the expectation values of the operator in each
        eigenstate. Shape: (s,)
        bb: Vector of the uncertainty values of the operator associated with
        each eigenstate. Shape: (s,)
    '''
    info=np.append(aa.transpose(), bb.transpose(), axis=1)
    np.savetxt(filename, info)

