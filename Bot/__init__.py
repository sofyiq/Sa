from pyrogram import Client
import pyromod

app = Client(
    "MediaDownloader",
    api_id=22931198,
    api_hash="8b80a7b0fa90f97e0b5002cded828694",
    bot_token="5249469006:AAEyC4hMWvcrZ8dTfY14dd_QTh7sqfroBO4",
    plugins=dict(root="Bot/handlers")
)
