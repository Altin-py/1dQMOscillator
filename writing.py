#!/usr/bin/env python3
"""
Output for the Schrodinger equation resolution.
"""
import numpy as np


def write_potential(pos, pot, filename="potential.dat"):
    '''Writes the discretized potential into a file.

    Args:
        pos: Vector with all the discretized positions (n,)
        pos: Vector with all the discretized values for the potential (n,)
        filename: Name of the file where the results should be written to. By
        default: "potential.dat".
    '''
    info = np.column_stack((pos, pot))
    np.savetxt(filename, info)


def write_energies(aa, filename="energies.dat"):
    '''Writes the selected eigenvalues of the Hamiltonian into a file.

    Args:
        aa: Vector with all the eigenvalues (s,)
        filename: Name of the file where the results should be written to. By
        default: "energies.dat".
    '''
    np.savetxt(filename, aa.transpose())


def write_wavefuncs(aa, bb, filename="wavefuncs.dat"):
    '''Writes the selected eigenfunctions of the Hamiltonian into a file.

    Args:
        aa: Vector with all the discretized positions. Shape: (n,)
        bb: Matrix with all the eigenfuncions at each postion. Shape: (n, s)
        filename: Name of the file where the results should be written to. By
        default: "eigenfuncs.dat".
    '''
    #First we create a matrix as aa as first column and then the bb matrix
    info = np.column_stack((aa, bb))
    np.savetxt(filename, info)


def write_expvalues(aa, bb, filename="expvalues.dat"):
    '''Writes the expectation values of an operator, together with the
    corresponding uncertainty, for each chosen eigenstate into a file.

    Args:
        aa: Vector of the expectation values of the operator in each
        eigenstate. Shape: (s,)
        bb: Vector of the uncertainty values of the operator associated with
        each eigenstate. Shape: (s,)
        filename: Name of the file where the results should be written to. By
        default: "expvalues.dat".
    '''
    info = np.column_stack((aa, bb))
    np.savetxt(filename, info)
