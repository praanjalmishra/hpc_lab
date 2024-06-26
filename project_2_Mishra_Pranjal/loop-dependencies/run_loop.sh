#!/bin/bash
#SBATCH --job-name=recur         # Job name
#SBATCH --output=recur-%j.out    # Output file
#SBATCH --error=recur-%j.err     # Error file
#SBATCH --ntasks=1               # Number of tasks
#SBATCH --constraint=EPYC_7763   # Select node with CPU
#SBATCH --cpus-per-task=48       # Number of CPUs per task
#SBATCH --mem-per-cpu=1024       # Memory per CPU
#SBATCH --time=00:40:00          # Wall clock time limit

# Load some modules & list loaded modules
module load gcc
module list

# Compile
make clean
make

# Run the program without OMP:
echo "Running the Sequential Program"
./recur_seq
echo "---------------------------------------------"

# Run the program for OMP_NUM_THREADS equal to 1, 2, 4, 8, 16, 32 -- 5
for ((i=1; i<=6; i++))
do
  OMP_NUM_THREADS=$((2**i))
  echo "Running with OMP_NUM_THREADS=$OMP_NUM_THREADS"
  export OMP_NUM_THREADS
  ./recur_omp
  echo "---------------------------------------------"
done