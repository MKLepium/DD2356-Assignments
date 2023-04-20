
"""
Static:

Function    Best Rate MB/s  Avg time     Min time     Max time
Copy:            5664.5     0.041381     0.028246     0.067527
Scale:           4994.7     0.040334     0.032034     0.051993
Add:             7523.8     0.037011     0.031899     0.044288
Triad:           7448.1     0.040827     0.032223     0.063712

Function    Best Rate MB/s  Avg time     Min time     Max time
Copy:            5707.2     0.039956     0.028035     0.059745
Scale:           4994.2     0.037801     0.032037     0.055764
Add:             7536.5     0.041709     0.031845     0.063893
Triad:           7424.8     0.038756     0.032324     0.052088

Function    Best Rate MB/s  Avg time     Min time     Max time
Copy:            4956.0     0.041827     0.032284     0.056003
Scale:           4461.8     0.040910     0.035860     0.055766
Add:             7479.4     0.042747     0.032088     0.059752
Triad:           7498.4     0.039850     0.032007     0.060005

Function    Best Rate MB/s  Avg time     Min time     Max time
Copy:            5013.7     0.040443     0.031913     0.055831
Scale:           4994.4     0.040412     0.032036     0.059999
Add:             7495.8     0.041872     0.032018     0.055873
Triad:           8653.9     0.043498     0.027733     0.075799

"""

static_best_rates_copy = [5664.5, 5707.2, 4956.0, 5013.7]
static_best_rates_scale = [4994.7, 4994.2, 4461.8, 4994.4]
static_best_rates_add = [7523.8, 7536.5, 7479.4, 7495.8]
static_best_rates_triad = [7448.1, 7424.8, 7498.4, 8653.9]

"""
Dynamic:

Dynamic:

Function    Best Rate MB/s  Avg time     Min time     Max time
Copy:             156.9     1.030060     1.019776     1.044005
Scale:           4987.1     0.042407     0.032083     0.064017
Add:             6787.7     0.042570     0.035358     0.068004
Triad:           8542.7     0.043188     0.028094     0.063939

Function    Best Rate MB/s  Avg time     Min time     Max time
Copy:             156.3     1.029706     1.023778     1.044000
Scale:           4425.4     0.048081     0.036155     0.063987
Add:             7527.1     0.043975     0.031885     0.056010
Triad:           7497.9     0.043571     0.032009     0.055892

Function    Best Rate MB/s  Avg time     Min time     Max time
Copy:             155.7     1.042552     1.027866     1.063899
Scale:           4969.1     0.049438     0.032199     0.080007
Add:             7401.0     0.047973     0.032428     0.071551
Triad:           7563.1     0.040893     0.031733     0.063901

Function    Best Rate MB/s  Avg time     Min time     Max time
Copy:             158.1     1.038163     1.012002     1.055832
Scale:           5001.3     0.047166     0.031992     0.079995
Add:             7473.1     0.044070     0.032115     0.072000
Triad:           7389.4     0.047560     0.032479     0.068016

Function    Best Rate MB/s  Avg time     Min time     Max time
Copy:             154.4     1.048429     1.035993     1.071863
Scale:           5000.9     0.045403     0.031994     0.063990
Add:             7526.8     0.044279     0.031886     0.072005
Triad:           8213.6     0.042777     0.029220     0.064025

"""

dynamic_best_rates_copy = [156.9, 156.3, 155.7, 158.1, 154.4]
dynamic_best_rates_scale = [4987.1, 4425.4, 4969.1, 5001.3, 5000.9]
dynamic_best_rates_add = [6787.7, 7527.1, 7401.0, 7473.1, 7526.8]
dynamic_best_rates_triad = [8542.7, 7497.9, 7563.1, 7389.4, 8213.6]


