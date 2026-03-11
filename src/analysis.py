"""
Bias and Variance Analysis Tools
"""

import numpy as np
from typing import List, Dict
from .monte_carlo import price_european_option
from .black_scholes import black_scholes_price


def bias_variance_analysis(
    S0: float, K: float, T: float, r: float, sigma: float,
    option_type: str = 'call',
    n_simulations_list: List[int] = None,
    n_trials: int = 100,
    scheme: str = 'exact'
) -> Dict:
    """
    Analyze bias and variance of Monte Carlo estimator.
    
    Parameters
    ----------
    S0, K, T, r, sigma : float
        Option parameters
    option_type : str
        'call' or 'put'
    n_simulations_list : List[int]
        List of simulation counts to test
    n_trials : int
        Number of independent trials per N
    scheme : str
        Simulation scheme
        
    Returns
    -------
    Dict
        Results including bias, variance, MSE for each N
    """
    if n_simulations_list is None:
        n_simulations_list = [1000, 5000, 10000, 50000, 100000]
    
    # True price from Black-Scholes
    true_price = black_scholes_price(S0, K, T, r, sigma, option_type)
    
    results = {
        'n_simulations': [],
        'bias': [],
        'variance': [],
        'mse': [],
        'std_error': []
    }
    
    for n_sims in n_simulations_list:
        prices = []
        
        for trial in range(n_trials):
            price, _ = price_european_option(
                S0, K, T, r, sigma, option_type,
                n_simulations=n_sims,
                scheme=scheme,
                antithetic=False,
                seed=trial
            )
            prices.append(price)
        
        prices = np.array(prices)
        
        # Calculate statistics
        bias = np.mean(prices) - true_price
        variance = np.var(prices)
        mse = bias**2 + variance
        std_error = np.std(prices)
        
        results['n_simulations'].append(n_sims)
        results['bias'].append(bias)
        results['variance'].append(variance)
        results['mse'].append(mse)
        results['std_error'].append(std_error)
    
    return results


def convergence_test(
    S0: float, K: float, T: float, r: float, sigma: float,
    option_type: str = 'call',
    max_simulations: int = 1000000,
    n_points: int = 20
) -> Dict:
    """Test convergence as N increases."""
    
    true_price = black_scholes_price(S0, K, T, r, sigma, option_type)
    
    n_sims_list = np.logspace(3, np.log10(max_simulations), n_points, dtype=int)
    
    prices = []
    errors = []
    
    for n_sims in n_sims_list:
        price, std_err = price_european_option(
            S0, K, T, r, sigma, option_type,
            n_simulations=n_sims,
            scheme='exact',
            antithetic=True
        )
        prices.append(price)
        errors.append(abs(price - true_price))
    
    return {
        'n_simulations': n_sims_list,
        'prices': prices,
        'errors': errors,
        'true_price': true_price
    }
