

# 🚀 Cryptocurrency Price Tracker

A fast and automated Python project that scrapes real-time cryptocurrency data from CoinMarketCap using Selenium and stores it for analysis.


## 📌 Features

* 📊 Fetches Top 10 cryptocurrencies in real-time
* ⏱ Fast web scraping using headless browser
* 💾 Automatically saves data to CSV
* 🚀 Detects top gainers (+5% in 24h)
* 🧾 Logs timestamped data for tracking

## 🛠️ Technologies Used

* Python
* Selenium
* Pandas
* WebDriver Manager

---

## 📂 Project Structure

CRYPTOCURRENCY
/
│── crypto.py
│── data/
│   └── crypto_prices.csv




## ⚙️ Installation

1. Clone the repository:


git clone https://github.com/your-username/crypto-price-tracker.git
cd crypto-price-tracker


2. Install required packages:

pip install pandas selenium webdriver-manager

## ▶️ How to Run


python crypto.py




## 📊 Sample Output


Fetching real-time cryptocurrency data from CoinMarketCap...

Latest Data:
Name        Price       24h Change
Bitcoin     $69,969     0.16%
Ethereum    $2,133      0.03%

Data saved successfully to data/crypto_prices.csv


## 📁 Output File

* CSV file is saved at:

data/crypto_prices.csv

* Contains:

  * Timestamp
  * Rank
  * Name
  * Price
  * 24h Change
  * Market Cap



## ⚠️ Notes

* Internet connection required
* If scraping fails:

  * Increase delay (`time.sleep(6)`)
  * Run with `headless=False`



## 🚀 Future Improvements

* 📈 Add data visualization (graphs)
* 🌐 Convert into Django web application
* 🔔 Add price alert system
* 📡 Real-time dashboard



