import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from PIL import Image, ImageDraw

TOKEN = os.environ.get("TOKEN")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    img = Image.new('RGB', (1280, 720), color=(20, 20, 20))
    draw = ImageDraw.Draw(img)

    draw.text((200, 300), text, fill="white")
    draw.text((950, 650), "PrimePixelBot", fill="gray")

    img.save("poster.png")

    await update.message.reply_photo(photo=open("poster.png", "rb"))

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()
