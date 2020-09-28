#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Reads out Data from reading.py and uses it to
interpolate the potentials
"""
import numpy as np
from scipy.interpolate import interp1d, CubicSpline, BarycentricInterpolator

def interpolate(diskr, ansatz, matinpo):
    """
    Function to interpolate the data with chosen nethod

    Args:
        diskr:
        ansatz:
        matinpo:
    return:
        nothing but savees the plotable data in x,y format
    """

    xdat = np.linspace(np.int(diskr[0]), np.int(diskr[1]), np.(diskr[2]))

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
