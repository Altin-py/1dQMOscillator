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

    args:
        directory where the potential.dat is supposed to be saved and where
        schrodinger.inp is
    return:
        nothing but savees the plotable data in x,y format
    """

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
    matrix = np.stack([xdat, ypot], axis=1)
    return matrix
