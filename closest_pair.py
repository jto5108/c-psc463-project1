from utils import dtw_distance, corr_distance


class ClosestPairFinder:
def __init__(self, metric='corr'):
self.metric = metric


def _distance(self, a, b):
return dtw_distance(a, b) if self.metric == 'dtw' else corr_distance(a, b)


def find_closest_pair(self, segs):
best = (None, None)
best_d = float('inf')
for i in range(len(segs)):
for j in range(i+1, len(segs)):
d = self._distance(segs[i], segs[j])
if d < best_d:
best = (i, j)
best_d = d
return best, best_d
