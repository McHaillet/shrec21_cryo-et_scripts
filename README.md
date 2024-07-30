# SHREC'21 cryo-ET dataset generation

This repository contains scripts to generate the SHREC'21 cryo-ET track dataset (doi:10.34894/XRTJMA). 

It makes use of PyTOM (commit: [master da64c6f]). Some of the scripts here have hard coded paths to the clone of PyTOM, specifically the following links are used directly:

* simulates a tomogram from a folder of input structures: /path/to/pytom/simulation/MicrographModeller.py
* generate electrostatic potential (real and imaginary part): /path/to/pytom/simulation/potential.py
* generate a vesicle electrostatic potential: /path/to/pytom/simulation/membrane.py

Some paths to the clone are also needed to access data:

* small MD equilibrated membrane patch used for sampling vesicles: /path/to/pytom/simulation/membrane_models/dppc128.pdb
* K2 detector data, DQE and MTF: /path/to/pytom/simulation/detectors/
