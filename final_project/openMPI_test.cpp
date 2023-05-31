#include <iostream>
#include <mpi.h>

int main(int argc, char** argv) {
    MPI_Init(&argc, &argv);

    int rank, size;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    if (size < 2) {
        std::cout << "This program requires at least 2 processes." << std::endl;
        MPI_Finalize();
        return 1;
    }

    if (rank == 0) {
        // Root process
        int n = 10;
        int* data = new int[n];
        for (int i = 0; i < n; ++i)
            data[i] = i;

        int blocklengths[2] = { 1, 2 };
        MPI_Aint displacements[2] = { 0, sizeof(int) };
        MPI_Datatype types[2] = { MPI_INT, MPI_INT };

        MPI_Datatype hvector_type;
        MPI_Type_create_hvector(2, 1, sizeof(int), MPI_INT, &hvector_type);
        MPI_Type_commit(&hvector_type);

        MPI_Request request;
        MPI_Isend(data, 1, hvector_type, 1, 0, MPI_COMM_WORLD, &request);

        // Simulate some work
        int totalIterations = 100000000;
        int percentIncrement = totalIterations / 100;
        for (int i = 0; i < totalIterations; ++i) {
            // Do some computation

            if (i % percentIncrement == 0) {
                int progress = (i / percentIncrement) + 1;
                std::cout << "Progress: " << progress << "%" << std::endl;
            }
        }

        // Cancel the communication
        MPI_Cancel(&request);
        MPI_Request_free(&request);

        delete[] data;
        MPI_Type_free(&hvector_type);
    }
    else if (rank == 1) {
        // Destination process
        int* received_data;
        MPI_Status status;

        MPI_Probe(0, 0, MPI_COMM_WORLD, &status);
        int count;
        MPI_Get_count(&status, MPI_INT, &count);
        received_data = new int[count];

        MPI_Recv(received_data, count, MPI_INT, 0, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);

        std::cout << "Received data: ";
        for (int i = 0; i < count; ++i)
            std::cout << received_data[i] << " ";
        std::cout << std::endl;

        delete[] received_data;
    }

    MPI_Finalize();
    return 0;
}

