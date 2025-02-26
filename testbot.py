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

# Logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# API and other keys
load_dotenv()

TELEGRAM_API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')
ETHERSCAN_API_KEY = os.getenv('ETHERSCAN_API_KEY')
#TOKEN_CONTRACT = "0x7076de6ff1d91e00be7e92458089c833de99e22e"  # USDC kontraktsadresse som eksempel

# URL of the token page
url = "https://etherscan.io/token/0x7076de6ff1d91e00be7e92458089c833de99e22e"

# Simulate a browser request with headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Send a GET request to fetch the webpage content
response = requests.get(url, headers=headers)

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Find the holders count using the provided selector
holders_div = soup.select_one("#ContentPlaceHolder1_tr_tokenHolders > div > div")

if holders_div:
    holders_count = holders_div.text.strip().split(" ")[0]  # Takes only the number
    print(f"Number of Holders: {holders_count}")
else:
    print("Holders information not found.")

