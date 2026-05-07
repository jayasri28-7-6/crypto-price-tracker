# Cryptocurrency Price Tracker  
A Python-based automation project that tracks real-time cryptocurrency prices from CoinMarketCap using Selenium and Pandas.

## 📌 Features
💰 Fetches Top 10 cryptocurrencies in real-time  
⚡ Fast web scraping using Selenium headless browser  
📊 Displays live crypto prices and 24h changes  
💾 Automatically saves cryptocurrency data to CSV  
🚀 Detects top gainers with significant price changes  
🕒 Stores timestamped records for future analysis  

## 🛠️ Technologies Used
- Python  
- Selenium  
- Pandas  
- WebDriver Manager  

## 📂 Project Structure
```bash
project/
│── crypto.py
│── data/
│    └── crypto_prices.csv
```

## ⚙️ Installation

Clone the repository:
```bash
git clone https://github.com/your-username/crypto-price-tracker.git
cd crypto-price-tracker
```

Install required packages:
```bash
pip install pandas selenium webdriver-manager
```

## ▶️ How to Run
```bash
python crypto.py
```

## 🌐 Output
- Fetches live cryptocurrency data from CoinMarketCap  
- Displays top cryptocurrencies with prices and 24h changes  
- Saves scraped data automatically into CSV format  
- Tracks timestamped market information for analysis  

## 📊 Example Features
- View Top 10 cryptocurrencies  
- Monitor 24h price changes  
- Detect top gaining cryptocurrencies  
- Save historical crypto data for analysis  

## 📁 Output File
CSV file is saved at:
```bash
data/crypto_prices.csv
```

### Contains:
- Timestamp  
- Rank  
- Cryptocurrency Name  
- Price  
- 24h Change  
- Market Cap  

## ⚠️ Notes
- Internet connection is required  

If scraping fails:
```python
time.sleep(6)
```

Run browser with:
```python
headless=False
```

## 🚀 Future Improvements
📈 Add cryptocurrency price visualization charts  
🔔 Implement real-time price alert system  
🌐 Convert project into a web application  
📡 Add live dashboard for tracking crypto trends  
🤖 Integrate AI-based price prediction system  


