# Ornstein-Uhlenbeck Mean-Reverting Process Skill

Exact discrete transition simulation for stationary Gaussian mean-reverting stochastic processes.

```mermaid
flowchart TD
    State["Current Value x_t"] --> Drift["Reversion Drift: θ(μ - x_t)"]
    State --> Decay["Exact Exponential Transition Mean μ + (x - μ)e^{-θΔt}"]
    Decay --> Variance["Stationary Conditional Variance (σ^2 / 2θ)(1 - e^{-2θΔt})"]
    Variance --> Sample["Sample Gaussian Transition"]
    Sample --> Next["Updated Trajectory x_{t+1}"]
```

## Features
- **100% Python Standard Library**: Exact conditional distribution evaluation.
- **Zero Discretization Bias**: Avoids naive Euler approximations.
- **Physical & Financial Applications**: Models friction, velocity relaxation, and interest rates.
