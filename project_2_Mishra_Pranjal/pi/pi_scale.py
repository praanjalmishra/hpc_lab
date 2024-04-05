import argparse
import subprocess
import matplotlib.pyplot as plt


def run(type: str, n: int, n_threads: int) -> float:

    output = subprocess.check_output(
        [f"./build/{type}", str(n)],
        env={"OMP_NUM_THREADS": str(n_threads)}
    ).decode("utf-8")


    time = float(output.split()[-2])

    return time


def run_weak_scaling(type: str, n_per_processor: int, n_threads: int) -> float:
    return run(type, n_per_processor * n_threads, n_threads)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='Scaling Benchmark')
    parser.add_argument(
        '-t', '--max_threads',
        type=int,
        default=8,
        help='Maximum number of threads'
    )
    parser.add_argument(
        '-n',
        '--problem_size',
        type=int,
        default=1000000,
        help='Problem size'
    )
    parser.add_argument(
        '-m',
        '--problem_pp',
        type=int,
        default=100000,
        help='Problem size per Processor'
    )
    args = parser.parse_args()

    # run the benchmark for each type and number of iterations
    types = ["pi_serial", "pi_omp_critical", "pi_omp_reduction"]
    threads = list(range(1, args.max_threads + 1))

    # Strong scaling plots
    plt.figure(figsize=(8, 6))
    plt.title("Strong Scaling")
    plt.xlabel("Threads")
    plt.ylabel("Speedup")
    plt.grid(True)

    # run strong scaling for "critical" and "reduction"
    for type in ["pi_omp_critical", "pi_omp_reduction"]:
        times_strong = []
        for n_threads in threads:
            times_strong.append(run(type, args.problem_size, n_threads))

        speedup = [times_strong[0] / t for t in times_strong]
        plt.plot(threads, speedup, label=type, linewidth=1)

    # Add the ideal line
    ideal_line = [t for t in threads]
    plt.plot(threads, ideal_line, color='green', linestyle='-', label='Ideal')

    plt.legend()
    plt.savefig("strong_scaling.png")
    plt.close()

    # Weak scaling plots
    plt.figure(figsize=(8, 6))
    plt.title("Weak Scaling")
    plt.xlabel("Threads")
    plt.ylabel("Efficiency")
    plt.grid(True)

    # run weak scaling for "critical" and "reduction"
    for type in ["pi_omp_critical", "pi_omp_reduction"]:
        times_weak = []
        for n_threads in threads:
            if type == "pi_serial":
                times_weak.append(run_weak_scaling(type, args.problem_pp, 1))
            else:
                times_weak.append(run_weak_scaling(
                    type, args.problem_pp, n_threads))

        efficiency = [times_weak[0] / (t * n) for t, n in zip(times_weak, threads)]
        plt.plot(threads, efficiency, label=type, linewidth=1)

    # Add the ideal line
    ideal_line = [1 for _ in threads]
    plt.plot(threads, ideal_line, color='green', linestyle='-', label='Ideal')

    plt.legend()
    plt.savefig("weak_scaling.png")
    plt.close()

