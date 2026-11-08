# Portfolio Completion Guide

This guide is the operating manual for completing the repository one milestone
at a time.

## The required evidence for a finished project

Each project should contain:

```text
project_name/
├── README.md
├── src/                 # Reusable implementation
├── notebooks/           # Exploration only
├── tests/               # Tests and validation
├── results/             # Small, reviewable figures or tables
└── requirements.txt     # Only if project-specific dependencies are needed
```

Do not commit downloaded market data, private credentials, generated caches,
or large binary files. Record the data source and the command needed to
download or regenerate data.

## Recommended completion sequence

### Milestone 1: Monte Carlo fundamentals

Current project: [`06_Projects/01_monte_carlo_basics/`](06_Projects/01_monte_carlo_basics/).

Required output:

- Reproducible simulation.
- Fixed seed.
- Absolute error.
- Convergence chart.
- Explanation of the `1 / sqrt(N)` error behavior.

### Milestone 2: Black-Scholes pricing

Create `06_Projects/02_option_pricing/`.

Required output:

- Black-Scholes call and put formulas.
- Greeks: delta, gamma, vega, theta, and rho.
- Unit tests against known values.
- A clear explanation of assumptions.

### Milestone 3: Monte Carlo option pricing

Create `06_Projects/03_monte_carlo_option_pricing/`.

Required output:

- Simulated geometric Brownian-motion paths.
- Discounted payoff estimate.
- Standard error and confidence interval.
- Convergence plot against the Black-Scholes analytical price.
- Discussion of discretization and sampling error.

### Milestone 4: Numerical methods

Create `06_Projects/04_numerical_methods/`.

Implement and test:

- Bisection and Newton methods.
- Numerical integration.
- Linear-system solution.
- At least one matrix factorization.

Apply one method to implied-volatility estimation.

### Milestone 5: Volatility surface

Create `06_Projects/05_volatility_surface/`.

Required output:

- Clean option data description.
- Implied-volatility solver.
- Maturity/strike interpolation.
- Surface plot.
- Arbitrage and extrapolation caveats.
- No invented market-data result.

### Milestone 6: C++ pricing engine

Create `06_Projects/06_cpp_pricing_engine/`.

Required output:

- C++ implementation of one pricing model.
- CMake build instructions.
- Tests or cross-checks against Python.
- Benchmark methodology.
- Honest performance comparison on the same machine.

The project should demonstrate clarity and correctness before adding
multithreading or advanced abstractions.

### Milestone 7: Strategy research

Improve [`03_Strategies/`](03_Strategies/) with:

- Transaction costs.
- Benchmark.
- Maximum drawdown and Sharpe ratio.
- Parameter-sensitivity analysis.
- Out-of-sample evaluation.
- Explicit protection against look-ahead and survivorship bias.

## Weekly workflow

1. Choose one bounded deliverable.
2. Read the relevant mathematical concept.
3. Implement the smallest correct version.
4. Validate it independently.
5. Write the result in English.
6. Commit the milestone.

## What counts as a strong result

A strong result is not the highest simulated return. It is a result that is:

- reproducible;
- mathematically explained;
- independently checked;
- honest about uncertainty;
- clear enough for another student to review.
