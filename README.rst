***********
Schrodinger
***********

Schrodinger is a package for solving the one-dimensional Schrodinger equation 
for an arbitrary potential.

Creating the input
==================

Create an input file 'schrodinger.in' containing (everything in atomic units):
the mass, the interval considered with the number of divisions for its discretization, 
the first and last eigenvalue that should be included in the output, the type
of interpolation that should be applied between the discretized points, the number
of interpolation points and xy declarations and the corresponding xy declarations
for the potential. Each independent parameter should be in a separate line.
The input should look like the next example (for a finite potential well)::
	
	2.0		        # mass
	-2.0 2.0 1999	# xMin xMax nPoint
	1 3		        # first and last eigenvalue in output
	linear		    # interpolation type
	6		        # number of interpolation points and xy declarations
	-2.0	0.0
	-0.5	0.0
	-0.5	-10.0
	0.5	-10.0
	0.5	0.0
	2.0	0.0

Running the program
===================
