#!/bin/bash
#SBATCH --job-name=scaling            # Job name    (default: sbatch)
#SBATCH --output=strong-scaling.out   # Output file (default: slurm-%j.out)
#SBATCH --error=strong-scaling.err    # Error file  (default: slurm-%j.out)
#SBATCH --ntasks=1                           # Number of tasks
#SBATCH --constraint=EPYC_7763               # Select node with CPU
#SBATCH --cpus-per-task=32                   # Number of CPUs per task
#SBATCH --mem-per-cpu=1024                   # Memory per CPU
#SBATCH --time=10:00:00                      # Wall clock time limit

#load modules
module load gcc
module load python/3.11.6

module list
#
#compile code
make clean
make

#!/bin/bash

# Create CSV file and write header
csv_file="scaling_strong_results.csv"
echo "Grid_Size,Num_Threads,Time_Spent" > $csv_file

# Grid sizes to be evaluated
grid_sizes=(64 128 256 512 1024)

# Number of threads from 1 to 24
for num_threads in {1..24}; do
    # Set the number of threads for OpenMP
    export OMP_NUM_THREADS=$num_threads

    # Iterate through each grid size
    for size in "${grid_sizes[@]}"; do
        # Run the program and redirect output to variable 'output'
        output=$(./main $size 100 0.01)

        # Parse and write the results to the CSV file
        # Assuming the output format is "simulation took <timespent> seconds"
        timespent=$(echo "$output" | grep -oP 'simulation took\s+(\d+\.\d+)\s+seconds')
        echo "$size,$num_threads,$timespent" >> $csv_file
    done
done

#python scaling_strong.py

