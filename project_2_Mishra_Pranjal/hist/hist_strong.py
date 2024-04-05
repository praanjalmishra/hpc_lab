import numpy as np
import matplotlib.pyplot as plt

# Execution times for OpenMP implementation
t_omp = np.array([0.70271, 0.41101 , 0.216416, 0.207817, 0.198355, 0.1993, 0.187701])

# Number of threads using
threads = np.array([1, 2, 4, 8, 12, 16, 32])

# Result for the sequential implementation (without OpenMP)
t_seq = 2.21554

# Calculate speedup
S = t_seq / t_omp

# Calculate ideal speedup
S_ideal = t_seq / (t_seq / threads)

# plot the Speed up
plt.figure(dpi=200)
plt.title("Parallel Speedup")
plt.xlabel("Number of Threads")
plt.ylabel("Speedup")
plt.grid()
plt.plot(threads, S, marker="o", linestyle='-', label="OMP Parallel")  # Using circle marker
plt.plot(threads, S_ideal, marker="x", linestyle='--', label="Ideal")  # Using cross marker
plt.legend()
plt.show()

plt.savefig('hist_speedup.png')
