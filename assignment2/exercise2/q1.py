

# Thread Count 1
# raw data
"""
Function	Best Rate MB/s	Avg time	Min time	Max time
Copy:	16271.6	0.009915	0.009833	0.01001
Scale:	13421.5	0.012008	0.011921	0.012083
Add:	15498.8	0.015541	0.015485	0.015605
Triad:	15368	0.015679	0.015617	0.0157
				
Function	Best Rate MB/s	Avg time	Min time	Max time
Copy:	16554.6	0.00976	    0.009665	0.009821
Scale:	13113.6	0.012243	0.012201	0.01231
Add:	15459.8	0.015574	0.015524	0.015647
Triad:	15470	0.015774	0.015514	0.01584
				
Function	Best Rate MB/s	Avg time	Min time	Max time
Copy:	14128.2	0.011637	0.011325	0.011988
Scale:	11600.9	0.014103	0.013792	0.014575
Add:	13851.2	0.017674	0.017327	0.018197
Triad:	13417.7	0.018293	0.017887	0.018769
				
Function	Best Rate MB/s	Avg time	Min time	Max time
Copy:	14904.5	0.014633	0.010735	0.016394
Scale:	12241	0.017445	0.013071	0.01986
Add:	13431.1	0.023967	0.017869	0.027409
Triad:	13391.2	0.024035	0.017922	0.027423
				
Function	Best Rate MB/s	Avg time	Min time	Max time
Copy:	15328.7	0.014375	0.010438	0.016276
Scale:	11913.7	0.017579	0.01343	    0.020153
Add:	13435.6	0.023964	0.017863	0.027699
Triad:	13769.3	0.023582	0.01743	    0.027127
"""
TC1_copy = [16271.6, 16554.6, 14128.2, 14904.5, 15328.7]
TC1_scale = [13421.5, 13113.6, 11600.9, 12241.0, 11913.7]
TC1_add = [15498.8, 15459.8, 13851.2, 13431.1, 13435.6]
TC1_triad = [15368.0, 15470.0, 13417.7, 13391.2, 13769.3]

TC1_avg_time_copy = [0.009915, 0.00976, 0.011637, 0.014633, 0.014375]
TC1_avg_time_scale = [0.012008, 0.012243, 0.014103, 0.017445, 0.017579]
TC1_avg_time_add = [0.015541, 0.015574, 0.017674, 0.023967, 0.023964]
TC1_avg_time_triad = [0.015679, 0.015774, 0.018293, 0.024035, 0.023582]


# Thread Count 32 
# raw data

"""
Function	Best Rate MB/s	Avg time	Min time	Max time
Copy:	55595.1	0.004208	0.002878	0.008747
Scale:	46567.8	0.005013	0.003436	0.007499
Add:	45977.6	0.006296	0.00522	0.007095
Triad:	42950.6	0.00623	0.005588	0.007539
				
Function	Best Rate MB/s	Avg time	Min time	Max time
Copy:	43873.5	0.005369	0.003647	0.007942
Scale:	37278.6	0.005757	0.004292	0.007154
Add:	54225	0.005931	0.004426	0.006409
Triad:	54201.6	0.005367	0.004428	0.006402
				
Function	Best Rate MB/s	Avg time	Min time	Max time
Copy:	32732.8	0.0066	0.004888	0.008892
Scale:	56737.3	0.004269	0.00282	0.005024
Add:	45290.8	0.006485	0.005299	0.007125
Triad:	73193.7	0.005613	0.003279	0.007491
				
Function	Best Rate MB/s	Avg time	Min time	Max time
Copy:	51052.8	0.00579	0.003134	0.008352
Scale:	33733.2	0.005701	0.004743	0.007534
Add:	53607	0.006017	0.004477	0.006483
Triad:	51778.9	0.005317	0.004635	0.006098
				
Function	Best Rate MB/s	Avg time	Min time	Max time
Copy:	38050	0.005966	0.004205	0.007347
Scale:	111960.1	0.004035	0.001429	0.005397
Add:	132451.7	0.005603	0.001812	0.006551
Triad:	77642.3	0.00535	0.003091	0.006709
"""

