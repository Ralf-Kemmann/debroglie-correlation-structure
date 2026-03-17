import numpy as np


def knn_graph_from_correlation(G: np.ndarray, k: int = 5, symmetrize: bool = True) -> np.ndarray:
    """
    Construct a k-nearest-neighbor graph from the correlation matrix.

    Large G_ij means strong relational proximity in the operational sense.

    Returns an adjacency matrix A with weighted edges copied from G.
    """
    if k < 1:
        raise ValueError("k must be at least 1")

    n = G.shape[0]
    A = np.zeros_like(G)

    for i in range(n):
        # Exclude self
        idx = np.argsort(G[i])[-(k + 1):]
        idx = idx[idx != i]

        for j in idx:
            A[i, j] = G[i, j]

    if symmetrize:
        A = np.maximum(A, A.T)

    return A
