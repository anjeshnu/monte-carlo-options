"""
Black-Scholes Analytical Pricing
"""

import numpy as np
from scipy.stats import norm


def black_scholes_call(S0: float, K: float, T: float, r: float, sigma: float) -> float:
    """Black-Scholes formula for European call option."""
    if T <= 0:
        return max(S0 - K, 0)
    
    d1 = (np.log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    return S0 * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)


def black_scholes_put(S0: float, K: float, T: float, r: float, sigma: float) -> float:
    """Black-Scholes formula for European put option."""
    if T <= 0:
        return max(K - S0, 0)
    
    d1 = (np.log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    return K * np.exp(-r * T) * norm.cdf(-d2) - S0 * norm.cdf(-d1)


def black_scholes_price(S0: float, K: float, T: float, r: float, sigma: float, 
                        option_type: str = 'call') -> float:
    """Black-Scholes price for call or put option."""
    if option_type.lower() == 'call':
        return black_scholes_call(S0, K, T, r, sigma)
    elif option_type.lower() == 'put':
        return black_scholes_put(S0, K, T, r, sigma)
    else:
        raise ValueError("option_type must be 'call' or 'put'")


def black_scholes_delta(S0: float, K: float, T: float, r: float, sigma: float,
                        option_type: str = 'call') -> float:
    """Calculate option delta."""
    if T <= 0:
        return 1.0 if (option_type == 'call' and S0 > K) else 0.0
    
    d1 = (np.log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    
    if option_type.lower() == 'call':
        return norm.cdf(d1)
    else:
        return norm.cdf(d1) - 1.0


def black_scholes_gamma(S0: float, K: float, T: float, r: float, sigma: float) -> float:
    """Calculate option gamma."""
    if T <= 0:
        return 0.0
    
    d1 = (np.log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    return norm.pdf(d1) / (S0 * sigma * np.sqrt(T))


def black_scholes_vega(S0: float, K: float, T: float, r: float, sigma: float) -> float:
    """Calculate option vega."""
    if T <= 0:
        return 0.0
    
    d1 = (np.log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    return S0 * norm.pdf(d1) * np.sqrt(T)
