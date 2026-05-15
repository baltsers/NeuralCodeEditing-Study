import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
def plot_examples(colormaps):
    """
    Helper function to plot data with associated colormap.
    """
    #np.random.seed(19680801)
    #data = np.random.randn(2, 20)
    data=[[3.66,3.16,3.33,3.5,3.33,2.83,3.33,3.16,2.66,3.16,3,2.83,3.16,3.33,2.83,2.83,1.83,2,3,3.16],[3.16,3.66,3.16,3,3,3,2.66,3,3.33,3.33,3.16,3.5,3.33,1.66,3,3,2.33,3.16,3,3.5]]
    n = len(colormaps)
    fig, axs = plt.subplots(1, n, figsize=(n * 2 + 2, 3),
                            constrained_layout=True, squeeze=False)
    for [ax, cmap] in zip(axs.flat, colormaps):
        psm = ax.pcolormesh(data, cmap=cmap, rasterized=True, vmin=1, vmax=4)
        fig.colorbar(psm, ax=ax)
    plt.show()

viridis = cm.get_cmap('viridis', 256)
plot_examples([viridis])

