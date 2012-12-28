
"""
pyh5md - Read and write H5MD files
==================================

The pyh5md module allows to reading and write H5MD files. H5MD is a file
specification found at http://nongnu.org/h5md/ designed 
for storing molecular data (structures of biophysical compounds, molecular 
dynamics simulations, ...).
"""

try:
    import h5py
except ImportError:
    print "pyh5md requires the h5py library."
    exit()

from core import *

__all__ = ["H5MD_File", "TrajectoryGroup", "Trajectory"]


