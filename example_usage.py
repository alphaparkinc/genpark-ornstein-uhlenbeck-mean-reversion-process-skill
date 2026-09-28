"""Example demonstrating OU mean-reverting simulation."""
from client import OrnsteinUhlenbeckSimulator

def main():
    path = OrnsteinUhlenbeckSimulator.simulate_exact(x0=5.0, theta=2.0, mu=0.0, sigma=0.5, t_max=1.0, steps=10)
    print("Mean Reversion Path (Reverting to 0):", path)

if __name__ == "__main__":
    main()
