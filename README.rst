************************************
SOSE: Solver Of Schrödinger Equation
************************************

Schrodinger is a package for solving the one-dimensional Schrodinger 
equation for an arbitrary potential.

Prerequisites
=============

SOSE needs Python 3 and the SciPy and NumPy packages.

Creating the input
==================

Create an input file 'schrodinger.in' containing (everything in atomic 
units): the mass, the interval considered with the number of divisions 
for its discretization, the first and last eigenvalue that should be 
included in the output, the type of interpolation that should be applied 
between the discretized points, the number of interpolation points and x 
declarations and the corresponding declarations for the potential. Each 
independent parameter should be in a separate line.
The input should look like the next example (for a finite potential 
well)::
	
	2.0		        # mass
	-2.0 2.0 1999	# xMin xMax nPoint
	1 3		        # first and last eigenvalue in output
	linear		    # interpolation type
	6		        # number of interpolation points
	-2.0	0.0
	-0.5	0.0
	-0.5	-10.0
	0.5	-10.0
	0.5	0.0
	2.0	0.0


Running the program
===================

Execute the `schrodinger.py` script in the folder with the input file 
`schrodinger.in`::

  schrodinger.py

If the input file is located in another directory, you may specify the folder
using the ``-d`` option::

  schrodinger.py -d somedir

The output will be always written into the same folder as the input.

Separately, once the main script has been executed, the `plotter.py` 
script can be called to plot the output files of the main program.

`plotter.py` will show the plot in the console and also save it in the
folder where it has been executed. Or, alternatively, in the folder
specified using the ``-d`` option::

  plotter.py -d somedir


Interpreting the result
=======================

The result is written into the output files::
  * `potential.dat`: It contains the positions and the corresponding values
of the interpolated potential, the file would look as::

  -2.000000000000000000e+00 0.000000000000000000e+00
  -1.997997997997998043e+00 0.000000000000000000e+00

  * `energies.dat`: It contains the obtained eigenvalues, the file would look
as::

  1.540583630743308230e-01
  6.162330721775809428e-01

  * `wavefunctions.dat`: It contains the positions and the corresponding values
of each eigenfunction, the file would look as::

  -2.000000000000000000e+00 4.967292090214622824e-05 -9.934571924097187990e-05 1.490182724511837674e-04 -1.986904579788334425e-04 -2.483621532540088942e-04
  -1.997997997997998043e+00 9.934571924129814344e-05 -1.986904579798026650e-04 2.980332357178472162e-04 -3.973730719985991587e-04 -4.967089863605157274e-04

  * `expvalues.dat`: It contains the expectation value of the position operator
and the corresponding values of the uncertainties, the file would look as::

  -2.505711814896135333e-14 3.237508297451815314e-02
  -2.510738070445538663e-14 4.761349610829506557e-02

===================