""" 
Guided:

Function    Best Rate MB/s  Avg time     Min time     Max time
Copy:            5001.4     0.050110     0.031991     0.075864
Scale:           4417.7     0.041475     0.036218     0.048003
Add:             8516.4     0.041133     0.028181     0.075905
Triad:           6694.4     0.045057     0.035851     0.059990

Function    Best Rate MB/s  Avg time     Min time     Max time
Copy:            4377.3     0.048410     0.036552     0.059896
Scale:           5620.1     0.042247     0.028469     0.055441
Add:             7424.8     0.042288     0.032324     0.063959
Triad:           6727.2     0.047025     0.035676     0.071998

Function    Best Rate MB/s  Avg time     Min time     Max time
Copy:            5000.9     0.046563     0.031994     0.068014
Scale:           4451.5     0.042021     0.035943     0.055998
Add:             8501.9     0.047853     0.028229     0.075890
Triad:           8375.2     0.050637     0.028656     0.067577

Function    Best Rate MB/s  Avg time     Min time     Max time
Copy:            5770.1     0.050327     0.027729     0.071992
Scale:           4968.2     0.044783     0.032205     0.075979
Add:             7194.9     0.041750     0.033357     0.047992
Triad:           7539.8     0.041762     0.031831     0.064000

Function    Best Rate MB/s  Avg time     Min time     Max time
Copy:            4463.0     0.053641     0.035850     0.075998
Scale:           4967.9     0.051198     0.032207     0.071994
Add:             9901.9     0.040848     0.024238     0.064015
Triad:           7463.0     0.040534     0.032159     0.055812
"""

guided_best_rates_copy = [5001.4, 4377.3, 5000.9, 5770.1, 4463.0]
guided_best_rates_scale = [4417.7, 5620.1, 4451.5, 4968.2, 4967.9]
guided_best_rates_add = [8516.4, 7424.8, 8501.9, 7194.9, 9901.9]
guided_best_rates_triad = [6694.4, 6727.2, 8375.2, 7539.8, 7463.0]


import numpy as np
# take average of best rates
static_best_rates_copy_avg = np.mean(static_best_rates_copy)
static_best_rates_scale_avg = np.mean(static_best_rates_scale)
static_best_rates_add_avg = np.mean(static_best_rates_add)
static_best_rates_triad_avg = np.mean(static_best_rates_triad)

dynamic_best_rates_copy_avg = np.mean(dynamic_best_rates_copy)
dynamic_best_rates_scale_avg = np.mean(dynamic_best_rates_scale)
dynamic_best_rates_add_avg = np.mean(dynamic_best_rates_add)
dynamic_best_rates_triad_avg = np.mean(dynamic_best_rates_triad)

guided_best_rates_copy_avg = np.mean(guided_best_rates_copy)
guided_best_rates_scale_avg = np.mean(guided_best_rates_scale)
guided_best_rates_add_avg = np.mean(guided_best_rates_add)
guided_best_rates_triad_avg = np.mean(guided_best_rates_triad)


# visualize
import matplotlib.pyplot as plt
import numpy as np

# data to plot
n_groups = 4
static = (static_best_rates_copy_avg, static_best_rates_scale_avg, static_best_rates_add_avg, static_best_rates_triad_avg)
dynamic = (dynamic_best_rates_copy_avg, dynamic_best_rates_scale_avg, dynamic_best_rates_add_avg, dynamic_best_rates_triad_avg)
guided = (guided_best_rates_copy_avg, guided_best_rates_scale_avg, guided_best_rates_add_avg, guided_best_rates_triad_avg)

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.25
opacity = 0.8

rects1 = plt.bar(index, static, bar_width,
alpha=opacity,
color='b',
label='Static')

rects2 = plt.bar(index + bar_width, dynamic, bar_width,
alpha=opacity,
color='g',
label='Dynamic')

rects3 = plt.bar(index + bar_width*2, guided, bar_width,
alpha=opacity,
color='r',
label='Guided')

plt.xlabel('Function')
plt.ylabel('Best Rate MB/s')
plt.title('Best Rate MB/s by Function')
plt.xticks(index + bar_width, ('Copy', 'Scale', 'Add', 'Triad'))
plt.legend()

plt.tight_layout()
plt.savefig('best_rates.png')