#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Reads out Data from reading.py and uses it to
interpolate the potentials
"""
import numpy as np
import reading
from scipy.interpolate import interp1d, CubicSpline, BarycentricInterpolator
def interpolate(directory):
    """
    Function to interpolate the data with chosen nethod
    """
    mass, diskr, eigv, ansatz, matinpo = reading.reading(directory)

    xgraph = np.linspace(diskr[0], diskr[1], diskr[2])

    if ansatz == 'linear':
        yinter = interp1d(matinpo[:,0], matinpo[:,1], kind = 'linear')
        ygraph = yinter(xgraph)
    if ansatz == 'polynomial':
        yinter = BarycentricInterpolator(matinpo[:,0], matinpo[:,1])
        ygraph = yinter(xgraph)
    if ansatz == 'cspline':
        yinter = CubicSpline(matinpo[:,0], matinpo[:,1], bc_type='natural')
        ygraph = yinter(xgraph)

    return xgraph, ygraph