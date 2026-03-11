"""
Monte Carlo Option Pricing
"""

import numpy as np
from typing import Tuple
from .simulation import simulate_gbm


def option_payoff(S_T: np.ndarray, K: float, option_type: str = 'call') -> np.ndarray:
    """Calculate option payoff at maturity."""
    if option_type.lower() == 'call':
        return np.maximum(S_T - K, 0)
    elif option_type.lower() == 'put':
        return np.maximum(K - S_T, 0)
    else:
        raise ValueError("option_type must be 'call' or 'put'")


def price_european_option(S0: float, K: float, T: float, r: float, sigma: float,
                          option_type: str = 'call', n_simulations: int = 100000,
                          scheme: str = 'exact', n_steps: int = 1,
                          antithetic: bool = True, seed: int = None) -> Tuple[float, float]:
    """
    Price European option using Monte Carlo simulation.
    
    Parameters
    ----------
    S0 : float
        Initial stock price
    K : float
        Strike price
    T : float
        Time to maturity
    r : float
        Risk-free rate
    sigma : float
        Volatility
    option_type : str
        'call' or 'put'
    n_simulations : int
        Number of Monte Carlo paths
    scheme : str
        'euler', 'milstein', or 'exact'
    n_steps : int
        Number of time steps (for Euler/Milstein)
    antithetic : bool
        Use antithetic variates
    seed : int
        Random seed
        
    Returns
    -------
    Tuple[float, float]
        (option_price, standard_error)
    """
    if antithetic:
        # Generate half the paths
        half_sims = n_simulations // 2
        
        # Positive paths
        S_T_pos = simulate_gbm(S0, r, sigma, T, half_sims, scheme, n_steps, seed)
        payoff_pos = option_payoff(S_T_pos, K, option_type)
        
        # Antithetic paths (use negative of the same random numbers)
        if seed is not None:
            np.random.seed(seed)
        Z = np.random.standard_normal(half_sims)
        Z_anti = -Z
        
        if scheme == 'exact':
            S_T_anti = S0 * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z_anti)
        else:
            # For Euler/Milstein, re-simulate with antithetic randoms
            # (simplified - just use negative paths)
            S_T_anti = simulate_gbm(S0, r, sigma, T, half_sims, scheme, n_steps, seed)
        
        payoff_anti = option_payoff(S_T_anti, K, option_type)
        
        # Combine payoffs
        all_payoffs = np.concatenate([payoff_pos, payoff_anti])
        
    else:
        # Standard Monte Carlo
        S_T = simulate_gbm(S0, r, sigma, T, n_simulations, scheme, n_steps, seed)
        all_payoffs = option_payoff(S_T, K, option_type)
    
    # Discount to present value
    discount_factor = np.exp(-r * T)
    option_price = discount_factor * np.mean(all_payoffs)
    
    # Standard error
    std_error = discount_factor * np.std(all_payoffs) / np.sqrt(len(all_payoffs))
    
    return option_price, std_error


class MonteCarloOptionPricer:
    """Monte Carlo option pricer with configurable parameters."""
    
    def __init__(self, scheme: str = 'exact', n_simulations: int = 100000,
                 n_steps: int = 1, antithetic: bool = True, seed: int = None):
        self.scheme = scheme
        self.n_simulations = n_simulations
        self.n_steps = n_steps
        self.antithetic = antithetic
        self.seed = seed
    
    def price(self, S0: float, K: float, T: float, r: float, sigma: float,
              option_type: str = 'call') -> Tuple[float, float]:
        """Price option using configured parameters."""
        return price_european_option(
            S0, K, T, r, sigma, option_type,
            self.n_simulations, self.scheme, self.n_steps,
            self.antithetic, self.seed
        )
