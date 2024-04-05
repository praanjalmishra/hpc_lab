#!/bin/bash
#SBATCH --job-name=hist_seq      # Job name
#SBATCH --output=hist_seq-%j.out # Output file
#SBATCH --error=hist_seq-%j.err  # Error file
#SBATCH --ntasks=1               # Number of tasks
#SBATCH --constraint=EPYC_7763   # Select node with CPU
#SBATCH --cpus-per-task=4        # Number of CPUs per task
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
./hist_seq
echo "---------------------------------------------"

# Compile
csv=out/data.csv
mkdir -p out
if [[ -z $csv || ! -s $csv ]]; then
    echo "method, cores, time" > $csv
fi


# Run
# for i in 1 {4..32..4}
# do
#     echo "- $i"
#     OMP_NUM_THREADS=$i ./hist_omp > out/tmp$i.txt
#     tail -1 out/tmp$i.txt >> $csv
# done
echo "Running the Parallel Program"
for ((i = 0; i <= 5; i++)); do
    threads=$((2 ** i))  
    echo "- $threads"
    OMP_NUM_THREADS=$threads ./hist_omp > out/tmp$threads.txt
    tail -1 out/tmp$threads.txt >> $csv
    echo "---------------------------------------------"
done