TC32_copy = [55595.1, 43873.5, 32732.8, 51052.8, 38050.0]
TC32_scale = [46567.8, 37278.6, 56737.3, 33733.2, 111960.1]
TC32_add = [45977.6, 54225.0, 45290.8, 53607.0, 132451.7]
TC32_triad = [42950.6, 54201.6, 73193.7, 51778.9, 77642.3]

TC32_avg_time_copy = [0.004208, 0.005369, 0.0066, 0.00579, 0.005966]
TC32_avg_time_scale = [0.005013, 0.005757, 0.004269, 0.005701, 0.004035]
TC32_avg_time_add = [0.006296, 0.005931, 0.006485, 0.006017, 0.005603]
TC32_avg_time_triad = [0.00623, 0.005367, 0.005613, 0.005317, 0.00535]

# Thread Count 64
# raw data
"""
Function	Best Rate MB/s	Avg time	Min time	Max time
Copy:	13607.9	0.019645	0.011758	0.032003
Scale:	30681.1	0.015741	0.005215	0.024004
Add:	15750.1	0.018058	0.015238	0.031993
Triad:	20173.4	0.017368	0.011897	0.031997
				
Function	Best Rate MB/s	Avg time	Min time	Max time
Copy:	10289.5	0.022365	0.01555	0.031983
Scale:	31570.2	0.018562	0.005068	0.032008
Add:	53249.7	0.018769	0.004507	0.031999
Triad:	42067.5	0.018046	0.005705	0.032004
				
Function	Best Rate MB/s	Avg time	Min time	Max time
Copy:	28985	0.021306	0.00552	0.032018
Scale:	73055.6	0.016	0.00219	0.031987
Add:	140434.3	0.016805	0.001709	0.032014
Triad:	127583.4	0.015481	0.001881	0.031976
				
Function	Best Rate MB/s	Avg time	Min time	Max time
Copy:	29728.4	0.019802	0.005382	0.032006
Scale:	186880.7	0.018567	0.000856	0.031998
Add:	216433.7	0.016536	0.001109	0.032
Triad:	222854.3	0.013109	0.001077	0.031995
				
Function	Best Rate MB/s	Avg time	Min time	Max time
Copy:	10874.7	0.020214	0.014713	0.031998
Scale:	145068.9	0.016658	0.001103	0.03204
Add:	17904.9	0.01718	0.013404	0.028093
Triad:	119510	0.0156	0.002008	0.023864
"""

TC64_copy = [13607.9, 10289.5, 28985.0, 29728.4, 10874.7]
TC64_scale = [30681.1, 31570.2, 73055.6, 186880.7, 145068.9]
TC64_add = [15750.1, 53249.7, 140434.3, 216433.7, 17904.9]
TC64_triad = [20173.4, 42067.5, 127583.4, 222854.3, 119510.0]

TC64_avg_time_copy = [0.019645, 0.022365, 0.021306, 0.019802, 0.020214]
TC64_avg_time_scale = [0.015741, 0.018562, 0.016, 0.018567, 0.016658]
TC64_avg_time_add = [0.018058, 0.018769, 0.016805, 0.016536, 0.01718]
TC64_avg_time_triad = [0.017368, 0.018046, 0.015481, 0.013109, 0.0156]

