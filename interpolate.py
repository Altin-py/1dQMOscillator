#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Reads out Data from reading.py and uses it to
interpolate the potentials
"""
import numpy as np
from scipy.interpolate import interp1d, CubicSpline, BarycentricInterpolator
import reading
def interpolate(directory):
    """
    Function to interpolate the data with chosen nethod
    """
    mass, diskr, eigv, ansatz, matinpo = reading.reading(directory)

    xdat = np.linspace(diskr[0], diskr[1], diskr[2])

    if ansatz == 'linear':
        yinter = interp1d(matinpo[:, 0], matinpo[:, 1], kind='linear')
        ypot = yinter(xdat)
    if ansatz == 'polynomial':
        yinter = BarycentricInterpolator(matinpo[:, 0], matinpo[:, 1])
        ypot = yinter(xdat)
    if ansatz == 'cspline':
        yinter = CubicSpline(matinpo[:, 0], matinpo[:, 1], bc_type='natural')
        ypot = yinter(xdat)

    return xdat, ypot
