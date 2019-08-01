# -*- coding: utf-8 -*-

"""
Proj: BountieBot - A Telegram Bot for Bountie!

Auth: Ken Fung

Desc: This Telegram bot directs users to Bountie's websites and social media pages. Also, it checks for
the price of BNTE, BTC and ETH.
"""


from uuid import uuid4
from telegram.utils.helpers import escape_markdown
from telegram import InlineQueryResultArticle, ParseMode, \
    InputTextMessageContent
from telegram.ext import Updater, InlineQueryHandler, CommandHandler

import logging
import json
import requests
from coinbase.wallet.client import Client

#------------------------------------------------------------------
#All this code does is collect for the crypto prices

big_result_list = []

# Get API Key and API Secret from your coinbase account. Check out README for more info
# Also you can leave the API version as it is.
client = Client('API Key', 'API Secret', api_version='YYYY-MM-DD')

BTCUSD_price = client.get_buy_price(currency_pair = 'BTC-USD')
ETHUSD_price = client.get_buy_price(currency_pair = 'ETH-USD')
BTCUSD = (BTCUSD_price.get("amount"))
ETHUSD = (ETHUSD_price.get("amount"))

big_result_list.append("1 BTC = US$" + str(BTCUSD))
big_result_list.append("1 ETH = US$" + str(ETHUSD))


def coinGecko_data():
    mainsite = 'https://api.coingecko.com/api/v3/coins/bountie?tickers=false&market_data=true'
    request = requests.get(mainsite)
    jsonTest = request.json()

    return (jsonTest)


x = coinGecko_data()
big_result_list.append("1 BNTE = US$" + str(x.get("market_data").get("ath").get("usd")))

big_result_list.append("Data gathered from CoinGecko and Coinbase!")

seperator = '\n'

big_spaced_list = seperator.join(big_result_list)

#--------------------------------------------------------

## Uncomment to enable logging for diagnostic purposes
#logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                    level=logging.INFO)
#
#logger = logging.getLogger(__name__)


# The message that the user receives when the bot first starts, or when the user types in /start
# Edit the @handle with the name of the bot!
def start(bot, update):
    update.message.reply_text('Hi! Type @(Edit with bot name) to begin!')


token_intro = 'Buy Bountie Tokens here!'
bountie_token_URL = 'https://latoken.com/exchange/BTC-BNTE'

token_list = []
token_list.append(token_intro)
token_list.append(bountie_token_URL)
token_spaced_list = seperator.join(token_list)


