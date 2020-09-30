#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interpolates the potential values from the input.
"""
import numpy as np
from scipy.interpolate import interp1d, CubicSpline, BarycentricInterpolator

def interpolate(diskr, ansatz, matinpo):
    """
    Function to interpolate the data with the chosen method.

    Args:
        diskr: Vector with the first and last values of the positions interval
        to interpolate and the number of points to interpolate. Shape: (3,)
        ansatz: String determining the method of interpolation.
        matinpo: Matrix with the positions (first column) and potential
        (second column) reference values. Shape: (r, 2)

    Returns: Matrix with the resulting values of the potential (second column)
    for each position (first column). Shape: (dim, 2)
    """

    xdat = np.linspace(np.int(diskr[0]), np.int(diskr[1]), np.int(diskr[2]))

    if ansatz == 'linear':
        yinter = interp1d(matinpo[:, 0], matinpo[:, 1], kind='linear')
        ypot = yinter(xdat)

    if ansatz == 'polynomial':
        yinter = BarycentricInterpolator(matinpo[:, 0], matinpo[:, 1])
        ypot = yinter(xdat)

    if ansatz == 'cspline':
        yinter = CubicSpline(matinpo[:, 0], matinpo[:, 1], bc_type='natural')
        ypot = yinter(xdat)

    matrix = np.stack([xdat, ypot], axis=1)

    return matrix
