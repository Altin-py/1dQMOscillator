#!/usr/bin/env python3
"""Routines for the diagonalization of square matrices"""
import numpy.linalg as linalg


def diagonalize(aa):
    """Diagonalizes a square matrix.

    Args:
        aa: Matrix to be diagonalized. Shape: (n, n)

    Returns:
        eigval: Vector (n,) with the unordered eigenvalues of the matrix aa.
        eigvec: Matrix (n, n) whose column eigvec[:,i] correspond to the
        eigenvector associated to the eigenvalue eigval[i].

    Raises:
        numpy.linalg.LinAlgError: if the eigenvalue computation does not
        converge.
    """
    eigval, eigvec=linalg.eig(aa)
    return eigval, eigvec
