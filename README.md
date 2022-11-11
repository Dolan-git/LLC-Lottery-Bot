# LLC-Lottery-Bot
A discord bot to track the LoveLace Club lottery on Cardano

## Requirements:
1. Python 3
1. A blackfrost.io api key
2. A discord developer token

## Steps to build:
1. Create a python virtual environment: `python3 -m venv /path/to/new/virtual/environment`
2. Activate the environment and run `pip install -r requirements.txt`
3. a. Set the PROJECT_ID environment variable to your blockfrost.io api key: `export PROJECT_ID={blackfrost_key}`

   b. Set the TOKEN environment variable to your discord developer token: `export TOKEN={discord_token}`
4. Run bot.py with python3: `python3 bot.py`
5. Enjoy!
