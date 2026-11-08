# Monte Carlo Basics: Estimating Pi

This small project introduces Monte Carlo simulation by estimating `pi` from
uniform random points sampled inside the unit square. Points inside the
quarter circle satisfy:

```text
x^2 + y^2 <= 1
```

The fraction of points inside the quarter circle estimates `pi / 4`.

## Run

From the repository root:

```powershell
python 06_Projects/01_monte_carlo_basics/pi_estimation.py --samples 1000000 --seed 2026
```

The script prints the estimate, absolute error, and runtime, and writes a
convergence chart to `06_Projects/01_monte_carlo_basics/results/pi_convergence.png`.

## Method

- Samples are generated with NumPy using a recorded random seed.
- The experiment reports the estimate for increasing sample sizes.
- The convergence chart compares the estimate with the true value of `pi`.
- A fixed seed makes the result reproducible; changing the seed is useful for
  examining Monte Carlo variability.

## Why this matters for quantitative finance

The same simulation pattern is used in option pricing, risk estimation, and
other numerical methods. This project is intentionally a small foundation, not
a financial pricing model. The next step is to reuse the simulation framework
for Black-Scholes Monte Carlo pricing and compare it with the analytical
solution.

## Limitations

Monte Carlo error decreases at a slow rate, approximately proportional to
`1 / sqrt(N)`. A close estimate with one seed is not evidence that a financial
model is correct; convergence, independent validation, and model assumptions
must also be examined.
