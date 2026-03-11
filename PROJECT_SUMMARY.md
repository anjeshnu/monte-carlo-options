# Monte Carlo Options Pricing - Project Summary

## Overview
Monte Carlo simulation framework for pricing European options using multiple numerical schemes and variance reduction techniques.

## What It Does
- Simulates stock price paths under Geometric Brownian Motion
- Prices European call and put options
- Compares different discretization schemes
- Applies variance reduction techniques
- Validates against Black-Scholes analytical solutions

## Key Features

### 1. Multiple Numerical Schemes
- **Euler**: Simple first-order scheme
- **Milstein**: Second-order with Itô correction
- **Exact**: Analytical GBM solution (no discretization error)

### 2. Variance Reduction
- **Antithetic Variates**: ~50% variance reduction
- Uses both Z and -Z random draws
- Doubles effective sample size

### 3. Comprehensive Analysis
- Bias-variance decomposition
- Convergence testing (N → ∞)
- Efficiency comparison
- Black-Scholes validation

### 4. Production-Ready Code
- Clean modular architecture
- Well-documented functions
- Type hints throughout
- Example scripts included

## Technical Implementation

### Core Components

**option.py** - Parameter classes
- OptionParameters dataclass
- SimulationParameters dataclass
- Input validation

**black_scholes.py** - Analytical pricing
- Call/put formulas
- Greeks (Delta, Gamma, Vega)
- Validation benchmark

**simulation.py** - GBM schemes
- Euler discretization
- Milstein scheme
- Exact simulation

**monte_carlo.py** - MC pricing engine
- Standard Monte Carlo
- Antithetic variates
- MonteCarloOptionPricer class

**analysis.py** - Testing tools
- Bias-variance analysis
- Convergence testing
- Performance metrics

**variance_reduction.py** - VR techniques
- Antithetic variates
- Efficiency calculations

## Results

### Accuracy
- Exact scheme: No discretization bias
- Matches Black-Scholes within confidence intervals
- Standard error ∝ 1/√N

### Efficiency
- Exact + Antithetic = optimal for European options
- ~50% variance reduction from antithetic variates
- 100k simulations sufficient for pricing

### Performance
- Fast NumPy vectorization
- <1 second for 100k paths
- Minimal overhead from variance reduction

## Use Cases

### Academic
- Teaching Monte Carlo methods
- Demonstrating numerical schemes
- Variance reduction techniques

### Professional
- Option pricing validation
- Benchmark for exotic options
- Foundation for path-dependent options

### Portfolio Projects
- Shows numerical methods expertise
- Demonstrates stochastic calculus knowledge
- Professional code organization

## Mathematical Foundation

### GBM Process
```
dS_t = r·S_t·dt + σ·S_t·dW_t
```

### Exact Solution
```
S_T = S_0·exp((r - 0.5·σ²)·T + σ·√T·Z)
```

### Monte Carlo Estimator
```
V_0 ≈ e^(-r·T) · (1/N) · Σ Payoff(S_T^i)
```

### Standard Error
```
SE = e^(-r·T) · σ_payoff / √N
```

## Technologies Used
- Python 3.8+
- NumPy (vectorized simulations)
- SciPy (statistical functions)
- pandas (data handling)
- matplotlib (visualization)
- Jupyter (analysis notebook)

## Educational Value

Demonstrates understanding of:
- Stochastic differential equations
- Numerical integration schemes
- Monte Carlo methods
- Variance reduction
- Statistical analysis
- Software engineering

## Extensions Possible
- Path-dependent options (Asian, Barrier)
- Multi-asset options
- Jump-diffusion models
- Stochastic volatility (Heston)
- Control variates
- Importance sampling
- Quasi-Monte Carlo

## Author
Anjeshnu Trivedi  
CQF Module 3 Examination Project

## Repository Structure
```
monte-carlo-options/
├── src/                  # Source code modules
├── notebooks/            # Jupyter analysis
├── examples/             # Usage examples
├── tests/                # Unit tests
├── docs/                 # Documentation
└── results/              # Output plots
```

## Perfect For
- Quantitative developer roles
- Risk management positions
- Derivatives trading
- Portfolio showcasing
- Academic research

---

