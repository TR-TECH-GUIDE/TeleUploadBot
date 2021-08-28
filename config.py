import os

BOTTOKEN = os.environ.get("BOTTOKEN", "")
APIID = int(os.environ.get("APIID", 12345))
APIHASH = os.environ.get("APIHASH", "lelhutto0")
DOWNLOADPATH = os.environ.get("DOWNLOADPATH", "Downloads/")
USERNAME = os.environ.get("USERNAME", "")

"""
If you using VPS, first fork repo, remove upper strings and edit like this:

BOTTOKEN = "" # your bot token frpm @BotFather
APIID =      # your api id from https://my.telegram.org/
APIHASH = "" # your api hash from https://my.telegram.org/
DOWNLOADPATH = "Downloads/" # don't change
USERNAME = "" # put your bot username here
"""