# Thread Count 128
# raw data
"""
Function	Best Rate MB/s	Avg time	Min time	Max time
Copy:	4001.8	0.0504	0.039982	0.063863
Scale:	5689.1	0.03572	0.028124	0.056023
Add:	7503.5	0.041439	0.031985	0.067806
Triad:	8261.3	0.03733	0.029051	0.047968
				
Function	Best Rate MB/s	Avg time	Min time	Max time
Copy:	5847.1	0.04998	0.027364	0.076051
Scale:	4991.1	0.042931	0.032057	0.056014
Add:	6809.9	0.043998	0.035243	0.06401
Triad:	8757.5	0.04123	0.027405	0.064026
				
Function	Best Rate MB/s	Avg time	Min time	Max time
Copy:	5117.1	0.054902	0.031268	0.071985
Scale:	5697	0.036568	0.028085	0.05598
Add:	8560.8	0.046574	0.028035	0.067824
Triad:	6682.1	0.048972	0.035917	0.063861
				
Function	Best Rate MB/s	Avg time	Min time	Max time
Copy:	5000.3	0.052309	0.031998	0.067896
Scale:	4441.9	0.045473	0.036021	0.06798
Add:	8493.7	0.039177	0.028256	0.067732
Triad:	8612.3	0.040785	0.027867	0.059733
				
Function	Best Rate MB/s	Avg time	Min time	Max time
Copy:	4471.5	0.050854	0.035782	0.063906
Scale:	5714.5	0.047676	0.027999	0.071983
Add:	12366.7	0.044392	0.019407	0.059988
Triad:	79387.5	0.040887	0.003023	0.063992
"""

TC128_copy = [4001.8, 5847.1, 5117.1, 5000.3, 4471.5]
TC128_scale = [5689.1, 4991.1, 5697.0, 4441.9, 5714.5]
TC128_add = [7503.5, 6809.9, 8560.8, 8493.7, 12366.7]
TC128_triad = [8261.3, 8757.5, 6682.1, 8612.3, 79387.5]

TC128_avg_time_copy = [0.0504, 0.04998, 0.054902, 0.052309, 0.050854]
TC128_avg_time_scale = [0.03572, 0.042931, 0.036568, 0.045473, 0.047676]
TC128_avg_time_add = [0.041439, 0.043998, 0.046574, 0.039177, 0.044392]
TC128_avg_time_triad = [0.03733, 0.04123, 0.048972, 0.040785, 0.040887]

import numpy as np


threads = [1, 32, 64, 128]
copy_data = np.array([TC1_copy, TC32_copy, TC64_copy, TC128_copy])
scale_data = np.array([TC1_scale, TC32_scale, TC64_scale, TC128_scale])
add_data = np.array([TC1_add, TC32_add, TC64_add, TC128_add])
triad_data = np.array([TC1_triad, TC32_triad, TC64_triad, TC128_triad])

# Calculate the mean and standard deviation of the bandwidth for each benchmark and each number of threads
copy_mean = np.mean(copy_data, axis=1)
copy_std = np.std(copy_data, axis=1)
scale_mean = np.mean(scale_data, axis=1)
scale_std = np.std(scale_data, axis=1)
add_mean = np.mean(add_data, axis=1)
add_std = np.std(add_data, axis=1)
triad_mean = np.mean(triad_data, axis=1)
triad_std = np.std(triad_data, axis=1)

import matplotlib.pyplot as plt

# Define the figure and subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 8), sharex=True)

# I hope that this is correct.. :c
axs[0, 0].errorbar(threads, copy_mean, yerr=copy_std, fmt='o-', capsize=5)
axs[0, 0].set_title('Copy')

axs[0, 1].errorbar(threads, scale_mean, yerr=scale_std, fmt='o-', capsize=5)
axs[0, 1].set_title('Scale')

axs[1, 0].errorbar(threads, add_mean, yerr=add_std, fmt='o-', capsize=5)
axs[1, 0].set_title('Add')

axs[1, 1].errorbar(threads, triad_mean, yerr=triad_std, fmt='o-', capsize=5)
axs[1, 1].set_title('Triad')

fig.text(0.5, 0.04, 'Number of Threads', ha='center', fontsize=14)
fig.text(0.04, 0.5, 'Bandwidth (MB/s)', va='center', rotation='vertical', fontsize=14)
fig.suptitle('Benchmark Results with Error Bars', fontsize=16)
plt.savefig('benchmark_results.png')