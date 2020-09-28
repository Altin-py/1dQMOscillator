#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Plots the wavefunctions and the potentials from the written files
"""
import os.path
import numpy as np
import matplotlib.pyplot as plt
import interpolate


def plotter(directory='schroedinger/POT_ASYM/', firsteigv, lasteigv, xmin = -10, xmax = 10, ymin = -10, ymax = 10 ):
    """
    Plots.
    """

    interpolate.interpolate(directory)
    potpath = os.path.join(directory, 'potential.dat')
    wavpath = os.path.join(directory, 'wavefuncs.dat')

    potential = np.loadtxt(potpath)
    wavefunct = np.loadtxt(wavpath)

    plt.figure(figsize=(15, 7))




    xlim = xmin, xmax
    ylim = ymin, ymax


    plt.plot(potential[:,0],potential[:,1])

    plt.plot(wavefunct[:,0],wavefunc[:,1])

    return plt.show()


