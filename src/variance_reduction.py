"""
Variance Reduction Techniques
"""

import numpy as np
from typing import Tuple


def antithetic_variates(random_samples: np.ndarray) -> np.ndarray:
    """
    Generate antithetic variates from random samples.
    
    For each Z, also use -Z to reduce variance.
    """
    antithetic = -random_samples
    return np.concatenate([random_samples, antithetic])


def calculate_variance_reduction(
    standard_variance: float,
    antithetic_variance: float
) -> Tuple[float, float]:
    """
    Calculate variance reduction factor and percentage.
    
    Returns
    -------
    Tuple[float, float]
        (reduction_factor, reduction_percentage)
    """
    reduction_factor = standard_variance / antithetic_variance
    reduction_pct = (1 - antithetic_variance / standard_variance) * 100
    
    return reduction_factor, reduction_pct
