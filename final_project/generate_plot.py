import matplotlib.pyplot as plt

# Simulation times for Cray_MPI and Open_MPI
cray_mpi_times = [19.8186, 10.4617, 5.56455, 3.34263, 2.08336, 1.45703, 10.5582, 3.41084, 2.11613, 1.54180, 5.65552, 5.67415, 3.41242, 2.10714, 1.57215, 3.49361, 2.09707, 1.51649, 2.17034, 1.49730, 1.53499]
open_mpi_times = [26.2657, 15.1193, 8.36371, 5.67561, 4.05356, 4.14757, 19.3273, 5.74797, 3.59659, 3.20662, 8.09556, 8.55707, 5.45970, 3.30551, 3.60205, 5.09247, 4.13643, 2.94228, 3.79584, 2.98757, 2.73155]

# Number of nodes and cores
nodes = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 4, 4, 4, 4, 8, 8, 8, 16, 16, 32]
cores_per_node = [1, 2, 4, 8, 16, 32, 1, 4, 8, 16, 2, 1, 2, 4, 1, 2, 4, 1, 2, 1]

# Create a dictionary to store the data points for each number of nodes
data_points = {}
for node, core, cray_mpi_time, open_mpi_time in zip(nodes, cores_per_node, cray_mpi_times, open_mpi_times):
    if node not in data_points:
        data_points[node] = []
    data_points[node].append((core, cray_mpi_time, open_mpi_time))

# Scatter Plot
plt.figure(figsize=(10, 5))

for node, points in data_points.items():
    cores, cray_mpi_times, open_mpi_times = zip(*points)
    plt.scatter([node] * len(cores), cray_mpi_times, marker='o', label=f'Cray_MPI ({node} nodes)', color='blue')
    plt.scatter([node] * len(cores), open_mpi_times, marker='^', label=f'Open_MPI ({node} nodes)', color='red')

plt.xlabel('Number of Nodes')
plt.ylabel('Simulation Time (sec)')
plt.title('Simulation Time vs Number of Nodes')
plt.legend()
plt.grid(True)
plt.savefig('scatter_plot.png')
