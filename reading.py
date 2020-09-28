#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given the path of the schrodinger.inp
reads out all the variables for further access
"""
import numpy as np


def reading(file):

    """
    Reads input potentialextracts variables

    ARG:
        directory: directory of the schrodinger.inp

        Textfile containing potential info

    Return: mass, diskr, eigv, ansatz, numb, inpo

        Variables neccessary for further process
        numb: number of interpolation points
        ansatz: Ansatz for the interpolation
        eigv: first and last eigv
        diskr: Diskrete points used for interpolation
        diskr[0]=xmin, diskr[1]=xmax, diskr[2]=npoint
    """
    with open(file) as fp:
        data = fp.read().splitlines()
    mass = data[0]
    mass = np.float(mass.split('#')[0].strip())  #cuts off comments

    diskr = data[1].split()
    diskr = [np.float(diskr[0]),np.float(diskr[1]),np.float(diskr[2])]

    eigv = data[2].split()
    eigv = [np.float(eigv[0]),np.float(eigv[1])]

    ansatz = data[3].split('#')[0].split()[0]

    numb = data[4].split()
    numb = numb[0]
    numb = int(numb)
    inpo = data[5:5+numb]
    matinpo = np.zeros((numb, 2))
    for ii in range(numb):
        for jj in range(2):
            matinpo[ii, jj] = np.float(inpo[ii].split()[jj])
    return mass, diskr, eigv, ansatz, matinpo
