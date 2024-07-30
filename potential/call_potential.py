import os

# Chimera and pytom should be on path for this script.

# V_ICE = 4.5301
# voltage = 300


files = ['1BXN.pdb', '1QVR.pdb', '1S3X.pdb', '1U6G.pdb', '2CG9.pdb', '3CF3.pdb', '3D2F.pdb', '3H84.pdb', '3GL1.pdb', '3QM1.pdb', '4CR2.pdb', '4V94.cif', '5mrc.cif']

for pdb_file in files:
    print(f'potential for {pdb_file}')
    # id = pdb_file.split('.')[0]
    os.system(f'pytom /path/to/pytom/simulation/potential.py -f {pdb_file} -d pdb/ -o ./ -s 1 -n 2 -b 5 -m -a --cores 4')
    