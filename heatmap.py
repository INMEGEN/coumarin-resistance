import vcf
import pprint
import numpy as np
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

from scipy.cluster.hierarchy import dendrogram
from scipy.cluster.hierarchy import linkage

from sample_data import resistant, controls
from sample_jinx import jinx

samples = resistant + controls


keys = sorted(samples)
rows = []
for i in keys:
    col = []
    for j in keys:
        if i==j:
            inter = 1
        else:
            inter = jinx.get((i, j), jinx.get((j,i)))
        col.append(inter)
    rows.append(col)



rows = np.array( rows )
column_labels = keys
row_labels = keys
data = np.array( rows )
fig, ax = plt.subplots()
heatmap = ax.pcolor(data, cmap='summer', picker=True)
# Format
fig = plt.gcf()
fig.set_size_inches(16, 13)
# put the major ticks at the middle of each cell
ax.set_xticks(np.arange(data.shape[0])+0.5, minor=False)
ax.set_yticks(np.arange(data.shape[1])+0.5, minor=False)
# want a more natural, table-like display
ax.invert_yaxis()
ax.xaxis.tick_top()
ax.set_xticklabels(row_labels, minor=False, fontsize=8)
ax.set_yticklabels(column_labels, minor=False, fontsize=8)
# plt.show()
plt.xticks(rotation=90)
plt.colorbar(heatmap, orientation="vertical")
plt.savefig('heatmap.png')



algorythms = [ 'average',
               'complete',
               'ward',
               'centroid',
               'single',
               'weighted',]

for algorythm in algorythms:
    # plot dendrograms
    fig = plt.figure(figsize=(15,15))
    fig.add_subplot()
    linkage_matrix = linkage(rows, algorythm)
    a = dendrogram(linkage_matrix,
                   color_threshold=1,
                   labels=keys,
                   show_leaf_counts=False,
                   leaf_font_size=5,
                   leaf_rotation=0.0,
                   orientation='left',
    )
    plt.savefig('dendrogram_%s.svg' % algorythm)
    plt.close()
