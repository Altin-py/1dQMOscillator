#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given the path of the schrodinger.inp
converts input potential data into a plottable
file of the interpolated potential.
"""
import os.path
def readfile(directory):
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
    diskr = data[1]      #array mit Daten für Diskret
    eigv = data[2]      #first and last eigv
    ansatz = data[3]    #Interpolationsansatz
    numb = data[4][0]      #anzahl interpolationspunkte
    numb = int(numb)
    inpo = data[5:5+numb-1]
    return mass, diskr, eigv, ansatz, numb, inpo
