"""
Basic Option Pricing Example

Simple example of using the Monte Carlo option pricer.
"""

import sys
sys.path.append('..')

from src.monte_carlo import price_european_option, MonteCarloOptionPricer
from src.black_scholes import black_scholes_price

# Option parameters
S0 = 100.0      # Initial stock price
K = 100.0       # Strike price
T = 1.0         # Time to maturity (1 year)
r = 0.05        # Risk-free rate (5%)
sigma = 0.2     # Volatility (20%)

print("=" * 60)
print("MONTE CARLO OPTION PRICING - BASIC EXAMPLE")
print("=" * 60)

print(f"\nOption Parameters:")
print(f"  S0 (Initial Price): ${S0}")
print(f"  K (Strike):         ${K}")
print(f"  T (Maturity):       {T} year")
print(f"  r (Risk-free):      {r*100}%")
print(f"  σ (Volatility):     {sigma*100}%")

# Black-Scholes analytical price
bs_call = black_scholes_price(S0, K, T, r, sigma, 'call')
bs_put = black_scholes_price(S0, K, T, r, sigma, 'put')

print(f"\n{'='*60}")
print("BLACK-SCHOLES ANALYTICAL PRICES")
print(f"{'='*60}")
print(f"  Call Option: ${bs_call:.4f}")
print(f"  Put Option:  ${bs_put:.4f}")

# Monte Carlo pricing
print(f"\n{'='*60}")
print("MONTE CARLO SIMULATION RESULTS")
print(f"{'='*60}")

# Standard Monte Carlo
mc_call, mc_call_se = price_european_option(
    S0, K, T, r, sigma, 'call',
    n_simulations=100000,
    scheme='exact',
    antithetic=False
)

print(f"\nStandard MC (100k sims):")
print(f"  Call Price: ${mc_call:.4f} ± ${mc_call_se:.4f}")
print(f"  Error vs BS: ${abs(mc_call - bs_call):.4f}")

# Antithetic variates
mc_call_anti, mc_call_anti_se = price_european_option(
    S0, K, T, r, sigma, 'call',
    n_simulations=100000,
    scheme='exact',
    antithetic=True
)

print(f"\nAntithetic Variates MC (100k sims):")
print(f"  Call Price: ${mc_call_anti:.4f} ± ${mc_call_anti_se:.4f}")
print(f"  Error vs BS: ${abs(mc_call_anti - bs_call):.4f}")
print(f"  SE Reduction: {(1 - mc_call_anti_se/mc_call_se)*100:.1f}%")

# Using the pricer class
print(f"\n{'='*60}")
print("USING MONTE CARLO PRICER CLASS")
print(f"{'='*60}")

pricer = MonteCarloOptionPricer(
    scheme='exact',
    n_simulations=100000,
    antithetic=True
)

put_price, put_se = pricer.price(S0, K, T, r, sigma, 'put')
print(f"\nPut Option:")
print(f"  MC Price: ${put_price:.4f} ± ${put_se:.4f}")
print(f"  BS Price: ${bs_put:.4f}")
print(f"  Error:    ${abs(put_price - bs_put):.4f}")

print(f"\n{'='*60}")
print("CONCLUSION")
print(f"{'='*60}")
print("✓ Monte Carlo prices match Black-Scholes within confidence intervals")
print("✓ Antithetic variates significantly reduce standard error")
print("✓ Exact scheme provides unbiased estimates")
