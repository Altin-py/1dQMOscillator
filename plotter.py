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
    name = args.title


    directory = args.directory
    prefactor = args.pref
    eigv = rd.reading(os.path.join(directory,_INPUT_FILE0))[2]
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
    firsteigv = np.int(eigv[0])
    lasteigv = np.int(eigv[1])

    plt.figure(figsize=(15, 7))


    plt.subplot(1, 2, 1)
    plt.title(name, fontsize=14)
    plt.xlabel("x [Bohr]", fontsize=14)
    plt.ylabel("Energy [Hartree]", fontsize=14)


    plt.plot(potential[:,0],potential[:,1])

    for xx in range(firsteigv, lasteigv+1):
        plt.plot(wavefunct[:,0], prefactor*wavefunct[:, xx]+energies[xx-firsteigv])

    if args.xmin is None:
        xmin = plt.xlim()[0]
    else:
        xmin = np.float(args.xmin)

    if args.xmax is None:
        xmax = plt.xlim()[1]
    else:
        xmax = np.float(args.xmax)


    if args.ymin is None:
        ymin = plt.ylim()[0]
    else:
        ymin = np.float(args.ymin)

    if args.ymax is None:
        ymax = plt.ylim()[1]
    else:
        ymax = np.float(args.ymax)

    plt.ylim(ymin, ymax)
    plt.xlim(xmin, xmax)

    plt.hlines(energies[firsteigv-1:lasteigv], xmin, xmax, color="gray")
    plt.plot(expect, energies[firsteigv-1:lasteigv], "g+")

    plt.subplot(1, 2, 2)
    plt.title('sigmax', fontsize=14)
    plt.xlabel("x [Bohr]", fontsize=14)
    plt.ylabel("Energy [Hartree]", fontsize=14)
    xmin = 0
    xmax = plt.xlim()[1]
    plt.ylim(ymin, ymax)
    plt.xlim(xmin, xmax)
    plt.plot(uncertainty,expect+energies,'b+')
    plt.hlines(energies[firsteigv-1:lasteigv], xmin, xmax, color="gray")

    plt.show()

def _parse_arguments():
    parser = argparse.ArgumentParser(description=_DESCRIPTION)
    msg = 'Directory, where input file is located and where output should be'\
        ' written to (default: .)'
    parser.add_argument('-d', '--directory', metavar='DIR', default='.', help=msg)

    msg = 'State name of the used potential as a string. '
    parser.add_argument('-t', '--title',default=None, help=msg)


    msg = 'Minimum of plotted x-axis'
    parser.add_argument('-xmin','-xminimum', default=None, help=msg)
    msg = 'Maximum of plotted x-axis'
    parser.add_argument('-xmax','-xmaximum', default=None, help=msg)

    msg = 'Minimum of plotted y-axis'
    parser.add_argument('-ymin','-yminimum', default=None, help=msg)
    msg = 'Maximum of plotted y-axis'
    parser.add_argument('-ymax','-ymaximum', default=None, help=msg)

    msg = 'Scaling prefactor of wavefunctions'
    parser.add_argument('-pref','-prefactor', type=float, default=1.0, help=msg)

    args = parser.parse_args()
    return args

   # plt.savefig("plot.png")

if __name__ == '__main__':
    main()
