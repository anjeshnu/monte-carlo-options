"""
Option Parameter Classes
"""

from dataclasses import dataclass
from typing import Literal


@dataclass
class OptionParameters:
    """Parameters for option pricing."""
    S0: float      # Initial stock price
    K: float       # Strike price
    T: float       # Time to maturity (years)
    r: float       # Risk-free rate
    sigma: float   # Volatility
    
    def __post_init__(self):
        if self.S0 <= 0 or self.K <= 0 or self.T <= 0:
            raise ValueError("S0, K, and T must be positive")
        if self.sigma < 0:
            raise ValueError("Volatility cannot be negative")
    
    @property
    def moneyness(self) -> float:
        """Calculate moneyness (S0/K)."""
        return self.S0 / self.K


@dataclass
class SimulationParameters:
    """Parameters for Monte Carlo simulation."""
    n_simulations: int
    n_steps: int = 1
    scheme: Literal['euler', 'milstein', 'exact'] = 'exact'
    antithetic: bool = False
    seed: int = None
    
    def __post_init__(self):
        if self.n_simulations <= 0:
            raise ValueError("Number of simulations must be positive")
        if self.scheme not in ['euler', 'milstein', 'exact']:
            raise ValueError("Scheme must be 'euler', 'milstein', or 'exact'")
