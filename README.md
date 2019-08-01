# BountieBot
A Telegram bot specially made for Bountie!

Hello whoever is taking over BountieBot! There are some important steps to follow in order to get this bot set up correctly!

Step 1: Installing Python 3.7
This bot is written and run in Python. We need this to get up and running!

For Windows:
https://www.ics.uci.edu/~pattis/common/handouts/pythoneclipsejava/python.html

It is very important to tick the box labelled "Add Python 3.7 to PATH"

After you are done installing, open up a Command Prompt window (windows key followed by a search for "cmd")
Type in python
Python 3.7.0 (other text) should appear.
If not, you probably did not add Python 3.7 to PATH.
Follow these instructions to fix this:
https://geek-university.com/python/add-python-to-the-windows-path/

For Mac:
https://wsvincent.com/install-python3-mac/

Open up a terminal window (Click the spotlight magnifying glass icon and type Terminal)
Copy and paste these commands exactly as they appear below. Follow the on-screen instructions.

xcode-select --install

/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

brew doctor

brew install python3

python3 --version

Step 2: Download Sublime Text Editor
This is an easy step. We need this to make changes to the BountieBot.py file!

Go to https://www.sublimetext.com/3
Download the correct version based on the system that you are using.

Step 3: Install the relevant modules on your computer
The BountieBot.py file requires several modules to grab information and/or run properly!

For Windows and Mac:
Open up a command prompt/Terminal window
Type the below commands as they appear:

pip3 install uuid, logging, json, requests, coinbase
pip3 install python-telegram-bot


Step 4: Creating the Bot container using Telegram's BotFather
You need a bot container!

First, go to your browser on your phone or your desktop.
Type in https://t.me/botfather
Start BotFather
Type in /newbot to create a new bot.
The first prompt will be to give the bot a display name.
The second prompt will be to give the bot an @ username.

After you are done, BotFather will give you an API-Key.
Open up BountieBot.py using Sublime Text.
Scroll down to line 176, and paste the API-Key where it says "Telegram Bot Token ID". Make sure the key is surrounded by double apostrophes.
It should be something like: updater = Updater("XXX-XXXXX-XXXXX-XXXX")

Next, enable inline mode for the @ space menu options. In BotFather, type /mybots, pick your newly created bot, and press "Bot Settings", followed by "Inline Mode". Turn inline mode on. You should also add some placeholder text.

Lastly, if you type in the /mybots command and press the "Edit Bot" option, you can pick your newly created bot and edit the various features, such as name and description.

Step 5: Getting Coinbase API Key and Secret
We can get prices from a public endpoint, but for some reason the coinbase module still requires an API key. -.-

Go to coinbase.com and create a new account.
After you are done with that, log in to your account.
On the top right hand corner, click your profile, followed by Settings
On the top row, click API Access
On the top right corner, click + New API Key
Now, you should see a box with a bunch of checkboxes. On the top, check LTC wallet, and on the bottom, check wallet:transactions:read. Press Create.
IMPORTANT: At this point, store your API Key and Secret somewhere safe. You cannot retrieve them from the coinbase site once you close the window!

Next, open up BountieBot.py using Sublime Text 3, and navigate to line 31. Paste your API Key and Secret in the appropriate fields.
Don't close the Sublime window just yet!

Step 6: Last cosmetic change in BountieBot.py
Go to line 71, and replace the (Edit with bot name) with the bot username that you created in Step 4.

Step 7: Run the bot!
Moment of truth!

First off, for easy navigation, drag BountieBot.py over to your desktop.

For Windows and Mac:
Open a command prompt/Terminal window and type the following command:
cd desktop
python3 BountieBot.py

Nothing will get printed on the command prompt/Terminal window, but that is ok.

Go to your web browser and type in t.me/(bot's username without the @)
The bot should automatically force you to output /start, and the bot will say Hi! Type @(Edit with bot name) to begin!

If you set everything up correctly, you can ping the bot by typing @, followed by the bot's username, followed by a space. Some placeholder text should appear if you set it up right in Step 4. After a while, some menu options should appear.

Step 8: Rejoice!
For you are done!

If there are any issues, feel free to open up a new issue on the Github page!




 













