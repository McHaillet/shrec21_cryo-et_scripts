if [ "$1" != "" ]; then
  pytom /path/to/pytom/simulation/MicrographModeller.py $1
else
    echo "Please pass path to conf file (for example, /path/to/pytom/simulation/simulation_tilt.conf)"
fi



