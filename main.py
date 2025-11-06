from data_loader import DataLoader
from cluster_dc import DivideConquerCluster
from closest_pair import ClosestPairFinder
from max_subarray import MaxSubarray
from visualization import Visualizer


if __name__ == '__main__':
segs = DataLoader.toy_data(n_segments=8, length=200)
segs = DataLoader.normalize_segments(segs)


dc = DivideConquerCluster(metric='corr', min_size=2, max_depth=3)
clusters = dc.fit(segs)
print(f'Generated {len(clusters)} clusters')


cp = ClosestPairFinder(metric='corr')
for idx, cl in enumerate(clusters):
(i, j), d = cp.find_closest_pair(cl)
print(f'Cluster {idx}: Closest pair ({i}, {j}) with distance {d:.4f}')
if i is not None:
Visualizer.plot_pair(cl[i], cl[j])


for k, s in enumerate(segs[:3]):
val, st, en = MaxSubarray.on_signal(s)
print(f'Segment {k}: Max subarray sum {val:.3f}, range ({st}, {en})')
