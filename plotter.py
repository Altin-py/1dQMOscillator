#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Plots the wavefunctions and the potentials from the written files
"""
import os.path
import numpy as np
import matplotlib.pyplot as plt
import interpolate

def plotter(directory='schroedinger/POT_ASYM/', firsteigv, lasteigv, [xmin, xmax], [ymin,ymax] ):
    """
    Plots.
    """
    if xmin is empty:
        xmin = diskr[0]
        xmax = diskr[1]
    if ymin is empty:
        ymin = -10
        ymax = 10

    interpolate.interpolate(directory)
    potpath = os.path.join(directory, 'potential.dat')
    wavpath = os.path.join(directory, 'wavefuncs.dat')

    potential = np.loadtxt(potpath)
    wavefunct = np.loadtxt(wavpath)

    plt.figure(figsize=(15, 7))




    xlim = xmin, xmax
    ylim = -0.5, 10


    plt.plot(potential[:,0],potential[:,1])

    return plt.show()


