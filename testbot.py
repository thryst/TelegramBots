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

# Sett opp logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Sett API-nøkler
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


# Filnavn for lagring av samtaler
#IMAGE_FILE = "fleabone_image.json"
#user_states = {}

# Håndter bildefil-lagring
#def load_image():
#    if os.path.exists(IMAGE_FILE):
#        with open(IMAGE_FILE, "r") as file:
#            return json.load(file).get("image_id", None)
#    return None

#def save_image(image_id):
#    with open(IMAGE_FILE, "w") as file:
#        json.dump({"image_id": image_id}, file)

# Last inn eksisterende samtale
#image_id = load_image()

# Kommando for å oppdatere bildet
#async def update_image(update: Update, context):
#    user_id = update.message.from_user.id
#    user_states[user_id] = "awaiting_image"
#    await update.message.reply_text("Vennligst send meg et nytt bilde eller en GIF som skal brukes fremover.")

# Håndter mottak av bilde eller GIF
#async def handle_media(update: Update, context):
#    user_id = update.message.from_user.id

    #if user_states.get(user_id) == "awaiting_image":
        #if update.message.photo:
            #new_image_id = update.message.photo[-1].file_id
        #elif update.message.animation:
            #new_image_id = update.message.animation.file_id
        #else:
            #await update.message.reply_text("Dette er ikke et gyldig bilde eller GIF. Prøv igjen.")
            #return

        #save_image(new_image_id)
        #global image_id
        #image_id = new_image_id
        #await update.message.reply_text("Bilde/GIF er oppdatert og vil bli brukt i fremtidige meldinger.")
        #user_states[user_id] = None

# Håndter meldinger og legg til bildet
#async def respond(update: Update, context):
#    global conversation_history, image_id
#
#    user_message = update.message.text
#    bot_username = f"@{context.bot.username}"
#    
#    if "bone" not in user_message and bot_username not in user_message:
#        return
#
#    if image_id:
#        await context.bot.send_photo(chat_id=update.message.chat_id, photo=image_id, caption=bot_reply)
#    else:
#        await update.message.reply_text(bot_reply)

# Hovedfunksjon
#if __name__ == '__main__':
#    application = ApplicationBuilder().token(TELEGRAM_API_TOKEN).build()

#    application.add_handler(CommandHandler('updateimage', update_image))
#    application.add_handler(MessageHandler(filters.PHOTO | filters.ANIMATION, handle_media))
#    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), respond))

#    application.run_polling()
#    application.idle()