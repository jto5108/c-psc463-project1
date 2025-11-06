from src.data_loader import DataLoader
from src.cluster_dc import DivideConquerCluster
from src.closest_pair import ClosestPairFinder
from src.max_subarray import MaxSubarray


def test_pipeline():
segs = DataLoader.toy_data(6, 100)
segs = DataLoader.normalize_segments(segs)


dc = DivideConquerCluster(metric='corr', min_size=2)
clusters = dc.fit(segs)


cp = ClosestPairFinder(metric='corr')
for cl in clusters:
if len(cl) >= 2:
(i, j), d = cp.find_closest_pair(cl)
assert d >= 0


val, st, en = MaxSubarray.on_signal(segs[0])
assert st < en
