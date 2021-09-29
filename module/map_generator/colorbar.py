import numpy as np


def get_ticks_labels(data=None, tick=None, **text_kwargs):
    ticks = [i for i in range(int(np.min(data)), int(np.max(data)), tick)]
    labels = list(map(str, ticks))
    return ticks, labels