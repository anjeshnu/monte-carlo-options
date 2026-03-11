# Monte Carlo Methods for Option Pricing

Monte Carlo simulation for European option pricing with multiple numerical schemes and variance reduction techniques.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 📋 Overview

Implementation of Monte Carlo methods for pricing European options under the Black-Scholes framework, comparing different numerical schemes and variance reduction techniques.

### Key Features

✅ **Multiple Schemes**: Euler, Milstein, Exact GBM simulation  
✅ **Variance Reduction**: Antithetic variates  
✅ **Validation**: Black-Scholes analytical comparison  
✅ **Analysis**: Bias, variance, efficiency testing  

## 🚀 Quick Start

```python
from src.monte_carlo import price_european_option

# Price call option
price, std_error = price_european_option(
    S0=100, K=100, T=1.0, r=0.05, sigma=0.2,
    option_type='call',
    n_simulations=100000,
    scheme='exact',
    antithetic=True
)

print(f"Call Price: ${price:.4f} ± ${std_error:.4f}")
```

## 📊 Numerical Schemes

### 1. Euler Scheme
```
S_{t+Δt} = S_t + r·S_t·Δt + σ·S_t·√Δt·Z
```
First-order accuracy, simple implementation.

### 2. Milstein Scheme  
```
S_{t+Δt} = S_t + r·S_t·Δt + σ·S_t·√Δt·Z + 0.5·σ²·S_t·Δt·(Z²-1)
```
Second-order accuracy, includes Itô correction.

### 3. Exact Simulation
```
S_T = S_0·exp((r - 0.5·σ²)·T + σ·√T·Z)
```
No discretization bias, most accurate for terminal payoffs.

## 🎲 Monte Carlo + Antithetic Variates

**Standard MC**: Use random draws Z  
**Antithetic**: Use both Z and -Z  

**Result**: ~50% variance reduction with minimal overhead

## 📈 Results

- **Exact + Antithetic**: Optimal for European options
- **Convergence**: SE ∝ 1/√N
- **Validation**: Matches Black-Scholes within confidence intervals

## 📁 Structure

```
monte-carlo-options/
├── examples/
│   ├── basic_pricing.py
│   └── scheme_comparison.py
├── notebooks/
│   └── monte_carlo_analysis.ipynb  # Complete analysis
├── src/
│   ├── option.py            # Parameters
│   ├── black_scholes.py     # Analytical pricing
│   ├── simulation.py        # GBM schemes
│   ├── monte_carlo.py       # MC pricer
│   ├── variance_reduction.py  # Effect of variance reduction techniques such as Antithetic
│   └── analysis.py            # Bias and Variance Analysis
├── README.md
└── requirements.txt

```

## 👤 Author

**Anjeshnu Trivedi**  
CQF Module 3 Examination Project

## 📄 License

MIT License - see [LICENSE](LICENSE)

---

⭐ Star this repository if helpful!
