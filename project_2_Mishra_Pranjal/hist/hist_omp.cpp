#include "walltime.h"
#include <iostream>
#include <random>
#include <vector>
#include <omp.h>

#define VEC_SIZE 1000000000
#define BINS 16

int main() {
  double time_start, time_end;
  int nloops = 100;
  double time_av = 0.;
  
  // Initialize random number generator
  unsigned int seed = 123;
  float mean = BINS / 2.0;
  float sigma = BINS / 12.0;
  std::default_random_engine generator(seed);
  std::normal_distribution<float> distribution(mean, sigma);

  // Generate random sequence
  // Note: normal distribution is on interval [-inf; inf]
  //       we want [0; BINS-1]
  std::vector<int> vec(VEC_SIZE);
  for (long i = 0; i < VEC_SIZE; ++i) {
    vec[i] = int(distribution(generator));
    if (vec[i] < 0       ) vec[i] = 0;
    if (vec[i] > BINS - 1) vec[i] = BINS - 1;
  }
  
  long dist[BINS];
  for (int j = 1; j <= nloops; ++j){
    // Initialize histogram: Set all bins to zero
    long dist[BINS];
    for (int i = 0; i < BINS; ++i) {
      dist[i] = 0;
    } 

    // TODO Parallelize the histogram computation
    time_start = walltime();
    #pragma omp parallel shared(vec)
      {
        long dist_local[BINS];
        for(int i = 0; i < BINS; ++i) 
            dist_local[i] = 0;

        #pragma omp for
        for(long i = 0; i < VEC_SIZE; ++i) {
            dist_local[vec[i]]++;
        }

        #pragma omp critical
        for(int i = 0; i < BINS; ++i) {
            dist[i] += dist_local[i];
        }
      }
    time_end = walltime();
    double time = time_end - time_start;
    time_av = time_av*(j-1)/j + time/j;
  }
  // Write results
  for (int i = 0; i < BINS; ++i) {
    std::cout << "dist[" << i << "]=" << dist[i] << std::endl;
  }
  std::cout << "Time: " << time_av << " sec" << std::endl;
  
  for (int i = 0; i < BINS; ++i) {
    std::cout << dist[i] << ",";
  }
  int nthreads = omp_get_max_threads();
  std::cout << nthreads << "," << time_av << std::endl;
  return 0;
}
