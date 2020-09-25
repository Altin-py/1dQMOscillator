#!/usr/bin/env python3
"""
Calculates the uncertainty of a variable (multiplicative operator) in a 1D
discretized quantum system.
"""
import numpy as np


def expectationval(aa, bb, delta, s, n):
    """Calculates the expectation value of the discretized operator in each
    eigenstate of the system.

    Args:
        aa: Vector of the discretized values of the operator. Shape: (n,)
        bb: Matrix of the eigenstates of the system. Shape: (n, s), where s is
        the number of eigenstates.
        delta: Distance between the discretized points. Scalar.
        s: Number of eigenstates. Scalar.
        n: Number of discretized points. Scalar.

    Returns:
        exp: Matrix of the expectation values of the operator in each position
        (rows) and in each eigenstate (columns). Shape: (n, s)

    Raises:

    """
    exp=np.zeros((n, s))
    for jj in range(s):
        for ii in range(n):
            exp[ii,jj]+=aa[ii]*bb[ii, jj]
        exp[ii,jj]*=delta
    return exp


def uncertainty(aa, bb, delta, s, n):
    """Calculates the uncertainty of a multiplicative operator in each
    eigenstate of a 1D discretized quantum system.

    Args:
        aa: Vector of the discretized values of the operator. Shape: (n,)
        bb: Matrix of the eigenstates of the system. Shape: (n,s), where s is
        the number of eigenstates.
        delta: Distance between the discretized points. Scalar.
        s: Number of eigenstates. Scalar.
        n: Number of discretized points. Scalar.

    Returns:
        sigma: Matrix of the uncertainty values of the operator, defined as the
        square root of the expectation value of the squared operator minus the
        squared expectation value of the operator itself. Shape: (n, s)

    Raises:

    """
    xx_2=aa*aa
    xx_2_exp=expectationval(xx_2, bb, delta, s, n)
    xx_exp_2=np.square(expectationval(aa, bb, delta, s, n))
    sigma=np.sqrt(xx_2_exp-xx_exp_2)
    return sigma