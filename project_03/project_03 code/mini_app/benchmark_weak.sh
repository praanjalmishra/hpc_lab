#!/bin/bash
#SBATCH --job-name=weak_scaling            # Job name    (default: sbatch)
#SBATCH --output=weak-scaling.out     # Output file (default: slurm-%j.out)
#SBATCH --error=weak-scaling.err      # Error file  (default: slurm-%j.out)
#SBATCH --ntasks=1                           # Number of tasks
#SBATCH --constraint=EPYC_7763               # Select node with CPU
#SBATCH --cpus-per-task=64                   # Number of CPUs per task
#SBATCH --mem-per-cpu=1024                   # Memory per CPU
#SBATCH --time=20:00:00                      # Wall clock time limit

#load modules
module load gcc
module load python/3.11.6

module list

#compile code
make clean
make

#run strong scaling
#!/bin/bash

main_run() {
  local threads=$1
  local grid_size=$2
  local nt=$3
  local t=$4
  local csv_file=$5

  # Set number of threads and run benchmark
  export OMP_NUM_THREADS=$threads
  output=$(./main $grid_size $nt $t)
  
  # Extract timespent using grep
  timespent=$(echo "$output" | grep -oP 'simulation took\s+(\d+\.\d+)\s+seconds')
  
  # Parse and append the output to CSV file
  echo "$grid_size,$threads,$timespent" >> $csv_file
}

# Create CSV file and write header
csv_file="scaling_weak_results.csv"
echo "Grid_Size,Num_Threads,Time_Spent" > $csv_file

# 1 64*64, 4 128*128, 16 256*256, 64 512*512 

# Weak comparison: 1 thread 128 vs 4 thread 256
main_run 1 64 100 0.005 $csv_file
main_run 4 128 100 0.005 $csv_file
main_run 16 256 100 0.005 $csv_file
main_run 64 512 100 0.005 $csv_file

