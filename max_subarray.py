import numpy as np


class MaxSubarray:
@staticmethod
def kadane(arr):
max_sum = curr = arr[0]
start = end = s = 0
for i in range(1, len(arr)):
if arr[i] > curr + arr[i]:
curr = arr[i]
s = i
else:
curr += arr[i]
if curr > max_sum:
max_sum, start, end = curr, s, i
return max_sum, start, end


@staticmethod
def on_signal(seg):
diff = np.abs(np.diff(seg))
return MaxSubarray.kadane(diff)
