import numpy as np
import perfplot

arr1=np.random.rand(20)
arr2=np.random.rand(20)

rest1 = np.c_[arr1, arr2]
rest2 = np.stack([arr1, arr2])
rest3 = np.vstack([arr1, arr2])
rest4 = np.column_stack([arr1, arr2])
rest5 = np.concatenate([arr1[:, None], arr2[:, None]], axis=1)

perfplot.show(
    setup=np.random.rand,
    kernels=[
        lambda a: np.c_[a,a],
        lambda a: np.stack([a,a]).T,
        lambda a: np.vstack([a, a]).T,
        lambda a: np.column_stack([a, a]),
        lambda a: np.concatenate([a[:, None], a[:, None]], axis=1)
    ],
    labels=['c_','stack','vstack','column stack', 'concate'],
    n_range=[2 ** k for k in range(15)],
    xlabel='len(a)'
)