#!/usr/bin/env python3
"""
Calculates the uncertainty of a variable (multiplicative operator) in a 1D
discretized quantum system.
"""
import numpy as np
NO HE TENIDO EN CUENTA QUE QUIERO CALCULARLO TODO PARA CADA POSICION Y PARA
CADA AUTOESTADO

def expectationval(aa, bb, delta, s, n):
    """Calculates the expectation value of the discretized operator in each
    eigenstate of the system.

    Args:
        aa: Vector of the discretized values of the operator. Shape: (n,)
        bb: Matrix of the eigenstates of the system. Shape: (n,s), where s is
        the number of eigenstates.
        delta: Distance between the discretized points. Scalar.
        s: Number of eigenstates. Scalar.
        n: Number of discretized points. Scalar.

    Returns:
        exp: Expectation value of the operator.

    Raises:

    """
    exp=0.0
    for ii in range(n):
        exp+=aa[ii]*bb[ii, s]
    exp*=delta
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
        sigma: Uncertainty of the operator, defined as the square root of the
        expectation value of the squared operator minus the squared expectation
        value of the operator itself.

    Raises:

    """
    xx_2_in=expectationval(aa*aa, bb, delta, s, n)
    xx_2_out=np.square(expectationval(aa, bb, delta, s, n))
    sigma=np.sqrt(xx_2_in-xx_2_out)
    return sigma