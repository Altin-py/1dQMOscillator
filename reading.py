#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given the path of the schrodinger.inp,
reads out all the variables for further access.
"""
import numpy as np


def reading(file):
    """
    Reads input potential and extracts variables

    Args:
        file: path of input file, containing the mass, the interval and """\
        """the number of divisions for the  discretization, the first and """\
        """last eigenvalues that should be obtained, the type of """\
        """interpolation that should be applied, the number of """\
        """interpolation points and x declarations with the corresponding """\
        """potential values (all separated in different lines).

    Returns:
        * Mass of the system. Scalar.
        * Vector with all the values for the discretization: the """\
        """minimum and maximum values of the selected positions interval """\
        """and the number of points. Shape: (3,)
        * Vector with the first and last chosen eigenvalues. Shape: (2,)
        * Ansatz for the interpolation (method of interpolation)
        * Matrix with the x declarations and corresponding """\
        """potential values. Shape: (r, 2)
    """
    with open(file) as fp:
        data = fp.read().splitlines()
    mass = data[0]
    mass = np.float(mass.split('#')[0].strip())  #cuts off comments

    diskr = data[1].split()
    diskr = [np.float(diskr[0]), np.float(diskr[1]), np.float(diskr[2])]

    eigv = data[2].split()
    eigv = [np.float(eigv[0]), np.float(eigv[1])]

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


def read_test_output_pot(file):
    """
    Reads the output file (reference) for the potential for the tests.

    Args:
        file: path of the file.
    """
    discr_pot = np.loadtxt(file)[:, 1]

    return discr_pot


def read_test_output_eig(file):
    """
    Reads the output file (reference) for the eigenvalues for the tests.

    Args:
        file: path of the file.
    """
    eigval = np.loadtxt(file)

    return eigval
