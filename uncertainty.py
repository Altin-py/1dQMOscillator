#!/usr/bin/env python3
"""
Calculates the uncertainty of a variable (multiplicative operator) in a 1D
discretized quantum system.
"""
import numpy as np


def expectationval(aa, bb, delta):
    """Calculates the expectation value of the discretized operator in each
    eigenstate of the system.

    Args:
        aa: Vector of the discretized values of the operator. Shape: (dim,)
        bb: Matrix of the eigenstates of the system. Shape: (dim, num_eig),
        where s is the number of eigenstates.
        delta: Distance between the discretized points. Scalar.

    Returns:
        exp: Vector of the expectation values of the operator in each
        eigenstate. Shape: (num_eig,)

    Raises:

    """
    num_eig = bb.shape(1)
    dim = bb.shape(0)
    exp = np.zeros(num_eig)
    for jj in range(num_eig):
        for ii in range(dim):
            exp[jj] += bb[ii, jj]*aa[ii]*bb[ii, jj]
        exp[jj] *= delta
    return exp


def uncertainty(aa, bb, delta):
    """Calculates the uncertainty of a multiplicative operator in each
    eigenstate of a 1D discretized quantum system.

    Args:
        aa: Vector of the discretized values of the operator. Shape: (dim,)
        bb: Matrix of the eigenstates of the system. Shape: (dim, num_eig),
        where s is the number of eigenstates.
        delta: Distance between the discretized points. Scalar.

    Returns:
        sigma: Vector of the uncertainty values of the operator in each
        eigenstate, defined as the square root of the expectation value of the
        squared operator minus the squared expectation value of the operator
        itself. Shape: (num_eig,)

    Raises:

    """
    xx_2 = aa*aa
    xx_2_exp = expectationval(xx_2, bb, delta)
    xx_exp_2 = np.square(expectationval(aa, bb, delta))
    sigma = np.sqrt(xx_2_exp-xx_exp_2)
    return sigma
