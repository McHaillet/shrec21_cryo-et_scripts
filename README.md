# SHREC'21 cryo-ET dataset generation

This repository contains scripts to generate the SHREC'21 cryo-ET track dataset [doi:10.34894/XRTJMA](https://dataverse.nl/dataset.xhtml?persistentId=doi:10.34894/XRTJMA). 

### Dependencies

You need to have PyTOM installed. Specifically, for the generation of SHREC'21, commit: [master da64c6f](https://github.com/SBC-Utrecht/PyTom/tree/da64c6f62b23eb23d363820f2a29d77be70fd470).

### Note on file paths

Some of the scripts here have hard coded paths to the clone of PyTOM, specifically the following links are used directly and need to be updated:

* simulates a tomogram from a folder of input structures: /path/to/pytom/simulation/MicrographModeller.py
* generate electrostatic potential (real and imaginary part): /path/to/pytom/simulation/potential.py
* generate a vesicle electrostatic potential: /path/to/pytom/simulation/membrane.py

Some paths to the clone are also needed to access data:

* small MD equilibrated membrane patch used for sampling vesicles: /path/to/pytom/simulation/membrane_models/dppc128.pdb
* K2 detector data, DQE and MTF: /path/to/pytom/simulation/detectors/

## Generating electrostatic potential

Go to the folder for electrostatic potential calculation:

```
cd potential/
```

The script `call_potential.py` needs to be updated with the correct paths. Additionally, all the atomic models need to be downloaded from the protein database (PDB) and placed in the folder `pdb/`. Once prepared the script is started:

```
python call_potential.py
```

The output from this script is generated in individual folders for each pdb and contains both an MRC with the real and imaginary part of the interaction potential. These files all need to be moved into the base folder `potential/` for the simulation to find it later.

## Run tomogram simulation

To start the full tilt-series and tomogram simulation go to the shrec_models directory:

```
cd shrec_models/
```

Update the `simulator.sh` file to refer to the correct paths. Then you can start simulation by calling

```
simulator.sh model_0.conf
```

, which will generate this model in a new directory `model_0/`. By default the `.conf` files are set to use 3 CPU cores (called `Nodes` in the configuration), this will require a looot of RAM memory ~200 GB: the parallelization is not very smart. The number of cores can be reduced, but running on a single core will still use 60 GB. 