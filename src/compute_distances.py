import numpy as np
from scipy.sparse.csgraph import shortest_path


def correlation_graph_distances(A: np.ndarray, eps: float = 1e-12) -> np.ndarray:
    """
    Derive effective relational distances from the weighted graph.

    Since strong correlation should correspond to short effective separation,
    we map edge weights to edge lengths via:

        L_ij = 1 / (A_ij + eps)

    Missing edges remain infinite.
    """
    L = np.full_like(A, np.inf, dtype=float)

    mask = A > 0.0
    L[mask] = 1.0 / (A[mask] + eps)

    np.fill_diagonal(L, 0.0)

    D = shortest_path(L, directed=False, unweighted=False)
    return D
