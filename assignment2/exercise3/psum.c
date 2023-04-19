#include <stdlib.h>
#include <omp.h>
#include <stdio.h>
#include <math.h>

void generate_random(double *input, size_t size)
{
    for (size_t i = 0; i < size; i++)
    {
        input[i] = rand() / (double)(RAND_MAX);
    }
}

double serial_sum(double *x, size_t size)
{
    double sum_val = 0.0;

    for (size_t i = 0; i < size; i++)
    {
        sum_val += x[i];
    }

    return sum_val;
}

double omp_sum(double *x, size_t size)
{
    double sum_val = 0.0;
    #pragma omp parallel for
    for (size_t i = 0; i < size; i++)
    {
        sum_val += x[i];
    }

    return sum_val;
}

double omp_critical_sum(double *x, size_t size)
{
    double sum_val = 0.0;
    #pragma omp parallel for
    for (size_t i = 0; i < size; i++)
    {
        #pragma omp critical
        {
            sum_val += x[i];
        }
    }

    return sum_val;
}

double omp_local_sum(double *x, size_t size, int threads)
{
    double local_sum[threads];
    #pragma omp parallel for
    for (size_t i = 0; i < size; i++)
    {
        local_sum[omp_get_thread_num()] += x[i];
    }

    double sum_val = 0.0;
    for (size_t i = 0; i < threads; i++)
    {
        sum_val += local_sum[i];
    }
    return sum_val;
}

// Ensure that each thread accesses a different cache line – Padding
double omp_local_sum_padding(double *x, size_t size, int threads)
{
    double local_sum[threads][64];
    #pragma omp parallel for
    for (size_t i = 0; i < size; i++)
    {
        local_sum[omp_get_thread_num()][0] += x[i];
    }

    double sum_val = 0.0;
    for (size_t i = 0; i < threads; i++)
    {
        sum_val += local_sum[i][0];
    }
    return sum_val;
}

void test(int mode, int threads)
{
    omp_set_num_threads(threads);
    // size 10**7
    size_t size = 10000000;

    // allocate memory
    double *input = (double *)malloc(size * sizeof(double));

    // Time
    double sum = 0.0;
    double sum2 = 0.0;

    for (int i = 0; i < 10; i++)
    {
        // generate random numbers
        generate_random(input, size);

        // serial sum
        double start = omp_get_wtime();
        double serial_sum_val = 0.0;

        if (mode == 0)
            serial_sum_val = serial_sum(input, size);
        else if (mode == 1)
            serial_sum_val = omp_sum(input, size);
        else if (mode == 2)
            serial_sum_val = omp_critical_sum(input, size);
        else if (mode == 3)
            serial_sum_val = omp_local_sum(input, size, threads);
        else if (mode == 4)
            serial_sum_val = omp_local_sum_padding(input, size, threads);

        double end = omp_get_wtime();

        // time
        double time_taken = end - start;
        sum += time_taken;
        sum2 += time_taken * time_taken;
    }

    // average time
    sum /= 10.0;
    sum2 /= 10.0;

    // standard deviation
    double std = sum2 - sum * sum;
    std = sqrt(std);

    char mode_name[5][20] = {"serial  ", "parallel", "critical", "local   ", "padding "};


    printf("%d, %s, %f, %f\n", threads, mode_name[mode], sum, std);

    // free memory
    free(input);
}

int main(int argc, char **argv)
{
    printf("\033[H\033[J");
    printf("threads, mode, average_time, standard_deviation\n");

    int threads[] = { 1, 2, 4, 8, 16, 20, 24, 28, 32, 64, 128};

    for (int t = 0; t < 11; t++)    
        for (int i = 0; i <= 4; i++)
            test(i, threads[t]);
}
