#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Plots the wavefunctions and the potentials from the written files
"""
import os.path
import numpy as np
import matplotlib.pyplot as plt


#def plotter(directory='schroedinger/POT_ASYM/', xmin = -10, xmax = 10, ymin = -10, ymax = 10 ):
def plotter(eigv, directory):
    """
    Plots.
    """

    prefactor = 2.5

    firsteigv = eigv[0]
    lasteigv = eigv[1]


    potpath = os.path.join(directory, 'potential.dat')
    wavpath = os.path.join(directory, 'wavefuncs.dat')
    energypath = os.path.join(directory, 'energies.dat')

    potential = np.loadtxt(potpath)
    wavefunct = np.loadtxt(wavpath)
    energies = np.loadtxt(energypath)


    plt.figure(figsize=(15, 7))




#    xlim = xmin, xmax
    plt.ylim(0, 2.5)


    plt.plot(potential[:,0],potential[:,1])

    for xx in range(np.int(firsteigv), np.int(lasteigv)+1):
        plt.plot(wavefunct[:,0],prefactor*wavefunct[:,xx]+energies[xx-np.int(firsteigv)])

    plt.savefig("plot.png")

