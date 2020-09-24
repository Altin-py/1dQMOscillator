#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given the path of the schrodinger.inp
converts input potential data into a plottable
file of the interpolated potential.
"""
import os.path
import numpy as np
# import numpy as np
def reading(directory):
    """
    Reads input potentialextracts variables

    ARG:
        directory: directory of the schrodinger.inp

        Textfile containing potential info

    Return: mass, diskr, eigv, ansatz, numb, inpo

        Variables neccessary for further process
    """
    file = os.path.join(directory, "schrodinger.inp")
    with open(file) as fp:
        data = fp.read().splitlines()
    mass = data[0]
    mass = np.asfarray(mass, float)
    diskr = data[1].split()     #array mit Daten für Diskret
    diskr = np.asfarray(diskr, float)
    eigv = data[2].split()      #first and last eigv
    eigv = np.asfarray(eigv, float)
    ansatz = data[3]    #Interpolationsansatz
    numb = data[4].split()      #anzahl interpolationspunkte
    numb = numb[0]
    numb = int(numb)
    inpo = data[5:5+numb]
    matinpo = np.zeros((numb, 2))
    for ii in range(numb):
        for jj in range(2):
            matinpo[ii, jj] = np.float(inpo[ii].split()[jj])
    return mass, diskr, eigv, ansatz, numb, matinpo
