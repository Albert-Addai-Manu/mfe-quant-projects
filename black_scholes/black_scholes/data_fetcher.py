import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime

def get_current_price(ticker: str) -> float:
    """
    Fetches the most recent closing price for a stock.
    """
    stock = yf.Ticker(ticker)
    data = stock.history(period="5d")  # Get a few days to ensure we have latest
    return data['Close'].iloc[-1]


def get_historical_volatility(ticker: str, days: int = 252) -> float:
    """
    Calculates annualized historical volatility from daily returns.
    
    Args:
        ticker: Stock symbol
        days: Number of trading days to use (default 252 ≈ 1 year)
    
    Returns:
        Annualized volatility (sigma)
    """
    stock = yf.Ticker(ticker)
    data = stock.history(period=f"{days}d")
    if len(data) < 30:
        raise ValueError("Not enough data to calculate volatility")
    
    daily_returns = data['Close'].pct_change().dropna()
    volatility = daily_returns.std()
    annualized_vol = volatility * np.sqrt(252)  # 252 trading days in a year
    return annualized_vol


def get_risk_free_rate() -> float:
    """
    Approximates the current US risk-free rate using the 10-year Treasury yield.
    (As of late 2025, this is a reasonable proxy)
    """
    # We can hardcode a recent value or fetch — here we use a safe recent average
    # In a full version you'd pull from FRED, but this keeps it simple and working
    return 0.042  # ≈ 4.2% as of Dec 2025 (you can update this manually if needed)
