"""
GBM Simulation Schemes
"""

import numpy as np


def simulate_gbm_euler(S0: float, r: float, sigma: float, T: float,
                       n_steps: int, n_paths: int, seed: int = None) -> np.ndarray:
    """
    Simulate GBM using Euler scheme.
    
    S_{t+dt} = S_t + r*S_t*dt + sigma*S_t*sqrt(dt)*Z
    """
    if seed is not None:
        np.random.seed(seed)
    
    dt = T / n_steps
    sqrt_dt = np.sqrt(dt)
    S = np.full(n_paths, S0)
    
    for _ in range(n_steps):
        Z = np.random.standard_normal(n_paths)
        S = S + r * S * dt + sigma * S * sqrt_dt * Z
        S = np.maximum(S, 0)
    
    return S


def simulate_gbm_milstein(S0: float, r: float, sigma: float, T: float,
                          n_steps: int, n_paths: int, seed: int = None) -> np.ndarray:
    """
    Simulate GBM using Milstein scheme.
    
    Includes Itô correction term: 0.5*sigma^2*S_t*dt*(Z^2-1)
    """
    if seed is not None:
        np.random.seed(seed)
    
    dt = T / n_steps
    sqrt_dt = np.sqrt(dt)
    S = np.full(n_paths, S0)
    
    for _ in range(n_steps):
        Z = np.random.standard_normal(n_paths)
        S = S + r * S * dt + sigma * S * sqrt_dt * Z + 0.5 * sigma**2 * S * dt * (Z**2 - 1)
        S = np.maximum(S, 0)
    
    return S


def simulate_gbm_exact(S0: float, r: float, sigma: float, T: float,
                       n_paths: int, seed: int = None) -> np.ndarray:
    """
    Simulate GBM using exact (analytical) solution.
    
    S_T = S_0 * exp((r - 0.5*sigma^2)*T + sigma*sqrt(T)*Z)
    """
    if seed is not None:
        np.random.seed(seed)
    
    Z = np.random.standard_normal(n_paths)
    S_T = S0 * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)
    
    return S_T


def simulate_gbm(S0: float, r: float, sigma: float, T: float, n_paths: int,
                 scheme: str = 'exact', n_steps: int = 1, seed: int = None) -> np.ndarray:
    """Simulate GBM using specified scheme."""
    if scheme == 'euler':
        return simulate_gbm_euler(S0, r, sigma, T, n_steps, n_paths, seed)
    elif scheme == 'milstein':
        return simulate_gbm_milstein(S0, r, sigma, T, n_steps, n_paths, seed)
    elif scheme == 'exact':
        return simulate_gbm_exact(S0, r, sigma, T, n_paths, seed)
    else:
        raise ValueError(f"Unknown scheme: {scheme}")
