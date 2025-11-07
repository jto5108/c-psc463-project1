"""
main.py
--------
This script demonstrates the full data analysis pipeline for a PulseDB-inspired
divide-and-conquer clustering project. It includes:
    1. Synthetic data generation and normalization
    2. Hierarchical clustering (Divide & Conquer)
    3. Closest pair detection within clusters
    4. Maximum subarray (signal activation) analysis
    5. Visualization of signal pairs

Author: [Your Name]
Course: CPSC 463 - Project 1
"""

# === Import necessary modules from src directory ===
from src.dataloader import DataLoader            # Handles data loading and normalization
from src.cluster_dc import DivideConquerCluster  # Divide & Conquer clustering algorithm
from src.closest_pair import ClosestPair         # Finds closest pair in a cluster
from src.max_subarray import KadaneAnalyzer      # Implements Kadane’s algorithm for signal peaks
from src.visualization import Visualizer         # Plots pairs and results


# === Main execution block ===
if __name__ == "__main__":
    # --------------------------------------------------
    # STEP 1: Generate synthetic (toy) time-series data
    # --------------------------------------------------
    # We create N segments, each of given length, to simulate PulseDB signals.
    # In a real project, this can be replaced with PulseDB dataset extraction.
    segs = DataLoader.toy_data(n_segments=8, length=200)
    print(f"[INFO] Generated {len(segs)} synthetic signal segments.")

    # Normalize all signals to have zero mean and unit variance.
    segs = DataLoader.normalize_segments(segs)
    print("[INFO] Normalized signal segments for consistent comparison.\n")

    # --------------------------------------------------
    # STEP 2: Cluster the segments using Divide & Conquer
    # --------------------------------------------------
    # DivideConquerCluster splits the dataset recursively based on correlation distance
    # until cluster sizes fall below 'min_size' or 'max_depth' recursion limit.
    dc = DivideConquerCluster(metric="corr", min_size=2, max_depth=3)
    clusters = dc.fit(segs)
    print(f"[INFO] Clustering complete. Generated {len(clusters)} clusters.\n")

    # --------------------------------------------------
    # STEP 3: Identify closest pairs within each cluster
    # --------------------------------------------------
    # Using correlation distance, the ClosestPair class finds the two most similar
    # signals in each cluster — useful for identifying related or redundant signals.
    cp = ClosestPair(metric="corr")

    for idx, cl in enumerate(clusters):
        # find_closest_pair returns ((index1, index2), distance)
        (i, j), d = cp.find_closest_pair(cl)
        print(f"[RESULT] Cluster {idx}: Closest pair ({i}, {j}) with distance {d:.4f}")

        # Plot the closest pair for visual confirmation
        if i is not None and j is not None:
            Visualizer.plot_pair(cl[i], cl[j])

    print("\n[INFO] Closest-pair visualization complete.\n")

    # --------------------------------------------------
    # STEP 4: Analyze activation windows using Kadane’s Algorithm
    # --------------------------------------------------
    # KadaneAnalyzer finds the contiguous subarray with the maximum sum —
    # useful for detecting high-activity regions in physiological signals.
    for k, s in enumerate(segs[:3]):  # Only process first 3 for demonstration
        val, st, en = KadaneAnalyzer.on_signal(s)
        print(f"[RESULT] Segment {k}: Max subarray sum = {val:.3f}, range = ({st}, {en})")

    print("\n[INFO] Kadane analysis complete. Pipeline finished successfully.")
