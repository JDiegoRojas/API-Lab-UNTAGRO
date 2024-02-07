from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import http.client
import json
import os
from dotenv import load_dotenv

load_dotenv()
telegram_token = os.getenv("TELEGRAM_TOKEN")

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def get_materiales(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    conexion=http.client.HTTPConnection("localhost",8000)
    conexion.request("GET","/materiales/")
    respuesta=conexion.getresponse()
    respuesta_api=respuesta.read().decode("UTF-8")
    materiales=json.loads(respuesta_api)

    mensaje=""
    for material in materiales:
        mensaje+=f'Nombre: {material.get("nombre","")}, Marca: {material.get("marca","")}\n'

    await update.message.reply_text(mensaje)


app = ApplicationBuilder().token(telegram_token).build()

app.add_handler(CommandHandler("hello", hello))

app.add_handler(CommandHandler("materiales", get_materiales))


app.run_polling()
