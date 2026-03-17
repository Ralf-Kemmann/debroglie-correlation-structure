import numpy as np


def de_broglie_wavenumber(mass: np.ndarray, velocity: np.ndarray, hbar: float = 1.0) -> np.ndarray:
    """
    Minimal de Broglie-inspired wavenumber:
        k = p / hbar = m * v / hbar

    This is the 'de Broglie relation' part:
    it assigns a phase scale to matter degrees of freedom.
    """
    return (mass * velocity) / hbar


def generate_states(
    n: int,
    x_max: float = 10.0,
    mass_mean: float = 1.0,
    mass_std: float = 0.05,
    velocity_mean: float = 1.0,
    velocity_std: float = 0.05,
    seed: int | None = None,
) -> dict:
    """
    Generate a minimal ensemble of phase-defined states.

    Returns a dictionary with:
    - x: positions / labels used to evaluate phase
    - mass: masses of the states
    - velocity: velocities of the states
    - k: de Broglie wavenumbers
    - phase: complex phase factors exp(i k x)
    """
    rng = np.random.default_rng(seed)

    x = np.linspace(0.0, x_max, n)
    mass = rng.normal(loc=mass_mean, scale=mass_std, size=n)
    velocity = rng.normal(loc=velocity_mean, scale=velocity_std, size=n)

    # Keep values positive in this minimal model
    mass = np.clip(mass, 1e-6, None)
    velocity = np.clip(velocity, 1e-6, None)

    k = de_broglie_wavenumber(mass, velocity)
    phase = np.exp(1j * k * x)

    return {
        "x": x,
        "mass": mass,
        "velocity": velocity,
        "k": k,
        "phase": phase,
    }
