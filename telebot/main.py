import requests
from datetime import datetime
import telebot
from auth_token import  token
from telebot import types




def telegram_bot(token):
    bot = telebot.TeleBot(token)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btc = types.KeyboardButton('BTC')
    eth = types.KeyboardButton('ETH')

    markup.add(btc,eth)

    @bot.message_handler(commands=["start"])
    def start_message(message):
        bot.send_message(message.chat.id, "Hello friend! Write the 'price Btc or Eth' !",reply_markup=markup)

    @bot.message_handler(content_types=["text"])

    def send_text(message):

        if message.text.lower() == 'price btc' or message.text.lower()=='price b'or message.text.lower()=='b'\
                or message.text=='BTC':
            try:
                request_Btc = requests.get("https://yobit.net/api/3/ticker/btc_usd")
                response = request_Btc.json()
                sell_price_btc = response["btc_usd"]["sell"]
                high_price_btc = response['btc_usd']['high']
                low_price_btc = response['btc_usd']['low']

                date = datetime.now().strftime('%Y-%m-%d %H:%M')
                bot.send_message(
                    message.chat.id,
                    f"{date}\nSell BTC price: {sell_price_btc} $\nHigh price:{high_price_btc} $\nLow price:{low_price_btc} $"
                )
            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id,
                    "Damn...Something was wrong..."
                )
        elif message.text.lower() == 'price eth' or message.text.lower() == 'price e' or message.text.lower() == 'e'\
                or message.text=='ETH':
            try:
                request_Eth = requests.get("https://yobit.net/api/3/ticker/eth_usd")
                response = request_Eth.json()
                sell_price_eth = response["eth_usd"]["sell"]
                high_price_eth = response['eth_usd']['high']
                low_price_eth = response['eth_usd']['low']

                date = datetime.now().strftime('%Y-%m-%d %H:%M')
                bot.send_message(
                    message.chat.id,
                    f"{date}\nSell Eth price: {sell_price_eth} $\nHigh price:{high_price_eth} $\nLow price:{low_price_eth} $"
                )
            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id,
                    "Damn...Something was wrong..."
                )

        else : bot.send_message(
                    message.chat.id,
                    "Sorry wrong command"
                )

    bot.polling()

if __name__=='__main__':
    telegram_bot(token)