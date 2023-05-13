import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()


# FOR CODES

API_ID = int(getenv("API_ID", "27424332"))
API_HASH = getenv("API_HASH", "cb93e76ed8e78c8081f52cd3aa66f08b")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5348648456").split()))
LOGGER = int(getenv("LOGGER", "-1001948541213")
OWNER = int(getenv("OWNER_ID", "6099950428"))
NAME = getenv("ALIVE_NAME")
OWN_USERNAME= getenv("OWN_USERNAME", "@Ankit_Varma42")
ALIVE_PIC = getenv("ALIVE_PIC", "https://te.legra.ph/file/e423cd7f9c3ce51d48d20.jpg")

# FOR SPAMBOT

TOKEN1 = getenv("TOKEN1", "6032040315:AAFyBtAEBGf3RDgl-DjSiQUejFexmeDDnDI") 
TOKEN2 = getenv("TOKEN2", "6087616147:AAHYk5umnz10lgJpRs6-IvGbuUEfXh_RR5E") 
TOKEN3 = getenv("TOKEN3", None) 
TOKEN4 = getenv("TOKEN4", None) 
TOKEN5 = getenv("TOKEN5", None) 
TOKEN6 = getenv("TOKEN6", None) 
TOKEN7 = getenv("TOKEN7", None) 
TOKEN8 = getenv("TOKEN8", None) 
TOKEN9 = getenv("TOKEN9", None) 
TOKEN10 = getenv("TOKEN10", None) 
