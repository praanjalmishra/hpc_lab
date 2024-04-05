import numpy as np
import matplotlib.pyplot as plt


t_omp_1 = [2.272308, 1.195870, 0.6430716, 0.4886622, 0.6920988, 1.066829]
# for size = 20000000
t_omp_2 = [4.87415, 2.482233, 1.312577, 0.9441289, 1.178456, 1.609801]
# for size = 40000000
t_omp_3 = [10.36749, 4.345547, 2.527655, 1.746379, 2.408726, 3.447392]
# for size = 80000000
t_omp_4 = [21.71861, 8.065011, 5.519126, 3.916089, 4.370055, 6.043425]
# for size = 160000000
t_omp_5 = [45.50376, 14.68840, 10.21596, 7.003359, 8.572749, 9.756872]


# Problem Size:
size = [10000000, 20000000, 40000000, 80000000, 160000000]

# Number of threads using 1, 2, 4 ....
threads = [1, 2, 4, 8, 16, 32]


t_seq = [2.147488, 4.537938, 9.431349, 19.64259, 41.11775, 87.35383]


S_1 = []
S_2 = []
S_3 = []
S_4 = []
S_5 = []


S_1 = [t_seq[0] / t_omp_1[i] for i in range(len(threads))]
S_2 = [t_seq[1] / t_omp_2[i] for i in range(len(threads))]
S_3 = [t_seq[2] / t_omp_3[i] for i in range(len(threads))]
S_4 = [t_seq[3] / t_omp_4[i] for i in range(len(threads))]
S_5 = [t_seq[4] / t_omp_5[i] for i in range(len(threads))]

S_ideal = []

for i in range(len(threads)):
    S_ideal.append( t_seq[0] / (t_seq[0] / threads[i]))


# plot the Speed up
plt.figure(dpi=200)
plt.title("Parallel Speedup")
plt.xlabel("Number of Threads")
plt.ylabel("Speedup")
plt.grid()
plt.plot(threads, S_ideal, marker="^", linestyle='--', label="ideal")
plt.plot(threads, S_1, marker="o", label="omp result: 10M")
plt.plot(threads, S_2, marker="o", label="omp result: 20M")
plt.plot(threads, S_3, marker="o", label="omp result: 40M")
plt.plot(threads, S_4, marker="o", label="omp result: 80M")
plt.plot(threads, S_5, marker="o", label="omp result: 160M")
plt.legend()

plt.savefig('qicksort_speedup_plot.png')