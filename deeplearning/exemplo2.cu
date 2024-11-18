#include <stdio.h>
#include <iostream>

// Número de elementos em cada vetor
#define N 2048 * 2048 

__global__ void my_kernel(int * a, int * b, int * c)
{
    // Determina a identificação de thread global exclusiva, por isso sabemos qual elemento processar
    int tid = blockIdx.x * blockDim.x + threadIdx.x;
    
    if ( tid < N ) // Certifique-se de que não inicializamos mais threads do que o necessário
        c[tid] = a[tid] + b[tid];
}

void report_gpu_mem()
{
    size_t free, total;
    cudaMemGetInfo(&free, &total);
    std::cout << "Free = " << free << " Total = " << total <<std::endl;
}

int main()
{
    int *a, *b, *c;

    // Número total de bytes por vetor
    int size = N * sizeof (int); 

    // Aloca memória sem a necessidade de usar cudaMemcpy
    cudaMallocManaged(&a, size);
    cudaMallocManaged(&b, size);
    cudaMallocManaged(&c, size);

    // Inicializa memória
    for( int i = 0; i < N; ++i )
    {
        a[i] = i;
        b[i] = i;
        c[i] = 0;
    }

    int threads_per_block = 128;
    int number_of_blocks = (N / threads_per_block) + 1;

    my_kernel <<< number_of_blocks, threads_per_block >>> ( a, b, c );

    // Espera até a GPU finalizar
    cudaDeviceSynchronize(); 

    // Imprime os últimos 5 valores de c 
    for( int i = N-5; i < N; ++i )
        printf("c[%d] = %d, ", i, c[i]);
    printf ("\n");

    // Libera toda a nossa memória alocada
    report_gpu_mem();
    cudaFree( a );
    report_gpu_mem(); 
    cudaFree( b );
    report_gpu_mem(); 
    cudaFree( c );
    report_gpu_mem();
}