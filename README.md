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

## Generate vesicles

To generate membrane vesicles for the simulation the following command need to be run for each vesicle (while setting the correct path):

```
pytom /path/to/pytom/simulation/membrane.py --radius_factor 4 --spacing 5 -d potential/ --membrane_pdb /path/to/pytom/simulation/membrane_models/dppc128.pdb -x -v 300 --cores 4
```

The membrane simulation can take a lot of time as many atoms need to be sampled, the memory requirements are also high and depend on vesicle size. The `--radius_factor` determines the size of the vesicle, the default of 1 generates a vesicle approximately 45nm in diameter. The size is slightly randomized and varied over the ellipsoidal radii to generate 'random' ellipsoidal vesicles. For SHREC'21 we generated 3 vesicles with `--radius-factor` of 4 and and two with a factor of 6 (IIRC).

Once the vesicles are generated they need to be renamed by replacing `bilayer_5.00A_...x...x...nm` by `v1`-`v5` to be able to read the later.

## Run tomogram simulation

First, for SHREC'21 we scaled the simulated tilt-series to the power spectra of experimental images from [EMPIAR-10064](https://www.ebi.ac.uk/empiar/EMPIAR-10064/), the CTEM and mixedCTEM. These should be downloaded and placed in the folder `scaling_examples/`.

To start the full tilt-series and tomogram simulation go to the shrec_models directory:

```
cd shrec_models/
```

Update the `simulator.sh` file to refer to the correct paths. Then you can start simulation by calling

```
simulator.sh model_0.conf
```

, which will generate this model in a new directory `model_0/`. By default the `.conf` files are set to use 3 CPU cores (called `Nodes` in the configuration), this will require a looot of RAM memory ~200 GB: the parallelization is not very smart. The number of cores can be reduced, but running on a single core will still use 60 GB. 