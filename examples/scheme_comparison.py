"""
Comparison of Different Numerical Schemes

Compare Euler, Milstein, and Exact simulation schemes.
"""

import sys
sys.path.append('..')

from src.monte_carlo import price_european_option
from src.black_scholes import black_scholes_price
import time

# Parameters
S0, K, T, r, sigma = 100.0, 100.0, 1.0, 0.05, 0.2
n_sims = 100000
n_steps = 50  # For Euler and Milstein

print("SCHEME COMPARISON")
print("=" * 70)

bs_price = black_scholes_price(S0, K, T, r, sigma, 'call')
print(f"Black-Scholes Price: ${bs_price:.4f}\n")

schemes = ['euler', 'milstein', 'exact']
results = {}

for scheme in schemes:
    start = time.time()
    
    price, se = price_european_option(
        S0, K, T, r, sigma, 'call',
        n_simulations=n_sims,
        scheme=scheme,
        n_steps=n_steps if scheme != 'exact' else 1,
        antithetic=True
    )
    
    elapsed = time.time() - start
    
    results[scheme] = {
        'price': price,
        'se': se,
        'error': abs(price - bs_price),
        'time': elapsed
    }

print(f"{'Scheme':<12} {'Price':<12} {'Std Error':<12} {'Error':<12} {'Time (s)'}")
print("-" * 70)

for scheme in schemes:
    r = results[scheme]
    print(f"{scheme.capitalize():<12} ${r['price']:<11.4f} "
          f"${r['se']:<11.4f} ${r['error']:<11.4f} {r['time']:.3f}")

print(f"\n{'='*70}")
print("EFFICIENCY ANALYSIS")
print(f"{'='*70}")

for scheme in schemes:
    r = results[scheme]
    efficiency = 1 / (r['se']**2 * r['time'])
    print(f"{scheme.capitalize():<12} Efficiency Score: {efficiency:.2f}")
