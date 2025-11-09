## 🧩 src/data_loader.py
```python
import os
import numpy as np
from scipy.io import loadmat
import pandas as pd

class DataLoader:
    # Existing toy_data and normalize_segments functions here...

    @staticmethod
    def load_pulsedb(data_dir: str, signal_type: str = "ABP", limit: int = 1000):
        """
        Loads real PulseDB signals (.mat or .csv) into memory as time-series segments.
        
        Parameters
        ----------
        data_dir : str
            Path to the folder where PulseDB files are stored.
        signal_type : str
            One of ['ABP', 'ECG', 'PPG'].
        limit : int
            Number of segments to load.
        
        Returns
        -------
        list of np.ndarray
            List of time-series segments.
        """
        segments = []
        count = 0

        for file in os.listdir(data_dir):
            if count >= limit:
                break
            
            # Case 1: MATLAB .mat format
            if file.endswith(".mat"):
                mat = loadmat(os.path.join(data_dir, file))
                if signal_type in mat:
                    sig = np.array(mat[signal_type]).flatten()
                    segments.append(sig)
                    count += 1
            
            # Case 2: CSV format
            elif file.endswith(".csv"):
                df = pd.read_csv(os.path.join(data_dir, file))
                if signal_type in df.columns:
                    sig = df[signal_type].to_numpy()
                    segments.append(sig)
                    count += 1

        print(f"✅ Loaded {len(segments)} {signal_type} segments from {data_dir}")
        return segments
