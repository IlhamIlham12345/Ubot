import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "200"))

DEVS = list(map(int, os.getenv("DEVS", "8078574143").split()))

API_ID = int(os.getenv("API_ID", "27216878"))

API_HASH = os.getenv("API_HASH", "5d522cb56680802e92cb6301d59d7163")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8375169793:AAGG1X65Nci4s-1oMykyOTEPkXMdSFartCs")

OWNER_ID = int(os.getenv("OWNER_ID", "8078574143"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002312835928").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://Indiaindiahottt:Indiaindiahottt@indiaindiahottt.o3ihegl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002312835928"))
