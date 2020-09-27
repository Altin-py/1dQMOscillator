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
import writing
import interpolate as interpol


ABSOLUTE_TOLERANCE = 1e-10
RELATIVE_TOLERANCE = 1e-10

TESTDATADIR = 'testdata'

TESTS = ['finite', 'asymmetric', 'infinite', 'harmonic_cubic',
         'harmonic_linear', 'harmonic_single']


def get_test_input(testname):
    "Reads the input for a given test."
    testinfile = os.path.join(TESTDATADIR, testname + '.in')
    ### aa, bb = io.read_input(testinfile)
    ### return aa, bb


def get_test_output(testname):
    "Reads the reference ouput for a given test."
    testoutfile = os.path.join(TESTDATADIR, testname + '.out')
    ### result = io.read_result(testoutfile)
    ### return result


@pytest.mark.parametrize("testname", TESTS)



if __name__ == '__main__':
    pytest.main()
