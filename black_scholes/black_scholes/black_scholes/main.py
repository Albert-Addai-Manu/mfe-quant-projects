from black_scholes_pricer import black_scholes_call, black_scholes_put
from data_fetcher import get_current_price, get_historical_volatility, get_risk_free_rate

def main():
    # User-configurable parameters
    ticker = "AAPL"          # Change to any stock, e.g., "MSFT", "TSLA"
    K = 230.0                # Strike price — try different values
    days_to_expiry = 30      # Days until option expires (e.g., 30, 60, 90)

    # Fetch real data
    S = get_current_price(ticker)
    sigma = get_historical_volatility(ticker)
    r = get_risk_free_rate()  # Current ~4.18%
    T = days_to_expiry / 365.0  # Time in years

    # Calculate prices
    call_price = black_scholes_call(S, K, T, r, sigma)
    put_price = black_scholes_put(S, K, T, r, sigma)

    # Print results
    print("\n=== Black-Scholes Option Pricer ===")
    print(f"Stock: {ticker}")
    print(f"Current Price (S): ${S:.2f}")
    print(f"Annualized Volatility (σ): {sigma:.2%}")
    print(f"Risk-Free Rate (r): {r:.2%}")
    print(f"Time to Expiry (T): {days_to_expiry} days ({T:.4f} years)")
    print(f"Strike Price (K): ${K}")
    print(f"\nTheoretical Call Option Price: ${call_price:.2f}")
    print(f"Theoretical Put Option Price: ${put_price:.2f}\n")

    # Quick sanity check
    if call_price > 0:
        print("✓ Model ran successfully!")
    else:
        print("Something went wrong — check inputs.")

if __name__ == "__main__":
    main()
