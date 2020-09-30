#!/usr/bin/env python3
"""
Calculates the expectation value of a multiplicative operator in each
eigenstate of a 1D discretized quantum system and the corresponding
uncertainty.
"""
import numpy as np


def expectationval(aa, bb, delta):
    """Calculates the expectation value of the discretized (multiplicative
    operator in each eigenstate of the system.

    Args:
        aa: Vector of the discretized values of the operator. Shape: (dim,)
        bb: Matrix of the eigenstates of the system. Shape: (dim, num_eig)
        delta: Distance between the discretized points. Scalar.

    Returns:
        Vector (num_eig,) of the expectation values of the operator in """\
        """each eigenstate.
    """
    num_eig = bb.shape[1]
    dim = bb.shape[0]
    exp = np.zeros(num_eig)

    for jj in range(num_eig):
        for ii in range(dim):
            exp[jj] = exp[jj] + bb[ii, jj]*aa[ii]*bb[ii, jj]
        exp[jj] = exp[jj]*delta

    return exp


def uncertainty(aa, bb, delta):
    """Calculates the uncertainty of an operator in each eigenstate of a 1D
    discretized quantum system.

    Args:
        aa: Vector of the discretized values of the operator. Shape: (dim,)
        bb: Matrix of the eigenstates of the system. Shape: (dim, num_eig)
        delta: Distance between the discretized points. Scalar.

    Returns:
        Vector (num_eig,) of the uncertainty values of the operator in """\
     """each eigenstate, defined as the square root of the expectation """\
     """value of the squared operator minus the squared expectation value """\
     """ of the operator itself. Shape:
    """
    xx_2 = np.dot(aa, aa)
    xx_2_exp = expectationval(xx_2, bb, delta)
    xx_exp_2 = expectationval(aa, bb, delta)*expectationval(aa, bb, delta)
    sigma = np.sqrt(xx_2_exp - xx_exp_2)

    return sigma