def inlinequery(bot, update):
    """Handle the inline query."""
    #So I type @ followed by the bot's username followed by a space...
    query = update.inline_query.query

    #...and these are the things that pop out!
    results = [

        InlineQueryResultArticle(
            id=uuid4(),
            title="Bountie App",
            input_message_content=
            InputTextMessageContent("https://app.bountie.io/",parse_mode=ParseMode.MARKDOWN),
            description="Get Paid to Play Today!",
            thumb_url="https://scontent.fsin9-2.fna.fbcdn.net/v/t1.0-9/60835836_926856927706288_2637550626338242560_o.png?_nc_cat=111&_nc_oc=AQkF6NEDJr3W8c_yEnG8b9BAhd7zBcUcB3VMuey5LOVWH_LgGf5w-JBW8ZH-yICSgRw&_nc_ht=scontent.fsin9-2.fna&oh=24d284cb5eb58963ccad3f586821bb56&oe=5DE3E6CF"),
               
       InlineQueryResultArticle(
            id=uuid4(),
            title="Bountie Arena",
            input_message_content=
            InputTextMessageContent("https://bountie.cc/",parse_mode=ParseMode.MARKDOWN),
            description="Check out the Bountie Arena!",
            thumb_url="https://scontent.fsin9-2.fna.fbcdn.net/v/t1.0-9/60835836_926856927706288_2637550626338242560_o.png?_nc_cat=111&_nc_oc=AQkF6NEDJr3W8c_yEnG8b9BAhd7zBcUcB3VMuey5LOVWH_LgGf5w-JBW8ZH-yICSgRw&_nc_ht=scontent.fsin9-2.fna&oh=24d284cb5eb58963ccad3f586821bb56&oe=5DE3E6CF"),

        InlineQueryResultArticle(
            id=uuid4(),
            title="Bountie Store",
            input_message_content=
            InputTextMessageContent("https://bountie.store/",parse_mode=ParseMode.MARKDOWN),
            description="Buy some Bountie merch today!",
            thumb_url="https://scontent.fsin9-2.fna.fbcdn.net/v/t1.0-9/60835836_926856927706288_2637550626338242560_o.png?_nc_cat=111&_nc_oc=AQkF6NEDJr3W8c_yEnG8b9BAhd7zBcUcB3VMuey5LOVWH_LgGf5w-JBW8ZH-yICSgRw&_nc_ht=scontent.fsin9-2.fna&oh=24d284cb5eb58963ccad3f586821bb56&oe=5DE3E6CF"),
        
        InlineQueryResultArticle(
            id=uuid4(),
            title="Bountie IG",
            input_message_content=
            InputTextMessageContent("https://www.instagram.com/bountieofficial/",parse_mode=ParseMode.MARKDOWN),
            description="Bountie's Official Instagram Page!",
            thumb_url="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Instagram_logo_2016.svg/240px-Instagram_logo_2016.svg.png"),

        InlineQueryResultArticle(
            id=uuid4(),
            input_message_content=
            InputTextMessageContent("https://www.instagram.com/bountiearena/",parse_mode=ParseMode.MARKDOWN),
            title="Bountie Arena IG",
            description="Bountie Arena Instagram Page!",
            thumb_url="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Instagram_logo_2016.svg/240px-Instagram_logo_2016.svg.png"),

        InlineQueryResultArticle(
            id=uuid4(),
            title="Bountie FB",
            input_message_content=
            InputTextMessageContent("https://www.facebook.com/BountieGaming/",parse_mode=ParseMode.MARKDOWN),
            description="Bountie's Official Facebook Page!",
            thumb_url="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/F_icon.svg/240px-F_icon.svg.png"),

        InlineQueryResultArticle(
            id=uuid4(),
            title="Bountie Youtube",
            input_message_content=
            InputTextMessageContent("https://www.youtube.com/channel/UCuNU-w5R3UWUmKcbkLo4dGg/",parse_mode=ParseMode.MARKDOWN),
            description="Bountie's Official Youtube Channel!",
            thumb_url="https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/YouTube_social_white_squircle_%282017%29.svg/240px-YouTube_social_white_squircle_%282017%29.svg.png"),

        InlineQueryResultArticle(
            id=uuid4(),
            title="Check Crypto Prices",
            input_message_content=
            InputTextMessageContent(str(big_spaced_list),parse_mode=ParseMode.MARKDOWN),
            description="Lists BTC, ETH and BNTE price info!",
            thumb_url="https://en.bitcoin.it/w/images/en/2/29/BC_Logo_.png"),

        InlineQueryResultArticle(
            id=uuid4(),
            title="Buy Bountie Tokens with Bitcoin!",
            input_message_content=
            InputTextMessageContent("https://latoken.com/exchange/BTC-BNTE",parse_mode=ParseMode.MARKDOWN),
            description="Link to LAToken to buy BNTE!",
            thumb_url="https://en.bitcoin.it/w/images/en/2/29/BC_Logo_.png")
        ]

    #Once the user clicks enter, the results will pop out!
    update.inline_query.answer(results)


def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    # Create the Updater and pass it your bot's token.
    
    # Get the bot token ID after creating a bot from the BotFather. Check out README for more info!
    updater = Updater("Telegram Bot Token ID")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Identify the slash commands
    dp.add_handler(CommandHandler("start", start))

    # Initial inline query handling
    dp.add_handler(InlineQueryHandler(inlinequery))

#    # Uncomment to initiate error logging for diagnostics purposes
#    dp.add_error_handler(error)

    # Start the bot
    updater.start_polling()

    # Bot will run until someone presses ctrl-c on the terminal that the bot is running on
    updater.idle()


#if __name__ == '__main__':
#    main()

