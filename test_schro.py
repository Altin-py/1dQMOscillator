#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Routines to test the reading, interpolate and solver modules.
"""
import os.path
import pytest
import numpy as np
import reading
import solver
import interpolate as interpol


ABSOLUTE_TOLERANCE = 1e-5
RELATIVE_TOLERANCE = 1e-5

TESTDATADIR = 'testdata'

TESTS = ['finite', 'asymmetric', 'infinite', 'harmonic_cubic',
         'harmonic_linear', 'harmonic_single']


def get_test_input(testname):
    "Reads the input for a given test."
    testinfile = os.path.join(TESTDATADIR, testname + '.in')
    mass, diskr, num_eigv, ansatz, matinpo = reading.reading(testinfile)
    return mass, diskr, num_eigv, ansatz, matinpo


def get_test_output(testname):
    "Reads the reference ouput for a given test."
    testoutfile_pot = os.path.join(TESTDATADIR, testname + '_pot.out')
    testoutfile_eig = os.path.join(TESTDATADIR, testname + '_eig.out')
    discr_pot = reading.read_test_output_pot(testoutfile_pot)
    eigval = reading.read_test_output_eig(testoutfile_eig)
    return discr_pot, eigval


@pytest.mark.parametrize("testname", TESTS)
def test_discr_pot(testname):
    "Tests the interpolation function"
    mass, diskr, num_eigv, ansatz, matinpo = get_test_input(testname)
    discr_pot_expected = get_test_output(testname)[0]
    discr_pot_to_test = interpol.interpolate(diskr, ansatz, matinpo)[:,1]

    assert np.allclose(discr_pot_to_test, discr_pot_expected,
                       atol=ABSOLUTE_TOLERANCE, rtol=RELATIVE_TOLERANCE)

@pytest.mark.parametrize("testname", TESTS)
def test_eigval(testname):
    "Tests the solver module"
    mass, diskr, num_eigv, ansatz, matinpo = get_test_input(testname)
    eigval_expected = get_test_output(testname)[1]
    delta = (diskr[1] - diskr[0]) / diskr[2]
    testoutfile_pot = os.path.join(TESTDATADIR, testname + '_pot.out')
    first_eig = np.int(num_eigv[0])-1
    last_eig = np.int(num_eigv[1])
    eigval_to_test = solver.diagonalize(mass, delta,
                                        testoutfile_pot)[0][first_eig:last_eig]

    assert np.allclose(eigval_to_test, eigval_expected,
                       atol=ABSOLUTE_TOLERANCE, rtol=RELATIVE_TOLERANCE)


if __name__ == '__main__':
    pytest.main()
