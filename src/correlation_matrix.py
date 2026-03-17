import numpy as np


def correlation_matrix_from_phases(
    phase: np.ndarray,
    sigma: float = 0.25,
) -> np.ndarray:
    """
    Build a correlation matrix from pairwise phase differences.

    Important conceptual distinction:
    - The de Broglie relation provides the phase structure.
    - Interference between these phases generates the correlations.

    We use a simple Gaussian coherence kernel on the phase difference:
        G_ij = exp( - (Delta phi_ij)^2 / (2 sigma^2) )

    where Delta phi_ij is the wrapped phase difference in [-pi, pi].

    This yields:
    - symmetry
    - bounded values in (0, 1]
    - maximal self-correlation on the diagonal
    """
    angles = np.angle(phase)
    delta = angles[:, None] - angles[None, :]

    # Wrap phase differences to [-pi, pi]
    delta_wrapped = np.angle(np.exp(1j * delta))

    G = np.exp(-(delta_wrapped ** 2) / (2.0 * sigma ** 2))

    # Numerical hygiene
    np.fill_diagonal(G, 1.0)

    return G
