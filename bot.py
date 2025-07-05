from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Olá! Eu sou um bot.")

app = ApplicationBuilder().token("AAE5tXJshmfblGwQaO0qSMbJPKron2G43P0").build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
