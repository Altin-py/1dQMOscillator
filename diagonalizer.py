#!/usr/bin/env python3
"""Routines for the diagonalization of square matrices"""
import scipy.linalg as linalg


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
