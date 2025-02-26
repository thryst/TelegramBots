import logging
import json
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from web3 import Web3
import openai
from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# API and other keys
load_dotenv()

TELEGRAM_API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')
ETHERSCAN_API_KEY = os.getenv('ETHERSCAN_API_KEY')
#TOKEN_CONTRACT = "0x7076de6ff1d91e00be7e92458089c833de99e22e"  # USDC kontraktsadresse som eksempel

# URL of the token page
url_ethscan = "https://etherscan.io/token/0x7076de6ff1d91e00be7e92458089c833de99e22e"
url_dext = "https://www.dextools.io/app/en/token/fleabone?t=1740580477858"

# Simulate a browser request with headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Set up the Chrome WebDriver
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(service=service, options=options)

# Send a GET request to fetch the webpage content
response_ethscan = requests.get(url_ethscan, headers=headers)

# Open the webpage
driver.get(url_dext)

# Wait for the specific element to load (you might need to adjust the wait time)
driver.implicitly_wait(10)

# Use XPath to find the element
marketcap = driver.find_element(By.XPATH, '/html/body/app-root/div/div/main/app-pairexplorer/app-layout/div/div/div[1]/div[1]/div/div[2]/app-pool-info/div/div[2]/ul/li[1]/span')

# Parse the HTML using BeautifulSoup
soup_ethscan = BeautifulSoup(response_ethscan.text, "html.parser")

# Find the holders count using the provided selector
holders_div = soup_ethscan.select_one("#ContentPlaceHolder1_tr_tokenHolders > div > div")

if holders_div:
    holders_count = holders_div.text.strip().split(" ")[0]  # Takes only the number
    print(f"Number of Holders: {holders_count} \nMarketCap: " + str(marketcap))
else:
    print("Holders information not found.")


# Close the WebDriver
driver.quit()

