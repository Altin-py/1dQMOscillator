#!/usr/bin/env python3
"""Routines for building the Hamiltonian of a discretized one dimensional
quandum system and for its corresponding diagonalization"""
import scipy.linalg as linalg
import numpy as np


def hamiltonian(mass, delta, file_pot="potential.dat"):
    """Construct the Hamiltonian for a discretized one dimensional
quandum system. It requires a file with the values of the
external potential (second column) for each value of the discretized positions
(first column). File called "potential.dat" by default.
    Args:
        mass: Mass of the system. Scalar.
        delta: Distance between the discretized points. Scalar.
        file_pot: Name of the file with the potential. Default: "potential.dat"

    Returns:
        ham: Hamiltonian matrix (dim, dim) of the discretized system.
    """
    pot = np.loadtxt(file_pot)[:,1]
    dim = pot.shape[0]
    const = 1 / (mass * delta * delta)
    ham = np.zeros((dim, dim))
    for ii in range(dim-1):
        ham[ii, ii] = const + pot[ii]
        ham[ii, ii+1] = ham[ii+1, ii] = -0.5 * const
    ham[dim-1, dim-1] = const + pot[dim-1]
    return ham



def diagonalize(aa):
    """Diagonalizes a complex hermitian or real symmetrical matrix.

    Args:
        aa: Matrix to be diagonalized. Shape: (dim, dim)

    Returns:
        eigval: Vector (s,) with the unordered eigenvalues of the matrix aa.
        eigvec: Matrix (dim, s) whose column eigvec[:,i] correspond to the
        eigenvector associated to the eigenvalue eigval[i].

    Raises:
        scipy.linalg.LinAlgError: if the eigenvalue computation does not
        converge.
    """
    eigval, eigvec = linalg.eigh(aa)
    return eigval, eigvec
