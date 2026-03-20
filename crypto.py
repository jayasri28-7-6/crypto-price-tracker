import os
import time
import pandas as pd
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def get_top_cryptos_fast(headless=True):
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--log-level=3")  # suppress logs
    chrome_options.add_argument("--blink-settings=imagesEnabled=false")  # don't load images
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    driver.set_page_load_timeout(15)

    try:
        driver.get("https://coinmarketcap.com/")
    except Exception:
        print("Page took too long to load or connection failed.")
        driver.quit()
        return pd.DataFrame()

    time.sleep(4)

    rows = driver.find_elements(By.CSS_SELECTOR, "table.cmc-table tbody tr")
    if not rows:
        print("⚠ Table not found on page.")
        driver.quit()
        return pd.DataFrame()

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    crypto_data = []

    for idx, row in enumerate(rows[:10]):  # top 10 cryptos
        try:
            cols = row.find_elements(By.TAG_NAME, "td")
            crypto_data.append({
                "Timestamp": current_time,
                "Rank": idx + 1,
                "Name": cols[2].text.split("\n")[0],
                "Price": cols[3].text,
                "24h Change": cols[4].text,
                "Market Cap": cols[7].text
            })
        except Exception:
            continue

    driver.quit()
    return pd.DataFrame(crypto_data)


def save_to_csv(df, filename="data/crypto_prices.csv"):
    os.makedirs("data", exist_ok=True)
    if os.path.exists(filename):
        existing = pd.read_csv(filename)
        df = pd.concat([existing, df], ignore_index=True)
    df.to_csv(filename, index=False)
    print(f" Data saved successfully to {filename}")


def main():
    print("Fetching real-time cryptocurrency data from CoinMarketCap...")
    start = time.time()

    data = get_top_cryptos_fast(headless=True)

    print(f"⏱ Completed in {time.time() - start:.2f}s")

    if data.empty:
        print("⚠ No data found.")
        return

    print("\nLatest Data:")
    print(data)
    save_to_csv(data)

    try:
        data["24h Change %"] = data["24h Change"].str.replace("%", "").astype(float)
        gainers = data[data["24h Change %"] > 5]

        if not gainers.empty:
            print("\n Top 24h Gainers:")
            print(gainers[["Name", "Price", "24h Change"]])
        else:
            print("\nNo coin gained above +5% in the last 24h.")
    except Exception as e:
        print(f"Error filtering gainers: {e}")


if __name__ == "__main__":
    main()