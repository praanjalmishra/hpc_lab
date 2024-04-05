import numpy as np
import matplotlib.pyplot as plt

# Execution times for OpenMP implementation
t_omp = np.array([382.479, 175.568, 190.889 , 154.987, 76.0977, 35.3486])

# Number of threads
threads = np.array([1, 2, 4, 8, 16, 32])

# for the sequential implementation
t_seq = 331.241

# Calculate speedup
S = t_seq / t_omp

# Calculate ideal speedup
S_ideal = t_seq / (t_seq / threads)

plt.figure(dpi=200)
plt.title("Parallel Speedup")
plt.xlabel("Number of Threads")
plt.ylabel("Speedup")
plt.grid()
plt.plot(threads, S, marker="o", linestyle='-', label="OMP Parallel")  
plt.plot(threads, S_ideal, marker="x", linestyle='--', label="Ideal")  
plt.legend()
plt.show()

plt.savefig('mandel_speedup.png')
