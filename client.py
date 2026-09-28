"""Ornstein-Uhlenbeck Mean-Reverting Process Simulator.
100% Python Standard Library.
"""

import math
import random

class OrnsteinUhlenbeckSimulator:
    """Exact simulation: dx_t = theta * (mu - x_t) * dt + sigma * dW_t."""
    @staticmethod
    def simulate_exact(x0, theta, mu, sigma, t_max, steps, seed=42):
        rng = random.Random(seed)
        dt = t_max / steps
        decay = math.exp(-theta * dt)
        cond_var = (sigma**2 / (2.0 * theta)) * (1.0 - math.exp(-2.0 * theta * dt))
        cond_std = math.sqrt(max(cond_var, 0.0))
        
        path = [x0]
        x = x0
        for _ in range(steps):
            cond_mean = mu + (x - mu) * decay
            x = rng.gauss(cond_mean, cond_std)
            path.append(round(x, 5))
        return path
