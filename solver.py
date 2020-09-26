#!/usr/bin/env python3
"""Routines for building the Hamiltonian of a discretized one dimensional
quandum system and for its corresponding diagonalization"""
import scipy.linalg as linalg
import numpy as np


def hamiltonian(mass, delta, pot):
    """Construct the Hamiltonian for a discretized one dimensional
quandum system.

    Args:
        mass: Mass of the system. Scalar.
        delta: Distance between the discretized points. Scalar.
        pot: Vector of the values of the potential on each point. Shape(n,)

    Returns:
        ham: Hamiltonian matrix (n, n) of the discretized system.
    """
    a = 1 / (mass * delta * delta)
    ham=np.zeros((n,n))
    for ii in range(n-1):
        ham[ii,ii]=a + pot[ii]
        ham[ii,ii+1]=ham[ii+1,ii]=-0.5 * a
    ham[n-1,n-1]=a + pot[n-1]
    return ham



def diagonalize(aa):
    """Diagonalizes a complex hermitian or real symmetrical matrix.

    Args:
        aa: Matrix to be diagonalized. Shape: (n, n)

    Returns:
        eigval: Vector (s,) with the unordered eigenvalues of the matrix aa.
        eigvec: Matrix (n, s) whose column eigvec[:,i] correspond to the
        eigenvector associated to the eigenvalue eigval[i].

    Raises:
        numpy.linalg.LinAlgError: if the eigenvalue computation does not
        converge.
    """
    eigval, eigvec=linalg.eigh(aa)
    return eigval, eigvec
