# 📊 Binance Free Historical Candle Data Downloader (Python)

Easily **fetch free historical Binance Futures candlestick (OHLCV) data** with this simple and powerful Python script.  
Download years of data (e.g., 2021–2025) for any symbol and interval — all without API keys or paid plans.

---

## 🚀 Features

✅ **Free & No API Key Required**  
✅ **Fetch from Binance Futures REST API**  
✅ **Supports Any Symbol (e.g., BTCUSDT, ETHUSDT)**  
✅ **All Timeframes Supported** – 1m, 5m, 15m, 1h, 4h, 1d, etc.  
✅ **Handles Full Date Ranges Automatically**  
✅ **Appends & Updates CSV Files**  
✅ **Rate-Limit Safe** with Auto Sleep  
✅ **Clean & Readable Data (timestamp, open, high, low, close, volume)**  

---

## 🧩 Example Use Cases

- Build **trading backtests** for bots or strategies  
- Train **machine learning models** on OHLCV data  
- Analyze **market structure and volatility**  
- Prepare data for **quantitative research or visualization**

---

## 📦 Installation

Make sure you have **Python 3.8+** installed.

```bash
git clone https://github.com/frostyalce000/binance-free-historical-candlestick-data-fetcher.git
cd binance-free-historical-candlestick-data-fetcher
pip install -r requirements.txt
````

> Requirements:
>
> * `requests`
> * `pandas`

If you don’t have a `requirements.txt`, simply install manually:

```bash
pip install requests pandas
```

---

## ⚙️ Configuration

Edit the following values inside the script:

```python
SYMBOL = "ETHUSDT"              # Change to any symbol, e.g., BTCUSDT
INTERVAL = "1h"                 # 1m, 5m, 15m, 1h, 4h, 1d, etc.
START_DATE = "2021-01-01T00:00:00Z"
END_DATE = "2025-12-31T23:59:00Z"
```

The script automatically fetches all candles in batches (up to Binance’s max limit of 1000 per request)
and stores them in a CSV file like:

```
historical_ETHUSDT_1h_2021-01-01_2025-12-31.csv
```

---

## ▶️ Usage

Run the script directly:

```bash
python fetch_binance_candles.py
```

It will start fetching data from the Binance Futures API and display progress:

```
Fetching candles from 2021-01-01 to 2025-12-31 for ETHUSDT...
Request #1: Fetching candles starting at 2021-01-01T00:00:00+00:00 ...
  Retrieved: 1000 candles; Total so far: 1000
...
Created new data file: historical_ETHUSDT_1h_2021-01-01_2025-12-31.csv with 34512 records
```

If you re-run the script, it will **append only new data** automatically.

---

## 📂 Output Example

| timestamp            | open   | high   | low    | close  | volume  | quote_volume |
| -------------------- | ------ | ------ | ------ | ------ | ------- | ------------ |
| 2021-01-01T00:00:00Z | 737.25 | 739.14 | 733.00 | 736.52 | 1234.55 | 908232.12    |
| 2021-01-01T01:00:00Z | 736.52 | 741.20 | 735.33 | 740.00 | 1102.10 | 816411.84    |
| ...                  | ...    | ...    | ...    | ...    | ...     | ...          |

---

## 🧠 Notes

* Works with **Binance Futures (fapi.binance.com)**
* For **Spot data**, replace the API endpoint:
  `https://api.binance.com/api/v3/klines`
* Avoid frequent calls; Binance limits requests per minute.
* Recommended sleep delay: **0.2–0.5 seconds** between requests.

---

## 💡 Example: Fetch Daily BTCUSDT Candles (Spot)

Just change these:

```python
SYMBOL = "BTCUSDT"
INTERVAL = "1d"
```

---

## 🧰 Tech Stack

* **Language:** Python 3
* **Libraries:** requests, pandas
* **Data Source:** Binance Futures API

---

## 🌟 Contribute

Pull requests and issues are welcome!
If you find this script useful, please ⭐ **star the repo** to support the project.
