#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Plots the wavefunctions and the potentials from the written files
"""
import sys
import os.path
import argparse
import numpy as np
import matplotlib.pyplot as plt
import reading as rd

_DESCRIPTION = '''Plots the output Data of schrodinger. inp. Requires the used
directory to contain energies.dat, wavefunct.dat, potential.dat. Additional the
range of plotting can be determined'''

_INPUT_FILE0 = 'schrodinger.inp'
_INPUT_FILE1 = 'energies.dat'
_INPUT_FILE2 = 'wavefunct.dat'
_INPUT_FILE3 = 'potential.dat'
_INPUT_FILE4 = 'expvalues.dat'


def main():
    '''Main driver routine of the visualisation.'''
    args = _parse_arguments()
    directory = args.directory
    prefactor = args.pref
    eigv = rd.reading(os.path.join(directory,_INPUT_FILE0))[2]
    xmin = args.xmin
    xmax = args.xmax
    ymin = args.ymin
    ymax = args.ymax
    try:
        potpath = os.path.join(directory, 'potential.dat')
    except FileNotFoundError as exc:
        print("Not found a file called '{}' in the folder".format(_INPUT_FILE3))
        print("Exception raised: {}".format(exc))
        sys.exit(1)
    potential = np.loadtxt(potpath)
    try:
        wavpath = os.path.join(directory, 'wavefuncs.dat')
    except FileNotFoundError as exc:
        print("Not found a file called '{}' in the folder".format(_INPUT_FILE2))
        print("Exception raised: {}".format(exc))
        sys.exit(1)
    wavefunct = np.loadtxt(wavpath)
    try:
        energypath = os.path.join(directory, 'energies.dat')
    except FileNotFoundError as exc:
        print("Not found a file called '{}' in the folder".format(_INPUT_FILE1))
        print("Exception raised: {}".format(exc))
        sys.exit(1)
    energies = np.loadtxt(energypath)
    try:
        exppath = os.path.join(directory, 'expvalues.dat')
    except FileNotFoundError as exc:
        print("Not found a file called '{}' in the folder".format(_INPUT_FILE4))
        print("Exception raised: {}".format(exc))
        sys.exit(1)
    expect = np.loadtxt(exppath)[:,0]
    uncertainty = np.loadtxt(exppath)[:,1]
    firsteigv = eigv[0]
    lasteigv = eigv[1]

    plt.figure(figsize=(15, 7))

    plt.ylim(ymin, ymax)
    plt.xlim(xmin, xmax)


    plt.plot(potential[:,0],potential[:,1])

    for xx in range(np.int(firsteigv), np.int(lasteigv)+1):
        plt.plot(wavefunct[:,0],prefactor*wavefunct[:,xx]+energies[xx-np.int(firsteigv)])

    plt.show()


def _parse_arguments():
    parser = argparse.ArgumentParser(description=_DESCRIPTION)
    msg = 'Directory, where input file is located and where output should be'\
        ' written to (default: .)'
    parser.add_argument('-d', '--directory', metavar='DIR', default='.', help=msg)

    msg = 'Minimum of plotted x-axis'
    parser.add_argument('-xmin','-xminimum', type=int, default=-10, help=msg)
    msg = 'Maximum of plotted x-axis'
    parser.add_argument('-xmax','-xmaximum', type=int, default=10, help=msg)

    msg = 'Minimum of plotted y-axis'
    parser.add_argument('-ymin','-yminimum', type=int, default=-10, help=msg)
    msg = 'Maximum of plotted y-axis'
    parser.add_argument('-ymax','-ymaximum', type=int, default=10, help=msg)

    msg = 'Scaling prefactor of wavefunctions'
    parser.add_argument('-pref','-prefactor', type=float, default=1.0, help=msg)

    args = parser.parse_args()
    return args

    plt.savefig("plot.png")

if __name__ == '__main__':
    main()
