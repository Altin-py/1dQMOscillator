#!/usr/bin/env python3
"""
Output for the Schrodinger equation resolution.
"""
import numpy as np
import os.path


def write_potential(pos, pot, directory, filename="potential.dat"):
    '''Writes the discretized potential into a file.

    Args:
        pos: Vector with all the discretized positions (n,)
        pos: Vector with all the discretized values for the potential (n,)
        directory: Name of the directory where the file should be written
        filename: Name of the file where the results should be written to. By
        default: "potential.dat".
    '''
    file = os.path.join(directory, filename)
    info = np.column_stack((pos, pot))
    np.savetxt(file, info)


def write_energies(aa, directory, filename="energies.dat"):
    '''Writes the selected eigenvalues of the Hamiltonian into a file.

    Args:
        aa: Vector with all the eigenvalues (s,)
        directory: Name of the directory where the file should be written
        filename: Name of the file where the results should be written to. By
        default: "energies.dat".
    '''
    file = os.path.join(directory, filename)
    np.savetxt(file, aa.transpose())


def write_wavefuncs(aa, bb, directory, filename="wavefuncs.dat"):
    '''Writes the selected eigenfunctions of the Hamiltonian into a file.

    Args:
        aa: Vector with all the discretized positions. Shape: (n,)
        bb: Matrix with all the eigenfuncions at each postion. Shape: (n, s)
        directory: Name of the directory where the file should be written
        filename: Name of the file where the results should be written to. By
        default: "eigenfuncs.dat".
    '''
    file = os.path.join(directory, filename)
    # Matrix with both variables, aa is added as the first column of bb
    info = np.column_stack((aa, bb))
    np.savetxt(file, info)


def write_expvalues(aa, bb, directory, filename="expvalues.dat"):
    '''Writes the expectation values of an operator, together with the
    corresponding uncertainty, for each chosen eigenstate into a file.

    Args:
        aa: Vector of the expectation values of the operator in each
        eigenstate. Shape: (s,)
        bb: Vector of the uncertainty values of the operator associated with
        each eigenstate. Shape: (s,)
        directory: Name of the directory where the file should be written
        filename: Name of the file where the results should be written to. By
        default: "expvalues.dat".
    '''
    file = os.path.join(directory, filename)
    # Matrix with both vectors as columns
    info = np.column_stack((aa, bb))
    np.savetxt(file, info)
