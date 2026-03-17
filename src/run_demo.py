import numpy as np
import matplotlib.pyplot as plt

from generate_states import generate_states
from correlation_matrix import correlation_matrix_from_phases
from build_graph import knn_graph_from_correlation
from compute_distances import correlation_graph_distances


def main() -> None:
    # 1) Generate phase-defined states from a de Broglie-inspired relation
    data = generate_states(
        n=80,
        x_max=12.0,
        mass_mean=1.0,
        mass_std=0.08,
        velocity_mean=1.0,
        velocity_std=0.08,
        seed=42,
    )

    # 2) Interference-induced correlation matrix
    G = correlation_matrix_from_phases(data["phase"], sigma=0.35)

    # 3) Graph extraction from strong correlations
    A = knn_graph_from_correlation(G, k=6, symmetrize=True)

    # 4) Derived relational distances
    D = correlation_graph_distances(A)

    # Basic diagnostics
    finite_distances = D[np.isfinite(D) & (D > 0)]
    print("Number of states:", len(data["x"]))
    print("Mean correlation:", G.mean())
    print("Graph density:", np.count_nonzero(A) / A.size)
    if finite_distances.size > 0:
        print("Mean finite relational distance:", finite_distances.mean())
    else:
        print("No finite relational distances found.")

    # Minimal plots
    fig, axes = plt.subplots(1, 3, figsize=(14, 4))

    im0 = axes[0].imshow(G, origin="lower", aspect="auto")
    axes[0].set_title("Correlation matrix $G_{ij}$")
    plt.colorbar(im0, ax=axes[0], fraction=0.046, pad=0.04)

    im1 = axes[1].imshow(A, origin="lower", aspect="auto")
    axes[1].set_title("Correlation graph adjacency")
    plt.colorbar(im1, ax=axes[1], fraction=0.046, pad=0.04)

    im2 = axes[2].imshow(D, origin="lower", aspect="auto")
    axes[2].set_title("Derived relational distances")
    plt.colorbar(im2, ax=axes[2], fraction=0.046, pad=0.04)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
