import numpy as np
from scipy.stats import norm

def black_scholes_call(S: float, K: float, T: float, r: float, sigma: float) -> float:
    """
    Price of a European call option using the Black-Scholes-Merton model.
    
    Args:
        S: Current stock price
        K: Strike price
        T: Time to maturity in years (e.g., 30/365 ≈ 0.082 for 30 days)
        r: Risk-free interest rate (annual, e.g., 0.05 for 5%)
        sigma: Annualized volatility (e.g., 0.20 for 20%)
    
    Returns:
        Theoretical call option price
    """
    if T <= 0:
        return max(S - K, 0.0)
    
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    call_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    return call_price


def black_scholes_put(S: float, K: float, T: float, r: float, sigma: float) -> float:
    """
    Price of a European put option using the Black-Scholes-Merton model.
    """
    if T <= 0:
        return max(K - S, 0.0)
    
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    put_price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    return put_price
