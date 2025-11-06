import numpy as np
from utils import corr_distance, dtw_distance


class DivideConquerCluster:
def __init__(self, metric='corr', min_size=10, max_depth=5):
self.metric = metric
self.min_size = min_size
self.max_depth = max_depth
self.clusters = []


def _distance(self, a, b):
return dtw_distance(a, b) if self.metric == 'dtw' else corr_distance(a, b)


def _choose_seeds(self, segs):
best_i, best_j, best_d = 0, 1, -1
for i in range(len(segs)):
for j in range(i+1, len(segs)):
d = self._distance(segs[i], segs[j])
if d > best_d:
best_i, best_j, best_d = i, j, d
return best_i, best_j


def _split(self, segs):
i, j = self._choose_seeds(segs)
a, b = segs[i], segs[j]
cluster_A, cluster_B = [], []
for s in segs:
if self._distance(s, a) < self._distance(s, b):
cluster_A.append(s)
else:
cluster_B.append(s)
return cluster_A, cluster_B


def fit(self, segs):
def recurse(subset, depth):
if len(subset) <= self.min_size or depth >= self.max_depth:
self.clusters.append(subset)
return
A, B = self._split(subset)
if not A or not B:
self.clusters.append(subset)
return
recurse(A, depth+1)
recurse(B, depth+1)
recurse(segs, 0)
return self.clusters
