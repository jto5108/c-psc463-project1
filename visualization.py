import matplotlib.pyplot as plt


class Visualizer:
@staticmethod
def plot_series(series_list, title='Cluster Overlay', max_n=10):
for s in series_list[:max_n]:
plt.plot(s, alpha=0.7)
plt.title(title)
plt.show()


@staticmethod
def plot_pair(a, b):
plt.plot(a, label='A')
plt.plot(b, label='B')
plt.legend()
plt.show()
