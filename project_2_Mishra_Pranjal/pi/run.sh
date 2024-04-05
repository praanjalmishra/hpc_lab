#!/bin/bash
#SBATCH --job-name=benchmark_pi
#SBATCH --output=benchmark_pi.out
#SBATCH --error=benchmark_pi.err
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=42
#SBATCH --constraint=EPYC_7763
#SBATCH --time=00:20:00

# load some modules & list loaded modules
module load gcc python
# module load intel
module list

mkdir -p build
make clean
make

srun python3 pi_scale.py -n 100000000 -m 10000000 -t 64