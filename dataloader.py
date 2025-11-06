## 🧩 src/data_loader.py
```python
import os
import numpy as np
import pandas as pd


class DataLoader:
def __init__(self, path=None):
self.path = path


def load_csv_folder(self, folder_path, max_segments=None):
segments = []
files = sorted([f for f in os.listdir(folder_path) if f.endswith('.csv')])
if max_segments:
files = files[:max_segments]
for f in files:
arr = pd.read_csv(os.path.join(folder_path, f), header=None).values.flatten()
segments.append(arr)
return segments


def load_from_single_csv(self, csv_path, max_segments=None):
df = pd.read_csv(csv_path, header=None)
if max_segments:
df = df.iloc[:max_segments]
return [row.values.astype(float) for _, row in df.iterrows()]


@staticmethod
def normalize_segments(segments):
normed = []
for s in segments:
mu, sigma = np.mean(s), np.std(s)
normed.append((s - mu) / sigma if sigma != 0 else np.zeros_like(s))
return normed


@staticmethod
def toy_data(n_segments=4, length=100, seed=0):
np.random.seed(seed)
t = np.linspace(0, 2 * np.pi, length)
segs = []
for i in range(n_segments):
amp = np.random.uniform(0.5, 1.5)
phase = np.random.uniform(0, 2*np.pi)
noise = np.random.normal(0, 0.1, length)
seg = amp * np.sin(t + phase) + noise
segs.append(seg)
return segs
