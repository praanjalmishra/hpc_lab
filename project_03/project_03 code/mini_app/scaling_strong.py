# import pandas as pd
# import matplotlib.pyplot as plt

# # Read data from CSV file
# df = pd.read_csv("scaling_strong_results.csv")

# # Iterate over unique grid sizes
# grid_sizes = df["Grid_Size"].unique()
# for size in grid_sizes:
#     # Filter data for current grid size
#     df_size = df[df["Grid_Size"] == size]

#     # Extract number of threads and time spent
#     num_threads = df_size["Num_Threads"]
#     time_spent = df_size["Time_Spent"].str.extract(r'simulation took (\d+\.\d+) seconds').astype(float)

#     # Plot strong scaling
#     plt.plot(num_threads, time_spent, label=f"Grid Size {size}")

# # Set plot labels and legend
# plt.xlabel("Number of Threads")
# plt.ylabel("Time Spent (seconds)")
# plt.title("Strong Scaling")
# plt.legend()

# # Show plot
# plt.savefig('plot_test.png')

import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV file
df = pd.read_csv("scaling_strong_results.csv")

# Iterate over unique grid sizes
grid_sizes = [64, 128, 256, 512, 1024]
for size in grid_sizes:
    # Filter data for current grid size
    df_size = df[df["Grid_Size"] == size]

    # Extract number of threads and time spent
    num_threads = df_size["Num_Threads"]
    time_spent = df_size["Time_Spent"].str.extract(r'simulation took (\d+\.\d+) seconds').astype(float)

    # Plot strong scaling
    plt.plot(num_threads, time_spent, label=f"Grid Size {size}")

    # Set plot labels and legend
    plt.xlabel("Number of Threads")
    plt.ylabel("Time Spent (seconds)")
    plt.title(f"Strong Scaling for Grid Size {size}")
    plt.legend()
    plt.grid(True)

    # Save plot
    plt.savefig(f"strong_scaling_grid_{size}.png")

    # Clear plot for the next iteration
    plt.clf()

