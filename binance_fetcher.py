import requests
import pandas as pd
from datetime import datetime, timezone, timedelta
import time
import os

# ========== Configuration ==========
SYMBOL = "ETHUSDT"
INTERVAL = "1h"

# Specify your date range here in UTC (ISO8601 format for convenience)
START_DATE = "2021-01-01T00:00:00Z"
END_DATE = "2025-12-31T23:59:00Z"
OUTPUT_FILENAME = f"historical_{SYMBOL}_{INTERVAL}_{START_DATE[:10]}_{END_DATE[:10]}.csv"


def fetch_candles(symbol, interval, start_time, end_time):
    """Fetch historical candles between start_time and end_time from Binance Futures API"""
    all_candles = []
    limit = 1000
    current_start_time = int(start_time.timestamp() * 1000)
    end_time_ms = int(end_time.timestamp() * 1000)
    request_count = 0

    while current_start_time < end_time_ms:
        try:
            params = {
                "symbol": symbol,
                "interval": interval,
                "startTime": current_start_time,
                "endTime": end_time_ms,
                "limit": limit
            }

            print(f"Request #{request_count + 1}: Fetching candles starting at {datetime.fromtimestamp(current_start_time/1000, tz=timezone.utc).isoformat()} ...")
            response = requests.get("https://fapi.binance.com/fapi/v1/klines", params=params)
            data = response.json()

            if not data:
                print("No more data to fetch.")
                break

            batch = [{
                "timestamp": datetime.fromtimestamp(entry[0] / 1000, tz=timezone.utc),
                "open": float(entry[1]),
                "high": float(entry[2]),
                "low": float(entry[3]),
                "close": float(entry[4]),
                "volume": float(entry[5]),          # Base asset volume
                "quote_volume": float(entry[7])     # Quote asset volume
            } for entry in data]

            all_candles.extend(batch)
            print(f"  Retrieved: {len(batch)} candles; Total so far: {len(all_candles)}")

            # Advance start_time to the next candle
            current_start_time = int(batch[-1]["timestamp"].timestamp() * 1000) + 1
            request_count += 1

            time.sleep(0.2)  # avoid rate limits

        except Exception as e:
            print(f"Error fetching data: {e}")
            break

    df = pd.DataFrame(all_candles)
    if not df.empty:
        df = df.sort_values("timestamp").drop_duplicates()
    return df


def save_to_csv(df, filename):
    """Save DataFrame to CSV with proper formatting"""
    df = df.copy()
    df['timestamp'] = df['timestamp'].dt.strftime('%Y-%m-%dT%H:%M:%SZ')

    if os.path.exists(filename):
        existing = pd.read_csv(filename)
        combined = pd.concat([existing, df]).drop_duplicates('timestamp')
        combined = combined.sort_values('timestamp')
        combined.to_csv(filename, index=False)
        print(f"Appended {len(combined) - len(existing)} new records to {filename}")
    else:
        df.to_csv(filename, index=False)
        print(f"Created new data file: {filename} with {len(df)} records")


def main():
    start_time = datetime.fromisoformat(START_DATE.replace("Z", "+00:00"))
    end_time = datetime.fromisoformat(END_DATE.replace("Z", "+00:00"))

    print(f"Fetching candles from {start_time} to {end_time} for {SYMBOL}...")
    df = fetch_candles(SYMBOL, INTERVAL, start_time, end_time)

    if not df.empty:
        print(f"Retrieved {len(df)} candles ({df['timestamp'].min()} to {df['timestamp'].max()})")
        save_to_csv(df, OUTPUT_FILENAME)
    else:
        print("No data retrieved. Check API connection and parameters")


if __name__ == "__main__":
    main()
