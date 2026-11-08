"""Estimate pi with a reproducible Monte Carlo experiment."""

from __future__ import annotations

import argparse
import time
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parent
RESULTS_DIR = ROOT / "results"


def estimate_pi(sample_sizes: np.ndarray, seed: int) -> np.ndarray:
    """Return pi estimates at each cumulative sample size."""
    rng = np.random.default_rng(seed)
    total_samples = int(sample_sizes[-1])
    points = rng.random((total_samples, 2))
    inside_flags = np.sum(points * points, axis=1) <= 1.0
    cumulative_inside = np.cumsum(inside_flags)
    return 4.0 * cumulative_inside[sample_sizes - 1] / sample_sizes


def plot_convergence(sample_sizes: np.ndarray, estimates: np.ndarray) -> Path:
    """Save and return the convergence chart path."""
    RESULTS_DIR.mkdir(exist_ok=True)
    output_path = RESULTS_DIR / "pi_convergence.png"
    figure, axis = plt.subplots(figsize=(8, 4.5))
    axis.plot(sample_sizes, estimates, marker="o", label="Monte Carlo estimate")
    axis.axhline(np.pi, color="tab:red", linestyle="--", label="pi")
    axis.set_xscale("log")
    axis.set_xlabel("Number of samples")
    axis.set_ylabel("Estimate")
    axis.set_title("Monte Carlo convergence toward pi")
    axis.grid(alpha=0.25)
    axis.legend()
    figure.tight_layout()
    figure.savefig(output_path, dpi=150)
    plt.close(figure)
    return output_path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--samples", type=int, default=1_000_000)
    parser.add_argument("--seed", type=int, default=2026)
    args = parser.parse_args()

    if args.samples < 100:
        parser.error("--samples must be at least 100")

    sample_sizes = np.unique(
        np.geomspace(100, args.samples, num=20).astype(int)
    )
    start = time.perf_counter()
    estimates = estimate_pi(sample_sizes, args.seed)
    elapsed = time.perf_counter() - start
    output_path = plot_convergence(sample_sizes, estimates)

    estimate = float(estimates[-1])
    print(f"samples: {args.samples:,}")
    print(f"seed: {args.seed}")
    print(f"pi estimate: {estimate:.6f}")
    print(f"absolute error: {abs(estimate - np.pi):.6f}")
    print(f"elapsed seconds: {elapsed:.3f}")
    print(f"plot: {output_path}")


if __name__ == "__main__":
    main()
