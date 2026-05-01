"""
Simple driver file to create a 2d and 3d plots of the deep water array.
"""

from fad import Project
import os

# define name of ontology input file
dir = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(dir,'task49_deepwater_array.yaml')

# initialize Project class with input file, use RAFT for 3D plotting
project = Project(file=input_file,raft=True)

# plot 2D
project.plot2d(plot_bathymetry = False)

# plot 3D
project.plot3d(plot_fowt = True, plot_boundary_on_bath=False, plot_bathymetry = False)