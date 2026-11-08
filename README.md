# Quant Journey 2026-2030

## Quantitative Finance Portfolio

This repository documents a structured preparation path for graduate study in
financial engineering, with Baruch College MFE as a long-term target for
2030. It is an evidence-based learning portfolio, not a claim that any
admission requirement is guaranteed or permanently fixed.

## What is already demonstrated

- A reproducible NumPy Monte Carlo simulation with a convergence plot.
- A first AAPL moving-average backtest with documented look-ahead-bias
  handling.
- Formal coursework foundations in calculus, linear algebra, probability, and
  mathematical statistics.

## Featured projects

| Project | Evidence | Status |
|---|---|---|
| [Monte Carlo Basics](06_Projects/01_monte_carlo_basics/) | Runnable Python code, fixed seed, error report, convergence chart | Complete foundation |
| [Moving-Average Strategy](03_Strategies/) | Research notebook and strategy documentation | Baseline study |
| Option Pricing | Analytical and Monte Carlo pricing with validation | Next priority |
| Volatility Surface | Implied-volatility calibration and visualization | Later priority |
| C++ Pricing Engine | C++ implementation benchmarked against Python | Later priority |

## Portfolio standard

Every completed project must answer five questions:

1. What problem is being studied?
2. What mathematical model or trading rule is used?
3. Can another person run the code from a clean environment?
4. What result is produced, and how is it validated?
5. What are the assumptions, limitations, and possible sources of bias?

An item is not marked complete because a folder exists. It is complete only
when the code, documentation, result, and validation are present.

## Repository map

```text
01_Mathematics/             Mathematical foundations and implementations
02_Coding/                  Python, C++, and data-structures practice
03_Strategies/              Backtests and empirical research
04_Environment/             Portable environment and reproducibility
05_Notes/                   Dated learning records
06_Projects/                Structured quantitative-finance projects
07_Application/              Coursework, evidence, and application preparation
templates/                  Reusable project and report templates
```

## Four-year execution plan

### Stage 1 — Foundations

- [x] Set up Python, Jupyter, VS Code, and Git.
- [x] Build a first reproducible Monte Carlo experiment.
- [x] Build a first moving-average backtest.
- [ ] Record formal course evidence and English course descriptions.
- [ ] Learn C++ fundamentals and STL.
- [ ] Study data structures and algorithms.

### Stage 2 — Numerical and statistical computing

- [ ] Complete numerical methods exercises with code.
- [ ] Study stochastic processes.
- [ ] Implement Black-Scholes and binomial-tree pricing.
- [ ] Implement Monte Carlo option pricing and convergence tests.
- [ ] Add tested risk metrics and time-series analysis.

### Stage 3 — Research-quality projects

- [ ] Build and validate an implied-volatility surface.
- [ ] Compare Python and C++ implementations.
- [ ] Use proper train/test or in-sample/out-of-sample procedures.
- [ ] Complete a relevant research or industry internship.

### Stage 4 — Application preparation

- [ ] Re-check official requirements for the actual application year.
- [ ] Complete English-test and GRE/GMAT preparation if required.
- [ ] Select two or three strongest projects for the portfolio.
- [ ] Prepare an evidence-based CV, statement, and recommendation strategy.

## How to work on this repository

For every new project:

1. Copy [`templates/project_template/`](templates/project_template/).
2. Define the research question before writing the model.
3. Add a minimal runnable implementation first.
4. Add tests or analytical benchmarks.
5. Record a result with the exact command, data, seed, and date.
6. Document limitations and mark the project status honestly.
7. Commit one coherent milestone with a descriptive message.

## Run the current project

From the repository root:

```powershell
python 06_Projects/01_monte_carlo_basics/pi_estimation.py --samples 1000000 --seed 2026
```

The command prints the estimate, absolute error, and runtime, and generates a
convergence chart under `06_Projects/01_monte_carlo_basics/results/`.

## Important disclaimer

This is an educational research portfolio, not investment advice. Backtests
and simulated prices are sensitive to data quality, parameter selection,
execution assumptions, and market regime. Future admission policies and
program requirements must be verified from official sources in the relevant
application cycle.

---

Last updated: 2026-11-08
